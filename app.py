import streamlit as st
from db import SessionLocal
from models import User, Project, Task

st.set_page_config(page_title="Team Task Manager", layout="centered")

st.title("📌 Team Task Manager")

db = SessionLocal()

menu = ["Login", "Signup", "Dashboard"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- SIGNUP ----------------
if choice == "Signup":
    st.subheader("Create Account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):
        if username and password:
            user = User(username=username, password=password)
            db.add(user)
            db.commit()
            st.success("Account created successfully!")
        else:
            st.error("Fill all fields")

# ---------------- LOGIN ----------------
elif choice == "Login":
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = db.query(User).filter_by(username=username, password=password).first()
        if user:
            st.session_state["user"] = username
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

# ---------------- DASHBOARD ----------------
elif choice == "Dashboard":

    if "user" not in st.session_state:
        st.warning("Please login first")
    else:
        st.subheader(f"Welcome {st.session_state['user']}")

        project_name = st.text_input("Project Name")

        if st.button("Create Project"):
            if project_name:
                p = Project(name=project_name, created_by=st.session_state["user"])
                db.add(p)
                db.commit()
                st.success("Project created!")
            else:
                st.error("Enter project name")

        st.markdown("---")

        task_title = st.text_input("Task Title")
        assigned_to = st.text_input("Assign To")
        due_date = st.text_input("Due Date")

        if st.button("Add Task"):
            if task_title:
                t = Task(
                    title=task_title,
                    assigned_to=assigned_to,
                    due_date=due_date,
                    status="todo",
                    project_id=1
                )
                db.add(t)
                db.commit()
                st.success("Task added!")
            else:
                st.error("Enter task title")

        st.markdown("---")
        st.subheader("All Tasks")

        tasks = db.query(Task).all()
        for t in tasks:
            st.write(f"📌 {t.title} | {t.status} | {t.assigned_to} | {t.due_date}")