# Final Project – Containerized Python App with PostgreSQL and CI/CD on Azure

This project was developed as part of my vocational education in Cloud and Virtualization at Campus Mölndal (2025).  
It demonstrates how to build, deploy, and manage a containerized Python application connected to a PostgreSQL database using modern DevOps tools.

## 🔧 Technologies Used

- **Python**  
- **PostgreSQL**  
- **Docker**  
- **Azure DevOps (Pipelines)**  
- **Azure App Service**  
- **psycopg2** (PostgreSQL client library for Python)

## 📦 Project Overview

The application:
- Connects to a PostgreSQL database to fetch and store structured data
- Validates input and handles basic CRUD operations
- Is packaged in a Docker container for portability
- Is deployed via CI/CD pipeline using Azure DevOps to an Azure App Service

## 🛠 Features

- Automated build and deployment with Azure DevOps
- Containerized environment using Docker
- Real-time interaction with PostgreSQL database
- Accessible via web browser
- Clear logging and basic error handling

## 🚀 How to Run Locally

```bash
git clone https://github.com/SamirMohamed24/Student-Data-Manager.git
cd examensarbete
docker build -t python-app .
docker run -e DB_USER=admin -e DB_PASSWORD=dittlösenord -p 5000:5000 python-app


📁 Folder Structure


├── app_files/
│   ├── student_app.py
│   └── student_image.jpg
├── requirements.txt
├── Dockerfile
└── README.md

🐳 Docker Commands

# Build Docker image
docker build -t <your-dockerhub-username>/<your-image-name> .

# Push to Docker Hub
docker push <your-dockerhub-username>/<your-image-name>
🚀 Azure DevOps Pipelines
Build Pipeline: Automates building and pushing the Docker image.

Release Pipeline: Pulls from Docker Hub and deploys to Azure App Service.

Stages: Includes release, restart of app service, and smoke testing.

🧪 App Features
Web form to input:

Name, address, email, phone

File format (radio buttons)

Languages (checkboxes)

File upload (saved as binary)

Data saved to PostgreSQL

🗄️ Database Schema (PostgreSQL)


CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name TEXT,
  address TEXT,
  email TEXT,
  phone BIGINT,
  certificate TEXT,
  languages TEXT,
  image BYTEA
);

🧠 Author
Samir Mohamed




