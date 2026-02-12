# Face Recognition Based Attendance System

![Python](https://img.shields.io/badge/Python-3.10-blue) ![OpenCV](https://img.shields.io/badge/OpenCV-4.7-green) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

Attendance is a crucial part of classroom evaluation. Traditional methods, such as manual roll calls, are prone to errors—teachers may miss students, or students may mark attendance multiple times.  

The **Face Recognition Based Attendance System** automates attendance tracking using **computer vision** to identify students based on their facial features. This ensures **accurate, reliable, and efficient** attendance management in educational institutions. 
The project is part of the broader field of **Human-Computer Interaction (HCI)**, which focuses on enhancing the interaction between humans and computer systems.

---

## Features

-  Automatic recognition of students using facial features  
-  Secure and authentic attendance record keeping  
-  Course-specific attendance logging  
-  Real-time attendance updates  
-  Scalable for large classrooms  

---

## System Workflow

The system operates in **four main phases**:

1. **Database Creation**  
   - Capture and store images of all students.  
   - Each student has a unique record associated with their facial data.  

2. **Face Detection**  
   - Detect faces in real-time using computer vision algorithms.  
   - Ensures only valid and clear faces are considered.  

3. **Face Recognition**  
   - Matches detected faces against the database to identify students.  
   - Uses unique facial features for accurate verification.  

4. **Attendance Updating**  
   - Automatically marks attendance for recognized students.  
   - Maintains a secure, course-specific, and tamper-proof attendance log.  

---

## System Architecture

```mermaid
flowchart LR
    A[Student Images] --> B[Database Creation]
    B --> C[Face Detection]
    C --> D[Face Recognition]
    D --> E[Attendance Updating]
    E --> F[Attendance Log & Reports]
