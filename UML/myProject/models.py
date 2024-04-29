from django.db import models


class Instructor(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=32)
    dept_name = models.CharField(max_length=32)
    salary = models.IntegerField()

    class Meta:
        db_table = "instructor"


from django.db.models import Avg, Max, Min


class Salary(Instructor):
    class Meta:
        proxy = True

    @classmethod
    def avg_salary(cls):
        return cls.objects.aggregate(Avg("salary"))["salary__avg"]

    @classmethod
    def max_salary(cls):
        return cls.objects.aggregate(Max("salary"))["salary__max"]

    @classmethod
    def min_salary(cls):
        return cls.objects.aggregate(Min("salary"))["salary__min"]


class Teaches(models.Model):
    course_id = models.CharField(max_length=20)
    sec_id = models.CharField(max_length=10)
    semester = models.CharField(max_length=20)
    year = models.IntegerField()
    teacher = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        db_column="teacher_id",
        related_name="teachings",
    )

    class Meta:
        db_table = "teaches"

    def __str__(self):
        return f"{self.course_id} Section: {self.sec_id}, {self.semester} {self.year}"


class InstructorProxy(Instructor):
    class Meta:
        proxy = True
        verbose_name = "Instructor Report"
        verbose_name_plural = "Instructor Reports"
