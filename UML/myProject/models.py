from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=32, primary_key=True)
    
class Instructor(models.Model):
    teacher_id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=32)
    dept_name = models.CharField(max_length=32)
    salary = models.IntegerField()

class Teaches(models.Model):
    course_id = models.CharField(max_length=10)
    sec_id = models.CharField(max_length=5)
    semester = models.CharField(max_length=10)
    year = models.IntegerField()
    teacher_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)

class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=32)
    dept_name = models.CharField(max_length=32)
    total_credits = models.IntegerField()

class Takes(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.CharField(max_length=10)
    sec_id = models.CharField(max_length=5)
    semester = models.CharField(max_length=10)
    year = models.IntegerField()
    grade = models.CharField(max_length=2)
