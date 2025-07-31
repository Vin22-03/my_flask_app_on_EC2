# 🚀Cloud-Deployed Flask App using Docker & EC2 | My First DevOps Deployment

This is a beginner-friendly DevOps mini-project that demonstrates how to:

- Build a Python Flask app 🐍
- Use Git & GitHub for version control 🔧
- Containerize the app using Docker 🐳
- Deploy it on a live EC2 instance via AWS ☁️
- Expose the app to the internet using Security Groups 🌐

---

## 🎯 Project Objectives

- ✅ Build a simple web app using Flask
- ✅ Version control using Git and push to GitHub
- ✅ Create a Dockerfile and build a custom Docker image
- ✅ Launch an EC2 Ubuntu instance on AWS
- ✅ SSH into the instance and run the app containerized
- ✅ Open port 80 via Security Group for global access

---

## ⚙️ Tech Stack

| Component        | Tool/Service          |
|------------------|------------------------|
| Web Framework    | Python + Flask         |
| Version Control  | Git + GitHub           |
| Containerization | Docker                 |
| Cloud Hosting    | AWS EC2 (Ubuntu 22.04) |
| Networking       | AWS Security Groups    |

---

## 📦 Project Structure

```bash
my_flask_app_on_EC2/
├── app.py
├── requirements.txt
├── Dockerfile

```
app.py

```bash
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Vin — Cloud in the making 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

##🐳 Dockerfile
```bash
Dockerfile
Copy code
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

## ✅ What I Learned

Basics of cloud deployment

How Docker simplifies app portability

Security group configuration

Git workflow for live projects

## 📚 Next Steps to learn
Integrate S3 for static file storage

Use Docker Compose for multi-container app

Add CI/CD via GitHub Actions

Monitor app using CloudWatch.

# “I believe in building before I believe I’m ready.”


