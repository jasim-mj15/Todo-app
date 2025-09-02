# 📝 Todo App — Flask-based Task Manager

A simple yet functional **To-Do List** web application built with Flask, containerized with Docker, and automated with CI/CD. Includes support for deployment to AWS via Elastic Beanstalk using CI workflows.

---

##  Project Overview

This project demonstrates end-to-end DevOps practices:
- **Flask** web app for managing tasks (create, update, delete).
- **Docker** containerization for consistent deployment.
- **CI/CD pipelines** using AWS CodeBuild or GitHub Actions.
- **AWS Elastic Beanstalk** deployment and configuration.
- **Buildspec and CI workflow YAMLs** included for automation.

---

##  Tech Stack & Tools

| Layer         | Technologies Used                           |
|---------------|---------------------------------------------|
| Backend       | Python, Flask                               |
| UI            | HTML (templates folder) + static files      |
| Container     | Docker, Dockerfile                          |
| CI/CD         | AWS CodeBuild (`buildspec.yml`), GitHub Actions (`ci-cd.yml`) |
| Cloud Infra   | AWS Elastic Beanstalk                       |

---

##  Repository Structure

.
├── app.py # Core Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Container image definition
├── .ebextensions/ # EB environment configurations
├── buildspec.yml # AWS CodeBuild spec
├── ci-cd.yml # GitHub Actions CI/CD workflow
├── templates/ # HTML templates
├── static/ # Static assets (CSS, JS, etc.)
└── README.md # This documentation
