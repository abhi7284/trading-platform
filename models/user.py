from uuid import uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.base import Base



class User(Base):

    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    name: Mapped[str]

    email: Mapped[str] = mapped_column(
        String,
        unique=True
    )

    password_hash: Mapped[str]

    broker_accounts = relationship(
        "BrokerAccount",
        back_populates="user"
    )