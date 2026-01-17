from faker import Faker
import random
from .models import Department, Student, StudentID

fake = Faker()

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
