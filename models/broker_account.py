from uuid import uuid4

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.base import Base


class BrokerAccount(Base):

    __tablename__ = "broker_accounts"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))

    broker_name: Mapped[str] = mapped_column(String(50))

    broker_user_id: Mapped[str] = mapped_column(String(100))

    access_token: Mapped[str] = mapped_column(String(1000))

    refresh_token: Mapped[str] = mapped_column(String(1000))

    status: Mapped[str] = mapped_column(String(20))

    user = relationship("User", back_populates="broker_accounts")
