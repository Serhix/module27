from datetime import datetime
from faker import Faker
import faker
from random import randint, choice

from src.db import session
from src.models import Student, StadyGroup, StadySubject, Teacher, Grade

MAX_STUDENTS = 50
MAX_GROUPS = 3
MAX_TEACHERS = 5
MAX_SUBJECTS = 8
MAX_EVALUTIONS = 20


def generate_fake_data(max_students, max_groups, max_teachers, max_subjects):
    fake_students = []
    fake_groups = []
    fake_teachers = []
    fake_subjects = []

    fake_data = faker.Faker("uk_UA")

    for _ in range(max_students - randint(0, 20)):
        fake_students.append(fake_data.name())

    for _ in range(max_groups):
        fake_groups.append(f"{choice('ABCDEF')}-{randint(1000,9999)}")

    for _ in range(max_teachers - randint(0, 2)):
        fake_teachers.append(fake_data.name())

    for _ in range(max_subjects - randint(0, 3)):
        fake_subjects.append(fake_data.catch_phrase())

    return fake_students, fake_groups, fake_teachers, fake_subjects


def get_stady_date():
    """
    Визначаємо будні дні в період 01.01.2023 31.05.2023
    """
    date = []
    for month in range(1, 6):
        for day in range(1, 32):
            try:
                grade_date = datetime(2023, month, day).date()
            except:
                pass
            finally:
                if grade_date and grade_date.strftime("%a") not in ["Sat", "Sun"]:
                    date.append(grade_date)
    return date


def create_data(fake_students, fake_groups, fake_teachers, fake_subjects):
    for student_name in fake_students:
        student = Student(
            full_name=student_name, stady_group_id=randint(1, len(fake_groups))
        )
        session.add(student)

    for group in fake_groups:
        stady_group = StadyGroup(group_name=group)
        session.add(stady_group)

    for teacher_name in fake_teachers:
        teacher = Teacher(full_name=teacher_name, is_sciens_title=randint(0, 1))
        session.add(teacher)

    for subject_name in fake_subjects:
        stady_subject = StadySubject(
            name=subject_name, teacher_id=randint(1, len(fake_teachers))
        )
        session.add(stady_subject)

    for stady_date in get_stady_date():
        # визначимо перелік предметів на день, вважатимемо що в день 3-4 заняття
        lessons = []
        for lesson in range(choice(range(3, 5))):
            lessons.append(randint(1, len(fake_subjects)))
        """
        максимальна кількість необхідних оцінок len(students)*len(subjects)*20
        максимальна кількість необхідних оцінок в день (len(students)*len(subjects)*20)/len(get_stady_date())
        максимальна кількість необхідних оцінок за занняття ((len(students)*len(subjects)*20)/len(get_stady_date()))/len(lessons)
        """
        max_grade_pet_lessons = (
            (len(fake_students) * len(fake_subjects) * 20) / len(get_stady_date())
        ) / len(lessons)
        for lesson in lessons:
            for _ in range(int(max_grade_pet_lessons)):
                grade = Grade(
                    stady_subject_id=lesson,
                    student_id=randint(1, len(fake_students)),
                    grade_val=randint(1, 100),
                    create_at=stady_date,
                )
                session.add(grade)
    session.commit()


if __name__ == "__main__":
    create_data(
        *generate_fake_data(MAX_STUDENTS, MAX_GROUPS, MAX_TEACHERS, MAX_SUBJECTS)
    )
