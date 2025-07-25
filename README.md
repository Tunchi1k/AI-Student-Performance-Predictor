# AI-Powered Student Performance Predictor

A Streamlit web app that allows users to:

- Add new student academic records
- View all student records from a MySQL database
- Predict whether a student is likely to pass based on attendance, study hours, and previous scores

---

## Features

### Add Record
Enter details for a student including:
- Student ID
- Name
- Attendance rate (0.0 to 1.0)
- Weekly hours studied
- Previous score (%)
- Whether they passed the last exam

The data is saved to a MySQL database.

### View Records
Displays all student data from the database in a tabular format using pandas and Streamlit.

###  Predict Performance
Trains a **Random Forest Classifier** on existing data and predicts performance of a new student. Input:
- Attendance rate
- Study hours per week
- Previous score

Displays prediction as:
> "Likely to PASS"  
> "At Risk of FAILING"

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, scikit-learn
- **Database**: MySQL
- **Libraries**: 
  - `pandas`
  - `mysql-connector-python`
  - `scikit-learn`

---

## Setup Instructions

### 1. Prerequisites
Ensure the following are installed:
- Python ≥ 3.7
- MySQL Server
- MySQL Connector: `pip install mysql-connector-python`
- Other Python libs:  
  ```bash
  pip install streamlit pandas scikit-learn
### 2. Create MySQL Database
```bash
CREATE DATABASE students;
USE students;
CREATE TABLE students (
    student_id VARCHAR(50) PRIMARY KEY,
    name_ VARCHAR(100),
    attendance_rate FLOAT,
    hours_studied_per_week FLOAT,
    previous_score FLOAT,
    passed INT
 );
```
### 3. Run the App
```bash
streamlit run app.py
```


## File Structure
```bash
student-performance-app/
│
├── app.py           # Main Streamlit application
├── README.md        # Project documentation
```

## Author
Chintu Lungu

## Inspiration
This project helps test integration between Streamlit and MySQL while applying basic machine learning to real-world student data. Ideal for beginners wanting hands-on AI + DB experience.


    
    
