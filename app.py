import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# 1. Read CSV
data = pd.read_csv("students.csv")

# 2. Calculate Average
data["Average"] = data[["Python", "Java", "DBMS"]].mean(axis=1)

# 3. Find Top Student
top_student = data.loc[data["Average"].idxmax(), "Name"]

# 4. Course Filter
st.sidebar.header("🔎 Filters")

courses = ["All"] + list(data["Course"].unique())

selected_course = st.sidebar.selectbox(
    "Select Course",
    courses
)

if selected_course != "All":
    filtered_data = data[data["Course"] == selected_course]
else:
    filtered_data = data

# 5. Dashboard Title
st.title("🎓 Student Performance Analytics Dashboard")
st.write("Analyze student attendance and academic performance.")

# 6. Dashboard Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "👨‍🎓 Total Students",
    len(filtered_data)
)

col2.metric(
    "📊 Average Marks",
    round(filtered_data["Average"].mean(), 2)
)

col3.metric(
    "🎯 Average Attendance",
    f"{filtered_data['Attendance'].mean():.2f}%"
)

filtered_top_student = filtered_data.loc[
    filtered_data["Average"].idxmax(),
    "Name"
]

col4.metric(
    "🏆 Top Student",
    filtered_top_student
)

# 7. Student Data Table
st.subheader("📋 Student Data")

st.dataframe(
    filtered_data,
    use_container_width=True
)

# 8. Subject-wise Average Marks
st.subheader("📊 Subject-wise Average Marks")

subject_average = filtered_data[["Python", "Java", "DBMS"]].mean()

fig, ax = plt.subplots()

subject_average.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Subjects")
ax.set_ylabel("Average Marks")
ax.set_title("Subject-wise Average Marks")

st.pyplot(fig)

# 9. Attendance vs Average Marks
st.subheader("📈 Attendance vs Average Marks")

fig2, ax2 = plt.subplots()

ax2.scatter(
    filtered_data["Attendance"],
    filtered_data["Average"]
)

ax2.set_xlabel("Attendance (%)")
ax2.set_ylabel("Average Marks")
ax2.set_title("Attendance vs Student Performance")

st.pyplot(fig2)

# 10. Top 5 Performing Students
st.subheader("🏆 Top 5 Performing Students")

top_students = filtered_data.sort_values(
    "Average",
    ascending=False
)

st.dataframe(
    top_students[["Name", "Attendance", "Average"]].head(5),
    use_container_width=True
)