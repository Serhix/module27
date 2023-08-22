from sqlalchemy import and_

from src.db import session
from src.models import Student, Teacher, StadyGroup, StadySubject, Grade


def get_all(dict_arg: dict):
    match dict_arg.get('model'):
        case 'Student':
            select = session.query(Student).all()
            for s in select:
                print(f'id: {s.id}, group: {s.stady_group.group_name}, name: {s.full_name}')
        case 'Teacher':
            select = session.query(Teacher).all()
            for s in select:
                print(f'id: {s.id}, name: {s.full_name}, sciens title: {s.is_sciens_title}')
        case 'StadyGroup':
            select = session.query(StadyGroup).all()
        case 'StadySubject':
            select = session.query(StadySubject).all()
        case 'Grade':
            select = session.query(Grade).all()
    return select


def create_model(dict_arg: dict):
    match dict_arg.get('model'):
        case 'Student':
            model = Student(full_name=dict_arg.get('name'), stady_group_id=dict_arg.get('group_id'))
        case 'Teacher':
            model = Teacher(full_name=dict_arg.get('name'), is_sciens_title=dict_arg.get('scient_title'))
        case 'StadyGroup':
            model = StadyGroup(group_name=dict_arg.get('name'))
        case 'StadySubject':
            model = StadySubject(name=dict_arg.get('name'), teacher_id=dict_arg.get('teacher_id'))
        case 'Grade':
            model = Grade(stady_subject_id=dict_arg.get('subject_id') , student_id=dict_arg.get('student_id') , grade_val=dict_arg.get('grade_val') )
    if model: 
        session.add(model)
        session.commit()
        print('Create done!!!')
    else:
        session.rollback()
    session.close()


# def update_todo(_id, title, description, user):
#     todo = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id))
#     if todo:
#         todo.update({"title": title, 'description': description})
#         session.commit()
#     session.close()
#     return todo.first()


# def remove_todo(_id, user):
#     r = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id)).delete()
#     session.commit()
#     session.close()
#     return r
