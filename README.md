# AI Job Recommender with Chatbot

## 📌 Project Overview

AI Job Recommender is a web application that analyzes a user's resume and recommends suitable jobs based on the skills found in the resume.  
It also includes a simple AI chatbot that helps guide users while searching for jobs.

The system extracts skills from the resume and compares them with available job roles to provide the best matching opportunities.

---

## 🚀 Features

- Upload Resume (PDF)
- Skill extraction from resume
- Job recommendation based on skills
- Matching score for each job
- Apply button that opens the official company website
- Simple AI chatbot assistant
- Clean UI with gradient background
- Responsive layout

---

## 🛠 Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- NLP (for resume skill matching)

---

## 📂 Project Structure

```
AI_JOB_RECOMMENDER/
│
├── app.py
├── chatbot.py
├── job_matcher.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── dataset/
│   └── jobs.csv
│
└── README.md
```

---

## ⚙️ Installation Steps

### Step 1: Install Python

Download and install Python from  
https://www.python.org/

---

### Step 2: Install Required Libraries

Open terminal or command prompt and run:

```
pip install flask pandas scikit-learn
```

---

### Step 3: Run the Project

Navigate to the project folder and run:

```
python app.py
```

---

### Step 4: Open in Browser

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📊 How It Works

1. User uploads resume
2. System extracts skills
3. Skills are compared with job dataset
4. Matching score is calculated
5. Best jobs are displayed

---

## 🔮 Future Improvements

- LinkedIn job integration
- Real-time job scraping
- Better resume parsing using NLP models
- User authentication system
- Dashboard for job tracking
