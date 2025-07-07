from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
import os
from datetime import datetime
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///secrets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if not os.path.exists("secret.key"):
    with open("secret.key", "wb") as f:
        f.write(Fernet.generate_key())

with open("secret.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)

class Secret(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(10), unique=True, nullable=False)
    encrypted_text = db.Column(db.Text, nullable=False)
    viewed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        secret = request.form['secret']
        slug = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        encrypted_text = fernet.encrypt(secret.encode()).decode()
        new_secret = Secret(slug=slug, encrypted_text=encrypted_text)
        db.session.add(new_secret)
        db.session.commit()
        return render_template('home.html', link=request.host_url + 's/' + slug)
    return render_template('home.html', link=None)

@app.route('/s/<slug>')
def show(slug):
    secret = Secret.query.filter_by(slug=slug).first()
    if secret and not secret.viewed:
        secret.viewed = True
        db.session.commit()
        decrypted = fernet.decrypt(secret.encrypted_text.encode()).decode()
        return render_template('show.html', secret=decrypted)
    else:
        return render_template('notfound.html')

if __name__ == '__main__':
    app.run(debug=True)
