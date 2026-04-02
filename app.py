import streamlit as st
import pandas as pd
from operations import *

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN / SIGNUP ----------------
if not st.session_state.logged_in:

    st.title("🔐 Login System")

    option = st.selectbox("Select", ["Login", "Signup"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if option == "Signup":
        if st.button("Create Account"):
            create_user(username, password)
            st.success("Account created! Now login.")

    elif option == "Login":
        if st.button("Login"):
            user = login_user(username, password)

            if user:
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()

# ---------------- MAIN APP ----------------

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.title("🎓 Student Management System")

menu = ["Add Student", "View Students", "Search", "Update", "Delete", "Analytics"]
choice = st.sidebar.selectbox("Menu", menu)

# ➕ Add Student
if choice == "Add Student":
    st.subheader("Add Student")

    name = st.text_input("Name")
    age = st.number_input("Age", 1, 100)
    course = st.text_input("Course")
    marks = st.number_input("Marks", 0, 100)

    if st.button("Add"):
        add_student(name, age, course, marks)
        st.success("Student Added!")

# 👀 View Students
elif choice == "View Students":
    st.subheader("All Students")

    data = get_students()
    df = pd.DataFrame(data, columns=["ID", "Name", "Age", "Course", "Marks"])

    
    df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
    df = df.dropna()

    st.dataframe(df)

# 🔍 Search
elif choice == "Search":
    st.subheader("Search Student")

    search_name = st.text_input("Enter name")

    if st.button("Search"):
        data = search_students(search_name)
        df = pd.DataFrame(data, columns=["ID", "Name", "Age", "Course", "Marks"])

        
        df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
        df = df.dropna()

        st.dataframe(df)

# ✏️ Update
elif choice == "Update":
    st.subheader("Update Student")

    student_id = st.number_input("Enter ID", 1)
    name = st.text_input("New Name")
    age = st.number_input("New Age", 1, 100)
    course = st.text_input("New Course")
    marks = st.number_input("New Marks", 0, 100)

    if st.button("Update"):
        update_student(student_id, name, age, course, marks)
        st.success("Student Updated!")

# ❌ Delete
elif choice == "Delete":
    st.subheader("Delete Student")

    student_id = st.number_input("Enter ID to delete", 1)

    if st.button("Delete"):
        delete_student(student_id)
        st.success("Student Deleted!")

# 📊 Analytics
elif choice == "Analytics":
    st.subheader("Analytics")

    data = get_students()
    df = pd.DataFrame(data, columns=["ID", "Name", "Age", "Course", "Marks"])

    df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
    df = df.dropna()

    st.write("📈 Marks Distribution")
    st.bar_chart(df["Marks"])

    st.write("📊 Course-wise Average Marks")
    course_avg = df.groupby("Course")["Marks"].mean()
    st.bar_chart(course_avg)

    st.write("🏆 Topper")
    topper = df.loc[df["Marks"].idxmax()]
    st.write(topper)