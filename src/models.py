from sqlalchemy import Column, Integer, String, func, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    stady_group_id = Column(
        ForeignKey("stady_groups.id", ondelete="SET NULL", onupdate="CASCADE"),
        nullable=False,
    )
    create_at = Column(DateTime, default=func.now())

    stady_group = relationship("StadyGroup", back_populates="student")
    grade = relationship("Grade", backref="student")


class StadyGroup(Base):
    __tablename__ = "stady_groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(50), nullable=False)

    student = relationship("Student", back_populates="stady_group")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    is_sciens_title = Column(Boolean, nullable=True)
    create_at = Column(DateTime, default=func.now())

    stady_subject = relationship("StadySubject", back_populates="teacher")


class StadySubject(Base):
    __tablename__ = "stady_subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    teacher_id = Column(
        ForeignKey("teachers.id", ondelete="SET NULL", onupdate="CASCADE"),
        nullable=True,
    )
    create_at = Column(DateTime, default=func.now())

    teacher = relationship("Teacher", back_populates="stady_subject")
    grade = relationship("Grade", backref="stady_subject")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    stady_subject_id = Column(
        "stady_subject_id", ForeignKey("stady_subjects.id", ondelete="CASCADE")
    )
    student_id = Column("student_id", ForeignKey("students.id", ondelete="CASCADE"))
    grade_val = Column(Integer, nullable=False)
    create_at = Column(DateTime, default=func.now())
