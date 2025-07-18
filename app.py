import streamlit as st
import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chintu@2003",
        database="students"
    )
#Page Title
st.title("AI-Powered Student Performance Predictor")


#Tabs
tab1, tab2, tab3 = st.tabs(["Add Record", "View Records", "Predict Performance"])


with tab1:
    st.header("Add a New Student Record")
     
    student_id = st.text_input("Student ID")
    name = st.text_input("Student Name")
    attendance = st.slider("Attendance Rate", 0.0, 1.0, 0.85)
    hours = st.number_input("Hours Studied Per Week", 0.0, 50.0, 10.0, key="hours_input")
    score = st.number_input("Previous Score (%)", 0.0, 100.0, 70.0, key="score_input")
    passed = st.selectbox("Passed Last Exam?", ["Yes", "No"])
    passed_val = 1 if passed == "Yes" else 0

    if st.button("Save Record"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO students (student_id,name_, attendance_rate, hours_studied_per_week, previous_score, passed)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (student_id, name, attendance, hours, score, passed_val))
            conn.commit()
            st.success(f"{name}'s record saved successfully.")
            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"Failed to insert record: {e}")



# TAB 2: View All Records
with tab2:
    st.header("All Student Records")
    try:
        conn = get_connection()
        df = pd.read_sql("SELECT * FROM students", conn)
        st.dataframe(df)
        conn.close()
    except Exception as e:
        st.error(f"Could not fetch data: {e}")


# TAB 3: Predict with Model

with tab3:
    st.header("Predict Student Performance")

    try:
        conn = get_connection()
        df = pd.read_sql("SELECT * FROM students", conn)
        conn.close()

        if len(df) < 5:
            st.warning("Not enough data to train a reliable model. Add more records.")
        else:
            # Prepare data
            X = df[['attendance_rate', 'hours_studied_per_week', 'previous_score']]
            y = df['passed']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

            # Train model
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            accuracy = model.score(X_test, y_test)

            st.success(f"Model trained with {round(accuracy*100, 2)}% accuracy.")

            # Input for prediction
            st.subheader("Predict a New Student")
            a = st.slider("Attendance Rate (0.0 - 1.0)", 0.0, 1.0, 0.8)
            h = st.number_input("Hours Studied Per Week", 0.0, 50.0, 10.0, key="predict_hours_input")
            s = st.number_input("Previous Score (%)", 0.0, 100.0, 70.0, key="predict_score_input")

            if st.button("Predict Outcome"):
                prediction = model.predict([[a, h, s]])[0]
                result = "Likely to PASS" if prediction == 1 else "At Risk of FAILING"
                st.info(f"Prediction: {result}")

    except Exception as e:
        st.error(f"Error: {e}")

