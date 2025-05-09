
# Examensarbete – Containeriserad Python-applikation med PostgreSQL och CI/CD i Azure

Detta projekt utvecklades som en del av min yrkeshögskoleutbildning inom moln- och virtualisering vid Campus Mölndal (2025).  
Syftet är att visa hur man bygger, distribuerar och hanterar en containeriserad Python-applikation som är kopplad till en PostgreSQL-databas med moderna DevOps-verktyg.

## 🔧 Använda tekniker

- **Python**  
- **PostgreSQL**  
- **Docker**  
- **Azure DevOps (Pipelines)**  
- **Azure App Service**  
- **psycopg2** (PostgreSQL-klient för Python)

## 📦 Projektöversikt

Applikationen:
- Ansluter till en PostgreSQL-databas för att hämta och lagra strukturerad data
- Validerar indata och hanterar grundläggande CRUD-operationer
- Paketeras i en Docker-container för portabilitet
- Distribueras via en CI/CD-pipeline med Azure DevOps till Azure App Service

## 🛠 Funktioner

- Automatiserad build och deployment med Azure DevOps
- Containerbaserad drift med Docker
- Realtidskommunikation med PostgreSQL
- Tillgänglig via webbläsare
- Enkel loggning och felhantering

## 🚀 Så här kör du lokalt

```bash
git clone https://github.com/SamirMohamed24/Student-Data-Manager.git
cd examensarbete
docker build -t python-app .
docker run -e DB_USER=admin -e DB_PASSWORD=dittlösenord -p 5000:5000 python-app


📁 Projektstruktur
/app
  ├── main.py
  ├── requirements.txt
  ├── Dockerfile
  └── README.md
