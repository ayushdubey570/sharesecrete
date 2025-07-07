# 🔐 ShareSecrete — One-Time Secret Sharing App

ShareSecrete is a micro SaaS web app that allows users to share **sensitive messages securely via one-time links**. Once a secret is viewed, it's destroyed permanently — perfect for passwords, OTPs, or confidential info.

Built with:
- 🐍 Flask (Python)
- 🗃️ SQLite (local DB)
- 🔐 Cryptography (AES encryption via Fernet)
- 🎨 Tailwind CSS (clean and responsive UI)
- ☁️ Render (for free deployment)

---

## ✨ Features

- 🔒 Create a one-time secret
- 🔗 Unique, random slug-based shareable link
- 💥 Link can be used only once
- 🔐 AES-256 encryption using `cryptography`
- 🧹 Secret auto-deletes after being viewed
- 🌈 Simple & modern UI with Tailwind CSS

---

## 📸 Screenshots


![home](https://github.com/user-attachments/assets/d8f88a51-7882-4515-baca-78dbe5a81682) 

![show](https://github.com/user-attachments/assets/82b2f889-0fce-47cb-abfe-1d697d473f5c) 

![not found](https://github.com/user-attachments/assets/8b941a66-b5fb-4ac3-bcb0-3bd4039f89dc) 

---

## 🛠 Local Setup

### 1. ⬇️ Clone or Download

```bash
git clone https://github.com/ayushdubey570/sharesecrete.git
cd sharesecrete
```

Or download the ZIP and unzip it.

---

### 2. 🐍 (Optional) Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\\Scripts\\activate        # Windows
```

---

### 3. 📦 Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4. 🚀 Run the App

```bash
python app.py
```

Open browser → [http://localhost:5000](http://localhost:5000)

---

## ☁️ Free Hosting on Render

### 🔧 1. Push to GitHub

If not already:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/username/repo.git
git push -u origin main
```

---

### 🔧 2. Deploy on Render

1. Go to [https://render.com](https://render.com)
2. Click **New → Web Service**
3. Connect your GitHub repo
4. Set:

| Setting          | Value                          |
|------------------|--------------------------------|
| Build Command    | `pip install -r requirements.txt` |
| Start Command    | `gunicorn app:app`             |
| Runtime          | Python                         |

5. Click **Deploy** 🎉

---

## 📁 Project Structure

```
sharesecrete/
├── app.py                # Main Flask app
├── requirements.txt      # Dependencies
├── secret.key            # Generated key (auto)
├── secrets.db            # SQLite DB (auto)
├── render.yaml           # Render deploy config
├── templates/            # Tailwind HTML templates
│   ├── home.html
│   ├── show.html
│   └── notfound.html
└── .gitignore            # Ignore DB, secrets, etc.
```

---

## 🧾 Security Notes

- ✔ Uses strong AES encryption via `cryptography.fernet`
- ❌ `secret.key` is excluded from Git via `.gitignore`
- 💥 Secret auto-deletes after first read
- ⚠ Never expose `secret.key` in production or GitHub

---

## 🔒 .gitignore Example

```gitignore
secret.key
secrets.db
__pycache__/
*.pyc
*.log
.env
```

Run this to remove `secret.key` from Git if already committed:

```bash
git rm --cached secret.key
```

---

## 🧠 Future Upgrades (Optional)

- ⏳ Secret expiration timers (e.g., after 10 minutes or 24h)
- 🔐 Password-protected secrets
- 📊 Admin dashboard (with login)
- 📱 Fully mobile-optimized UI
- 🌍 Multilingual support

---

## 👨‍💻 Author

**Ayush Dubey**  
📧 ayushdubey570@gmail.com  
🔗 [GitHub @ayushdubey570](https://github.com/ayushdubey570)

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use and modify it commercially or personally.

---

> 🛡 If you use this in production, consider switching to PostgreSQL and using environment variables for secrets.
