from src.db import session
from src.models import Student, Teacher, StadyGroup, StadySubject, Grade


def get_all(dict_arg: dict):
    match dict_arg.get("model"):
        case "Student":
            select = session.query(Student).all()
            for s in select:
                print(
                    f"id: {s.id}, group: {s.stady_group.group_name}, name: {s.full_name}"
                )
        case "Teacher":
            select = session.query(Teacher).all()
            for s in select:
                print(
                    f"id: {s.id}, name: {s.full_name}, sciens title: {s.is_sciens_title}"
                )
        case "StadyGroup":
            select = session.query(StadyGroup).all()
            for s in select:
                print(f"id: {s.id}, name: {s.group_name}")
        case "StadySubject":
            select = session.query(StadySubject).all()
            for s in select:
                print(f"id: {s.id}, name: {s.name}, teacher: {s.teacher.full_name}")
        case "Grade":
            select = session.query(Grade).all()
            for s in select:
                print(
                    f"id: {s.id}, student: {s.student.full_name}, subject: {s.stady_subject.name}, {s.grade_val}"
                )


def create_model(dict_arg: dict):
    match dict_arg.get("model"):
        case "Student":
            model = Student(
                full_name=dict_arg.get("name"), stady_group_id=dict_arg.get("group_id")
            )
        case "Teacher":
            model = Teacher(
                full_name=dict_arg.get("name"),
                is_sciens_title=dict_arg.get("scient_title"),
            )
        case "StadyGroup":
            model = StadyGroup(group_name=dict_arg.get("name"))
        case "StadySubject":
            model = StadySubject(
                name=dict_arg.get("name"), teacher_id=dict_arg.get("teacher_id")
            )
        case "Grade":
            model = Grade(
                stady_subject_id=dict_arg.get("subject_id"),
                student_id=dict_arg.get("student_id"),
                grade_val=dict_arg.get("grade_val"),
            )
    if model:
        session.add(model)
        session.commit()
        print("Create done!!!")
    else:
        session.rollback()
    session.close()


def update_model(dict_arg: dict):
    match dict_arg.get("model"):
        case "Student":
            model = session.query(Student).filter(Student.id == dict_arg.get("id"))
            if model:
                model.update(
                    {
                        "full_name": dict_arg.get("name"),
                        "stady_group_id": dict_arg.get("group_id"),
                    }
                )
                session.commit()
        case "Teacher":
            model = session.query(Teacher).filter(Teacher.id == dict_arg.get("id"))
            if model:
                model.update(
                    {
                        "full_name": dict_arg.get("name"),
                        "is_sciens_title": dict_arg.get("scient_title"),
                    }
                )
                session.commit()
        case "StadyGroup":
            model = session.query(StadyGroup).filter(
                StadyGroup.id == dict_arg.get("id")
            )
            if model:
                model.update({"group_name": dict_arg.get("name")})
                session.commit()
        case "StadySubject":
            model = session.query(StadySubject).filter(
                StadySubject.id == dict_arg.get("id")
            )
            if model:
                model.update(
                    {
                        "name": dict_arg.get("name"),
                        "teacher_id": dict_arg.get("teacher_id"),
                    }
                )
                session.commit()
        case "Grade":
            model = session.query(Grade).filter(Grade.id == dict_arg.get("id"))
            if model:
                model.update(
                    {
                        "stady_subject_id": dict_arg.get("subject_id"),
                        "student_id": dict_arg.get("student_id"),
                        "grade_val": dict_arg.get("grade_val"),
                    }
                )
                session.commit()
    session.close()
    print("Update done!!!")



def remove_model(dict_arg: dict):
    match dict_arg.get("model"):
        case "Student":
            model = session.query(Student).filter(Student.id == dict_arg.get("id"))
        case "Teacher":
            model = session.query(Teacher).filter(Teacher.id == dict_arg.get("id"))
        case "StadyGroup":
            model = session.query(StadyGroup).filter(StadyGroup.id == dict_arg.get("id"))
        case "StadySubject":
            model = session.query(StadySubject).filter(StadySubject.id == dict_arg.get("id"))
        case "Grade":
            model = session.query(Grade).filter(Grade.id == dict_arg.get("id"))
    if model:
        model.delete()
        session.commit()
        print("Remove Done!!!")
    session.close()
