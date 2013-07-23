import sqlalchemy.types
import sqlalchemy.schema
from zope.interface import implements

from sqlalchemy.ext import declarative
from z3c.saconfig import named_scoped_session
from .interfaces import IMessage
Base = declarative.declarative_base()

Session = named_scoped_session("mydb")


class Message(Base):
    """Database-backed implementation of IMessage
    Cfr. Documentazione di SQLAlchemy
    """
    implements(IMessage)

    __tablename__ = 'message'

    message_id = sqlalchemy.schema.Column(
        sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement=True,
    )

    year = sqlalchemy.schema.Column(
        sqlalchemy.types.Integer(4),
        nullable=False,
    )

    title = sqlalchemy.schema.Column(
        sqlalchemy.types.Unicode(200),
        nullable=False,
    )
