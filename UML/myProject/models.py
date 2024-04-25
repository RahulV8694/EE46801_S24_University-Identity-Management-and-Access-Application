from django.db import models


class Instructor(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=32)
    dept_name = models.CharField(max_length=32)
    salary = models.IntegerField()

    class Meta:
        db_table = "instructor"


class Salary(models.Model):
    dept_name = models.CharField(max_length=255, primary_key=True)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    avg_salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "departmentsalarystats"


class Teaches(models.Model):
    # No changes needed here if you can't modify the schema
    course_id = models.CharField(max_length=20)
    sec_id = models.CharField(max_length=10)
    semester = models.CharField(max_length=20)
    year = models.IntegerField()
    teacher = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, related_name="teachings"
    )

    class Meta:
        db_table = "teaches"
        unique_together = ("course_id", "sec_id", "semester", "year")


class StudentCourse(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True)
    teaches = models.ForeignKey(Teaches, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    class Meta:
        db_table = "takes"

    def __str__(self):
        return f"{self.student_id} - {self.teaches}"


class ProfessorPublications(models.Model):
    publication_id = models.AutoField(primary_key=True)
    professor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publication_year = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "professor_publications"


class Course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    dept_name = models.CharField(max_length=32)
    credits = models.IntegerField()

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.title


class InstructorProxy(Instructor):
    class Meta:
        proxy = True
        verbose_name = "Instructor Report"
        verbose_name_plural = "Instructor Reports"
