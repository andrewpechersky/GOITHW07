from datetime import date
from sqlalchemy import create_engine, Integer, String, Date, ForeignKey

from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column

engine = create_engine('sqlite:///mydatabase.db')

DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'), unique=False)


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_name: Mapped[str] = mapped_column(String(50), unique=True)


class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=False)


class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(50))
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'))


class Grade(Base):
    __tablename__ = 'grades'
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'),
                                            primary_key=True,
                                            unique=False)

    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'),
                                          unique=False)

    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.id'),
                                            primary_key=True,
                                            unique=False)

    grade: Mapped[int] = mapped_column(Integer,
                                       unique=False)

    date: Mapped[date] = mapped_column(Date,
                                       primary_key=True,
                                       unique=False)


#Base.metadata.create_all(engine)
# Base.metadata.bind = engine
#
# session.commit()
