import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError
from src_cli.repositiry import create_model, get_all


parser = argparse.ArgumentParser(description='CLI for CRUD')
parser.add_argument('--action', '-a', help='Comand: create, update, list, remove')
parser.add_argument('--model', '-m', help='Choise model for action')
parser.add_argument('--id')
parser.add_argument('--name', '-n', help='name student, teacher, group, subject')
parser.add_argument('--group_id')
parser.add_argument('--scient_title', action='store_true', help="Scientific title true")
parser.add_argument('--teacher_id')
parser.add_argument('--subject_id')
parser.add_argument('--student_id')
parser.add_argument('--grade_val')

arguments = parser.parse_args()
my_args = vars(arguments)
action = my_args.get('action')


def main():
    match action:
        case 'create':
            create_model(my_args)
        case 'list':
            get_all(my_args)
        # case 'update':
        #     # t = update_todo(_id=_id, title=title, description=description, user=user)
        #     if t:
        #         print(t.id, t.title, t.description, t.user.login)
        #     else:
        #         print('Not found!!!')
        # case 'remove':
        #     r = remove_todo(_id=_id, user=user)
        #     print(f'Remove {r}')
        case _:
            print('Wrong comand!!!')



if __name__ == '__main__':
    main()

