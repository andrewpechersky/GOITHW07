from faker import Faker
from random import randint
from datetime import datetime, timedelta

from models import Student, Group, Teacher, Subject, Grade, session


fake = Faker()


def create_students():
    for _ in range(30):
        student = Student(name=fake.name(), group_id=randint(1, 3))
        session.add(student)


def create_groups():
    for group_name in ['Group 1', 'Group 2', 'Group 3']:
        group = Group(group_name=group_name)
        session.add(group)


def create_teachers():
    for _ in range(3):
        teacher = Teacher(name=fake.name())
        session.add(teacher)


def create_subjects():
    subjects = ['Math', 'English', 'Science', 'History', 'Art']
    for subject_name in subjects:
        teacher_id = randint(1, 3)
        subject = Subject(subject=subject_name, teacher_id=teacher_id)
        session.add(subject)


def create_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    # For all students
    for student in students:
        # For all subjects
        for subject in subjects:
            grade = randint(60, 100)
            date_received = datetime.now() - timedelta(days=randint(1, 365))

            new_grade = Grade(student_id=student.id,
                              subject_id=subject.id,
                              grade=grade,
                              date=date_received,
                              group_id=randint(1, 3))
            session.add(new_grade)


create_groups()
create_teachers()
create_subjects()
create_students()
create_grades()


session.commit()