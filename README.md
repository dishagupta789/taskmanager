# 📌 Team Task Manager (Streamlit + Python)

A simple full-stack task management web application built using Python and Streamlit.  
This project helps users manage projects, assign tasks, and track task progress efficiently.

---

## 🚀 Features

- User Signup & Login (Session-based authentication)
- Create and manage Projects
- Add Tasks under Projects
- Assign tasks to users
- Update task status (To Do / In Progress / Done)
- Track overdue tasks based on due date
- Simple dashboard to view all tasks

---

## 🛠️ Tech Stack

- Python
- Streamlit
- SQLite (Database)
- SQLAlchemy (ORM)

---

## 📁 Project Structure

task manager/
│── app.py  
│── db.py  
│── models.py  
│── create_db.py  
│── requirements.txt  

---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/your-username/task-manager.git  
cd task-manager  

---

### 2. Install dependencies
pip install -r requirements.txt  

---

### 3. Create database
python create_db.py  

---

### 4. Run the application
streamlit run app.py  

---

## 🌐 Deployment

This project is deployed using Railway.

Live URL: (https://taskmanager-production-166d.up.railway.app/)

---

## 🎯 How it works

- User creates account (signup/login)
- Creates a project
- Adds tasks under project
- Assigns tasks to users
- Tracks status in dashboard

---

## 📌 Future Improvements

- Role-based access (Admin / Member)
- Task edit & delete functionality
- Better UI design with Streamlit components
- Email notifications for overdue tasks
- Real-time updates

---

## 👩‍💻 Author

Developed by Seema Gupta

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub
