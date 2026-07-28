import streamlit as st
import pandas as pd


# ---------------- Student Class ---------------- #

class Student:
    def __init__(self):
        self.student = {}

    # Add Student
    def add_student(self, name, age, roll_no, city):
        if roll_no in self.student:
            return False, "Student with this roll number already exists."

        self.student[roll_no] = {
            "name": name,
            "age": age,
            "city": city
        }
        return True, f"{name} added successfully."

    # Get All Students records 
    def get_student(self):
        return self.student

    # Get Student By Roll No.
    def get_student_by_roll_no(self, roll_no):
        return self.student.get(roll_no)

    # Update Student to edit the previous one....
    def update_student(self, roll_no, name, age, city):
        if roll_no not in self.student:
            return False, "Student not found."

        self.student[roll_no] = {
            "name": name,
            "age": age,
            "city": city
        }

        return True, "Student updated successfully."

    # Delete Student
    def drop_student(self, roll_no):
        if roll_no not in self.student:
            return False, "Student not found."

        del self.student[roll_no]
        return True, "Student deleted successfully."


# ---------------- Session State ---------------- #

if "student_obj" not in st.session_state:
    st.session_state.student_obj = Student()

    # Default Records
    st.session_state.student_obj.add_student("Dheeraj", 30, 7878, "Gwalior")
    st.session_state.student_obj.add_student("Rahul", 30, 9420, "Bamor")
    st.session_state.student_obj.add_student("Raghav", 33, 9421, "Nurabaad")
    st.session_state.student_obj.add_student("Saumya", 25, 1234, "Nurabaad")

student = st.session_state.student_obj


# ----------------for visualization  ---------------- #

st.set_page_config(page_title="Student Management System", layout="wide")

st.title("🎓 Student Management System")

menu = st.sidebar.radio(
    "Select Operation",
    [
        "Add Student",
        "View All Students",
        "Search Student",
        "Update Student",
        "Delete Student",
    ],
)


# ===================================================
# Add Student
# ===================================================

if menu == "Add Student":

    st.header("➕ Add Student")

    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    roll = st.number_input("Roll Number", min_value=1)
    city = st.text_input("City")

    if st.button("Add Student"):

        status, msg = student.add_student(
            name,
            int(age),
            int(roll),
            city,
        )

        if status:
            st.success(msg)
        else:
            st.error(msg)


# ===================================================
# View All Students
# ===================================================

elif menu == "View All Students":

    st.header("📋 All Students")

    data = student.get_student()

    if data:

        df = pd.DataFrame.from_dict(data, orient="index")

        df.index.name = "Roll Number"

        st.dataframe(df, use_container_width=True)

    else:
        st.warning("No student found.")


# ===================================================
# Search Student
# ===================================================

elif menu == "Search Student":

    st.header("🔍 Search Student")

    roll = st.number_input(
        "Enter Roll Number",
        min_value=1,
        key="search",
    )

    if st.button("Search"):

        result = student.get_student_by_roll_no(int(roll))

        if result:

            st.success("Student Found")

            st.write("### Details")

            st.write(f"**Roll Number :** {roll}")
            st.write(f"**Name :** {result['name']}")
            st.write(f"**Age :** {result['age']}")
            st.write(f"**City :** {result['city']}")

        else:
            st.error("Student not found.")


# ===================================================
# Update Student
# ===================================================

elif menu == "Update Student":

    st.header("✏ Update Student")

    roll = st.number_input(
        "Roll Number",
        min_value=1,
        key="update_roll",
    )

    name = st.text_input("New Name")
    age = st.number_input(
        "New Age",
        min_value=1,
        max_value=100,
        key="update_age",
    )
    city = st.text_input("New City")

    if st.button("Update Student"):

        status, msg = student.update_student(
            int(roll),
            name,
            int(age),
            city,
        )

        if status:
            st.success(msg)
        else:
            st.error(msg)


# ===================================================
# Delete Student
# ===================================================

elif menu == "Delete Student":

    st.header("🗑 Delete Student")

    roll = st.number_input(
        "Roll Number",
        min_value=1,
        key="delete",
    )

    if st.button("Delete Student"):

        status, msg = student.drop_student(int(roll))

        if status:
            st.success(msg)
        else:
            st.error(msg)