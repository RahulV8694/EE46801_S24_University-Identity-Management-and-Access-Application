# University-Identity-Management-and-Access-Application
University Identity Management and Access Application 

--------------------------
Overview
The University Course Management System is a prototype developed to meet the requirements of the course EE468/EE568/CS560: Database Systems. This system is designed to facilitate the management of university courses and user interactions across three primary user types: Admin, Professors, and Students.

System/Tools Requirements
MySQL: Version 8.0.28
Django: Version 4.2.11
Python: Version 3.10.4
IDE: Visual Studio Code
Accessing the System
The system can be accessed using a web browser at 127.0.0.1:8000, which is the address of the index page. The application is compatible with all major browsers.

Features
Admin Module
Create a list of professors: Sorted by name, department, or salary.
Generate a salary report: Displays minimum, maximum, and average salaries by department.
Report on professor and student associations: Lists professors alongside the total number of students they taught in a given semester.
Professor Module
Course section management: Lists course sections and the enrollment numbers for each section taught by the professor in a specified semester.
Student enrollment details: Provides a list of students enrolled in a particular course section during a given semester.
Student Module
Course section query: Allows students to search for course sections offered by department in a specified semester and year.
User Instructions
Admin Instructions
Navigate to the admin section: Use the Admin login on the index page.
Professor list: Choose sorting criteria (name, department, salary) to view and sort the list of professors.
Salary report: Select a department to view detailed salary statistics.
Professor and student report: Enter the professor's name, year, and semester to generate a report on their teaching engagements.
Professor Instructions
Login: Use the Professor ID and password to access.
View course sections: Enter the semester and year to retrieve course sections taught.
View enrolled students: Enter the course section ID, semester, and year to see the list of enrolled students.
Student Instructions
Login: Enter Student ID and password.
Query course sections: Fill in the department, year, and semester to search for available courses.
Logout: Use the logout button to exit the system safely.
Development Team
Rahul Vijaykumar
Satya Sai Deepak Velagapudi
Yu Liu
Supervised By
Professor Daqing Hou
Clarkson University
