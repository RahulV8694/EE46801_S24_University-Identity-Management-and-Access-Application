from django.http import JsonResponse
from django.db.models import Avg, Max, Min, Sum
from django.shortcuts import render,redirect
from .models import Teaches, Takes, Instructor, Student
from django.db import connection
import json

def uni_home(request):
    return render(request, 'university_home.html')

def professor(request):
    if request.method == 'POST':
        if 'professor_id' in request.POST:  # First form for entering Professor ID
            professor_id = request.POST.get('professor_id')

            # Check if the professor ID exists in the database
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Instructor WHERE id = %s", [professor_id])
                professor_exists = cursor.fetchone()

            if professor_exists:
                return redirect('professor_valid', professor_id=professor_id)
            else:
                return render(request, 'professor_form.html', {'invalid_id': True})
    else:
        return render(request, 'professor_form.html')
    
def professor_valid(request, professor_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'f4':
            # Fetch semester and year from the form
            semester = request.POST.get('semester')
            year = request.POST.get('year')
            print("HI")
            print(semester,year)
            # Fetch course sections and students enrolled for the professor in the chosen semester and year
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT t.course_id, t.sec_id, t.semester, t.year, COUNT(tk.student_id) AS num_students
                    FROM Teaches t
                    JOIN Takes tk ON t.sec_id = tk.sec_id AND t.semester = tk.semester AND t.year = tk.year
                    WHERE t.teacher_id = %s AND t.semester = %s AND t.year = %s
                    GROUP BY t.sec_id, t.semester, t.year;
                """, [professor_id, semester, year])
                course_sections_and_students = cursor.fetchall()
            print(course_sections_and_students)
            return render(request, 'course_sections_and_students.html', {'course_sections_and_students': course_sections_and_students})

        elif action == 'f5':
            # Fetch students enrolled in the chosen course section
            section_id = request.POST.get('section_id')
            semester = request.POST.get('semester')
            year = request.POST.get('year')

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT tk.student_id, s.name, s.dept_name
                    FROM Takes tk
                    JOIN Student s ON tk.student_id = s.student_id
                    JOIN Teaches t ON t.sec_id = tk.sec_id and t.semester = tk.semester and t.year = tk.year and t.course_id = tk.course_id
                    WHERE t.teacher_id = %s AND t.sec_id = %s AND t.semester = %s AND t.year = %s
                """, [professor_id, section_id, semester, year])
                students_enrolled = cursor.fetchall()
            
            return render(request, 'students_enrolled.html', {'students_enrolled': students_enrolled})

    else:
        # Render the form template
        return render(request, 'professor_form_valid.html', {'professor_id': professor_id})

def student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        # Check if the student ID exists in the database
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Student WHERE student_id = %s", [student_id])
            student_exists = cursor.fetchone()

        if student_exists:
            return redirect('department_semester_form')
        else:
            return render(request, 'student_form.html', {'invalid_student_id': True})
    else:
        return render(request, 'student_form.html', {'invalid_student_id': False})
def department_semester_form(request):
    if request.method == 'POST':
        department=request.POST.get('department')
        semester=request.POST.get('semester')
        year=request.POST.get('year')
        print(department,year,semester)
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT c.title,t.course_id, t.sec_id
                FROM teaches as t
                INNER JOIN Course as c
                ON t.course_id=c.course_id
                WHERE c.dept_name = %s AND t.year = %s AND t.semester = %s;
            """, [department, year, semester])   
            course_sections = cursor.fetchall()
        print(course_sections)
        return render(request, 'course_sections_query.html', {'course_sections': course_sections})
    else:
        return render(request, 'departmen_semester_form.html')
        




def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')
