from sqlalchemy import func, desc, and_
from sqlalchemy.orm import joinedload
from src.db import session
from src.models import Grade, StadySubject, StadyGroup, Student, Teacher


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    """
    select = (
        session.query(
            Student.full_name,
            func.round(func.avg(Grade.grade_val), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    for s in select:
        print(s)


def select_2(id_subj: int):
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    """
    select = (
        session.query(
            Student.full_name,
            func.round(func.avg(Grade.grade_val), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .where(Grade.stady_subject_id == id_subj)
        .order_by(desc("avg_grade"))
        .group_by(Student.id)
        .limit(1)
        .all()
    )
    for s in select:
        print(s)


def select_3(id_sabj: int):
    """
    Знайти середній бал у групах з певного предмета.
    """
    select = (
        session.query(
            StadySubject.name,
            StadyGroup.group_name,
            func.round(func.avg(Grade.grade_val), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(StadySubject)
        .join(Student)
        .join(StadyGroup)
        .filter(StadySubject.id == id_sabj)
        .order_by(desc("avg_grade"))
        .group_by(StadyGroup.group_name)
        .group_by(StadySubject.name)
        .all()
    )
    for s in select:
        print(s)


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).
    """
    select = (
        session.query("avg grade: " + func.round(func.avg(Grade.grade_val), 2))
        .select_from(Grade)
        .scalar()
    )
    print(select)


def select_5(id_teacher: int):
    """
    Знайти, які курси читає певний викладач.
    """
    select = (
        session.query("Subject: " + StadySubject.name, "Teacher: " + Teacher.full_name)
        .select_from(StadySubject)
        .join(Teacher)
        .filter(Teacher.id == id_teacher)
        .all()
    )
    for s in select:
        print(s)


def select_6(id_group: int):
    """
    Знайти список студентів у певній групі.
    """
    select = (
        session.query(
            "Group: " + StadyGroup.group_name, "Student: " + Student.full_name
        )
        .select_from(Student)
        .join(StadyGroup)
        .filter(StadyGroup.id == id_group)
        .all()
    )
    for s in select:
        print(s)


def select_7(id_group: int, id_subj: int):
    """
    Знайти оцінки студентів в окремій групі з певного предмета.
    """
    select = (
        session.query(
            Student.full_name, StadyGroup.group_name, StadySubject.name, Grade.grade_val
        )
        .select_from(Grade)
        .join(Student)
        .join(StadyGroup)
        .join(StadySubject)
        .filter(Grade.stady_subject_id == id_subj, StadyGroup.id == id_group)
        .order_by(Student.id)
        .all()
    )
    for s in select:
        print(s)


def select_8(id_teacher: int):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.(з кожного окремо)
    """
    select = (
        session.query(Teacher.full_name, StadySubject.name, func.avg(Grade.grade_val))
        .select_from(Grade)
        .join(StadySubject)
        .join(Teacher)
        .filter(Teacher.id == id_teacher)
        .group_by(Teacher.id, StadySubject.id)
        .all()
    )
    print("Average score for each subject separately")
    for s in select:
        print(s)
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.(зі всіх предметів)
    """
    select = (
        session.query(Teacher.full_name, func.avg(Grade.grade_val))
        .select_from(Grade)
        .join(StadySubject)
        .join(Teacher)
        .filter(Teacher.id == id_teacher)
        .group_by(Teacher.id)
        .all()
    )
    print("Average score in all subjects")
    for s in select:
        print(s)


def select_9(id_student: int):
    """
    Знайти список курсів, які відвідує певний студент.
    """
    select = (
        session.query(
            "Student: " + Student.full_name, "Stady Subject: " + StadySubject.name
        )
        .select_from(Grade)
        .join(Student)
        .join(StadySubject)
        .filter(Student.id == id_student)
        .group_by(StadySubject.id, Student.id)
        .all()
    )
    for s in select:
        print(s)


def select_10(id_student: int, id_teacher: int):
    """
    Список курсів, які певному студенту читає певний викладач.
    """
    select = (
        session.query(
            "Student: " + Student.full_name,
            "Teacher: " + Teacher.full_name,
            "Stady Subject: " + StadySubject.name,
        )
        .select_from(Grade)
        .join(StadySubject)
        .join(Teacher)
        .join(Student)
        .filter(Student.id == id_student, Teacher.id == id_teacher)
        .group_by(StadySubject.id, Teacher.id, Student.id)
        .all()
    )
    for s in select:
        print(s)


def select_11(id_teacher: int, id_student: int):
    """
    Середній бал, який певний викладач ставить певному студентові.
    """
    select = (
        session.query(
            "Teacher: " + Teacher.full_name,
            "Student: " + Student.full_name,
            func.avg(Grade.grade_val),
        )
        .select_from(Grade)
        .join(StadySubject)
        .join(Teacher)
        .join(Student)
        .filter(Student.id == id_student, Teacher.id == id_teacher)
        .group_by(Teacher.id, Student.id)
        .all()
    )
    for s in select:
        print(s)


def select_12(id_group: int, id_subj: int):
    """
    Оцінки студентів у певній групі з певного предмета на останньому занятті.
    """
    last_lesson = (
        session.query(func.max(Grade.create_at))
        .select_from(Grade)
        .join(StadySubject)
        .join(Student)
        .join(StadyGroup)
        .filter(StadyGroup.id == id_group, StadySubject.id == id_subj)
        .scalar()
    )
    select = (
        session.query(
            Grade.grade_val, StadyGroup.group_name, StadySubject.name, Grade.create_at
        )
        .select_from(Grade)
        .join(StadySubject)
        .join(Student)
        .join(StadyGroup)
        .filter(
            StadyGroup.id == id_group,
            StadySubject.id == id_subj,
            Grade.create_at == last_lesson,
        )
        .all()
    )
    for s in select:
        print(s)


if __name__ == "__main__":
    select_1()
    select_2(7)
    select_3(4)
    select_4()
    select_5(1)
    select_6(3)
    select_7(3, 3)
    select_8(3)
    select_9(14)
    select_10(14, 3)
    select_11(3, 14)
    select_12(3, 3)
