from faker import Faker
import random
from .models import Department, Student, StudentID,Subject, SubjectMarks

fake = Faker()


def create_subject_marks(n):
    try:
        student_obj=Student.objects.all()
        for student in student_obj:
            subjects=Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    student=student,
                    subject=subject,
                    marks=random.randint(0,100)

                )
    except Exception as e:
        print(f"Error creating subject marks: {e}")

def seed_db(n=10) -> None:
    departments = list(Department.objects.all())

    if not departments:
        print("No departments found. Please create departments first.")
        return

    for _ in range(n):
        department = random.choice(departments)

        student_id = f"STU-{random.randint(100, 999)}"
        student_name = fake.name()
        student_email = fake.unique.email()
        student_age = fake.random_int(min=18, max=30)
        student_address = fake.address()

        student_id_obj = StudentID.objects.create(
            student_id=student_id
        )

        Student.objects.create(
            department=department,
            student_id=student_id_obj,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address,
        )
