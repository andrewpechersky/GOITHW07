from sqlalchemy import func
#from pprint import pprint as print
from models import Student, Grade, Subject, Group, Teacher, session


# Запит №1: Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    result = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return result


# Запит №2: Знайти студента із найвищим середнім балом з певного предмета
def select_2(subject_name):
    query = session.query(Student, func.avg(Grade.grade).label('avg_grade')) \
        .join(Grade) \
        .join(Subject) \
        .filter(Subject.subject == subject_name) \
        .group_by(Student.id) \
        .order_by(func.avg(Grade.grade).desc()) \
        .first()
    student_name, average_grade = query[0].name, round(query[1], 2)
    return f'Highest average grade > {subject_name}: {student_name} | {average_grade}'


# Запит №3: Знайти середній бал у групах з певного предмета
def select_3(subject_name):
    average_grade_per_group = session.query(Group.group_name, func.avg(Grade.grade).label('avg_grade')) \
        .join(Grade) \
        .join(Subject) \
        .filter(Subject.subject == subject_name) \
        .group_by(Group.id) \
        .all()
    return f"{subject_name} > {average_grade_per_group,}"


# Запит №4: Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4():
    query = session.query(func.avg(Grade.grade).label('average_grade')).scalar()
    return f'Avg grade for all > : {round(query, 3)}'


# Запит №5: Знайти які курси читає певний викладач
def select_5(teacher_id):
    query = session.query(Subject.subject) \
        .filter(Subject.teacher_id == teacher_id) \
        .distinct() \
        .all()
    return [course.subject for course in query]


# Запит №6: Знайти список студентів у певній групі
def select_6(group_name):
    students_in_group = session.query(Student) \
        .join(Group) \
        .filter(Group.group_name == group_name) \
        .all()
    return [student.name for student in students_in_group]


# Запит №7: Знайти оцінки студентів у окремій групі з певного предмета
def select_7(group_name, subject_name):
    grades_in_group_and_subject = session.query(Student.name, Grade.grade) \
        .join(Grade) \
        .join(Subject) \
        .filter(Group.group_name == group_name, Subject.subject == subject_name) \
        .all()
    return grades_in_group_and_subject


# Запит №8: Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(teacher_id):
    average_grade_by_teacher = session.query(func.avg(Grade.grade)) \
        .join(Subject) \
        .join(Teacher) \
        .filter(Teacher.id == teacher_id) \
        .scalar()
    return average_grade_by_teacher


# Запит №9: Знайти список курсів, які відвідує певний студент
def select_9(student_name):
    courses_attended_by_student = session.query(Subject.subject) \
        .join(Grade) \
        .join(Student) \
        .filter(Student.name == student_name) \
        .distinct() \
        .all()
    return courses_attended_by_student


# Запит №10: Список курсів, які певному студенту читає певний викладач
def select_10(student_name, teacher_name):
    result = session.query(Subject.subject) \
        .join(Teacher) \
        .join(Grade) \
        .join(Student) \
        .filter(Teacher.name == teacher_name, Student.name == student_name) \
        .distinct() \
        .all()
    return result


if __name__ == "__main__":

    print("Result 1:", select_1())
    print("Result 2:", select_2("Math"))
    print("Result 3:", select_3("Math"))
    print("Result 4:", select_4())
    print("Result 5:", select_5(1))
    print("Result 6:", select_6("Group 1"))
    print("Result 7:", select_7("Group 1", "Math"))
    print("Result 8:", select_8(1))
    print("Result 9:", select_9("Lori Mcclure"))
    print("Result 10:", select_10("Lori Mcclure", "Brandon Collins"))
