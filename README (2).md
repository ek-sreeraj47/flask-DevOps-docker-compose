# 🐳 Flask DevOps Project: Docker + MongoDB Atlas + Render Deployment

This is a beginner-friendly DevOps project where a simple Flask web application is containerized with Docker, connected to a cloud MongoDB Atlas database, tested with GitHub Actions CI, and deployed to [Render](https://flask-devops-docker-compose.onrender.com) using a Docker-based workflow.

---

## 🚀 Live Demo

🌐 [https://flask-devops-docker-compose.onrender.com](https://flask-devops-docker-compose.onrender.com)

- `/` → Confirms MongoDB connection
- `/health` → Simple health check

---

## 🛠️ Tech Stack

- **Python** + **Flask**
- **MongoDB Atlas** (Free Tier Cloud DB)
- **Docker** (containerized app)
- **GitHub Actions** (CI Pipeline)
- **Render** (cloud deployment platform)

---

## 📁 Project Structure

```
.
├── app.py                     # Flask application code
├── Dockerfile                # Container setup
├── requirements.txt          # Python dependencies
└── .github
    └── workflows
        └── docker.yml        # GitHub Actions workflow file
```

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Repo

```bash
git clone https://github.com/ek-sreeraj47/flask-DevOps-docker-compose.git
cd flask-DevOps-docker-compose
```

### 🐍 2. Install Dependencies (Optional for local test)

```bash
pip install -r requirements.txt
python app.py
```

### 🐳 3. Build Docker Image

```bash
docker build -t flask-devops-app .
```

### 🧪 4. Run Locally with Docker

```bash
docker run -p 5000:5000 -e MONGO_URI="<your MongoDB URI>" flask-devops-app
```

---

## 🧪 GitHub Actions CI

- Workflow is defined in `.github/workflows/docker.yml`
- On every push, it:
  1. Builds Docker image
  2. Checks build success
  3. (Optional) Pushes to DockerHub

---

## ☁️ Deployment on Render

Steps:

1. Push code to GitHub
2. Login to [Render](https://render.com)
3. Create new Web Service from repo
4. Choose:
   - Environment: `Docker`
   - Region: `Asia/Singapore or Mumbai`
5. Set Environment Variable:

```bash
Key:    MONGO_URI
Value:  mongodb+srv://admin:<password>@cluster0.xyz.mongodb.net/devopsdb?retryWrites=true&w=majority
```

6. Deploy 🚀

---

## 🔐 Environment Variables

| Key        | Description                       |
|------------|-----------------------------------|
| `MONGO_URI` | MongoDB Atlas connection string  |

---

## ✅ Routes

| Route        | Description                        |
|--------------|------------------------------------|
| `/`          | Checks MongoDB connection status   |
| `/health`    | Returns `OK` (used for health checks) |

---

## 📄 License

This project is free to use for learning and portfolio purposes.

---

## 🙌 Credits

Built by **[@ek-sreeraj47](https://github.com/ek-sreeraj47)** as part of a DevOps learning journey.
