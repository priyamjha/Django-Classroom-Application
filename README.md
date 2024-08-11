# Classroom Management System

## Introduction

The Classroom Management System is a full-stack web application designed to streamline the management of school classrooms. This application allows the principal to create classrooms, assign teachers and students, and manage their details. Teachers can manage their classrooms and create timetables, while students can view their classroom details and timetable. The application is built using Django for the backend and utilizes Bootstrap for the frontend.

## Technology Used

- **Backend:** Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap, JavaScript

## Features Implemented

### User Roles

1. **Principal**
   - Can create classrooms and assign teachers to those classrooms.
   - Can assign students to teachers.
   - Can view and manage the list of teachers and students.
   - Can edit or delete teacher and student details.
   - Can create accounts for teachers and students.

2. **Teacher**
   - Can view the list of students in their assigned classroom.
   - Can edit or delete student details.

3. **Student**
   - Can view the list of other students in their classroom.

### Classroom Management

- Principal can create classrooms with specified name, start time, end time, and days of the week the classroom is in session.
- Principal can assign a classroom to a teacher.

### Authentication

- Predefined principal account:
  - Email: `principal@classroom.com`
  - Password: `Admin`
- Principal can create teacher and student accounts with email and password.

## What It Does

- **Principal Dashboard:**
  - View list of teachers and students in a tabular format.
  - Edit or delete teacher and student details.
  - Create classrooms with specified details.
  - Assign a classroom to a teacher.

- **Teacher Dashboard:**
  - View list of students in their assigned classroom.
  - Edit or delete student details.

- **Student Dashboard:**
  - View list of other students in their classroom.

## Accessing the Application

To access the application, use the predefined principal account:

- **Email:** principal@classroom.com
- **Password:** Admin

Once logged in, the principal can create teacher and student accounts, set up classrooms, and assign teachers to classrooms. Teachers and students can log in using the credentials created by the principal.

---
