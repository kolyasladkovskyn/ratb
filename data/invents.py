import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Invent(SqlAlchemyBase):
    __tablename__ = 'Inv'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    money = sqlalchemy.Column(sqlalchemy.BigInteger, nullable=True, default=0)
    inv = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')