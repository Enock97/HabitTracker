# Habit Tracker

A responsive intermediate-level full-stack habit tracking application built with a **React + Material UI frontend (Vercel)** and a **Python FastAPI backend (AWS Lambda + DynamoDB)** for the purpose of learning fullstack React + Python and deployment to AWS.

## Features

- Track daily habits with create, read, update, and delete (CRUD) functionality
- Real-time UI updates and smooth user experience with dark mode toggle
- Serverless backend with FastAPI, deployed to AWS Lambda using the Serverless Framework
- Persistent data storage in AWS DynamoDB
- Frontend deployed on Vercel with full CORS integration
- Clean, intuitive interface and scalable architecture

## Tech Stack

- **Front-end:** React, TypeScript, Material UI
- **Back-end:** Python using FastAPI + Mangum (AWS Lambda)
- **Database:** AWS DynamoDB (NoSQL)
- **API Docs:** Auto-generated with OpenAPI (Swagger UI)
- **Cloud & DevOps:** AWS (CloudFormation), Vercel
- **Tools:** VS Code, YouTube (freeCodeCamp.org), GPT-4

## Try the App

Test the live application here: 
- **[Live App (Vercel)](https://habit-tracker-two-virid.vercel.app/)**
- **[API Check (AWS)](https://pogv79s4w9.execute-api.eu-north-1.amazonaws.com/)**

<br>

Live application availability (YES/NO): **YES**

## Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/habit-tracker.git
```

### 2. Install dependencies

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Frontend

```bash
cd frontend
npm install
```

### 3. Start the project

#### Backend

```bash
uvicorn app.main:app --reload
```

#### Frontend

```bash
npm start
```

## Developer

**Enock Ladu – Full-Stack Developer**: [LinkedIn Profile](https://www.linkedin.com/in/enock-ladu-b56b0724b/) / Oslo, Norway
