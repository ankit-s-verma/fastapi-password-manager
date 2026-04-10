# 🔐 FastAPI Password Manager

### 🚀 Secure. Simple. API-Driven Credential Management

## 📌 Overview

**Tired of storing passwords in plain text or scattered notes?**
This project delivers a **secure, API-driven password manager** built with **FastAPI**, designed to demonstrate real-world backend engineering practices.

It combines **strong encryption**, **clean RESTful design**, and **modular architecture** to provide a reliable system for managing credentials safely.

At its core, this application answers a critical question:
👉 *How do you securely store and manage sensitive data in a modern web application?*

---

## ✨ Key Highlights

* 🔐 **End-to-end encryption** using Fernet (no plaintext storage)
* ⚡ **High-performance APIs** powered by FastAPI
* 🔄 **Complete CRUD workflow** with real-time frontend interaction
* 🔍 **Search-enabled credential retrieval**
* 🧩 **Clean, modular backend architecture**
* 🌐 **Frontend + API integration using Fetch**

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite
* **Encryption:** Cryptography (Fernet)
* **Frontend:** HTML, CSS, JavaScript
* **Server:** Uvicorn

---

## 📁 Project Structure

```
password-manager/
│── app/
│   ├── main.py
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── database/
│   └── utils/
│
│── static/
│── templates/
│── requirements.txt
│── README.md
```

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ankit-s-verma/password-manager.git
cd password-manager
```

### 2️⃣ Set Up Virtual Environment

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## 🌍 Live Demo

Note: The app may take a few seconds to load due to free-tier hosting.

```
https://fastapi-password-manager.onrender.com/
```



---

## 📡 API Endpoints

| Method | Endpoint       | Description                |
| ------ | -------------- | -------------------------- |
| GET    | `/`            | Home page                  |
| GET    | `/passwords`   | Retrieve all credentials   |
| POST   | `/add`         | Add new credential         |
| PUT    | `/update/{id}` | Update existing credential |
| DELETE | `/delete/{id}` | Delete credential          |

---

## 🔐 Security Architecture

Security is the core of this project:

* Passwords are encrypted using **Fernet symmetric encryption**
* Encryption happens **before database storage**
* No plaintext credentials are ever persisted
* Designed to support **environment-based key management**

---

## ⚠️ Current Limitations

* SQLite is used (suitable for development, not large-scale production)
* No authentication layer (single-user system)
* No role-based access control

---

## 🔮 Future Enhancements

* 🔑 JWT-based user authentication
* ☁️ PostgreSQL for production scalability
* 🐳 Docker containerization
* ⚛️ React frontend (SPA architecture)
* 📊 Password strength analyzer
* 🔄 Backup & recovery system

---

## 💡 What This Project Demonstrates

* Secure handling of sensitive data
* RESTful API design principles
* Backend modularization and scalability
* Real-world encryption implementation
* Frontend ↔ Backend communication

---

## 👨‍💻 Author

Ankit Verma

---

## 📜 License

This project is licensed under the MIT License.
