#database
from src.core.db import Base,Engine
#sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema":"librery_system"}

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column()
    hash_password: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    #relationship
    favorite_book: Mapped[list["Favorite"]] = relationship(back_populates="user")

class Favorite(Base):
    __tablename__ = "favorite"
    __table_args__ = {"schema":"librery_system"}

    user_id: Mapped[int] = mapped_column(ForeignKey("librery_system.user.id"),primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("librery_system.book.id"),primary_key=True)

class Book(Base):
    __tablename__ = "book"
    __table_args__ = {"schema":"librery_system"}

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column()
    subtitle: Mapped[str] = mapped_column()
    author: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    pdf_url: Mapped[str] = mapped_column()
    number_page: Mapped[int] = mapped_column()
    created_at: Mapped[str] = mapped_column()
    book_cover_image_url: Mapped[str] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey("librery_system.category.id"))
    #relationship
    Book: Mapped["Category"] = relationship(back_populates="book",uselist=False)
    user: Mapped[list["Favorite"]] = relationship(back_populates="book")

class Category(Base):
    __tablename__ = "category"
    __table_args__ = {"schema":"librery_system"}

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column()

Base.metadata.create_all(Engine)

