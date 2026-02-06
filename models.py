from typing import List
from flask_login import UserMixin
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from extensions import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False)
    task: Mapped[List["Task"]] = relationship('Task', back_populates='user')

class Task(db.Model):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(1000))
    date_created: Mapped[float] = mapped_column(Integer)
    date_completed: Mapped[float] = mapped_column(Integer, nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('user.id'))
    user: Mapped["User"] = relationship('User', uselist=False, back_populates='task')