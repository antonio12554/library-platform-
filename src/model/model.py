#database
from src.core.db import Base,Engine
#sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema":"library_system"}

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True)
    hash_password: Mapped[str] = mapped_column()
    created_at: Mapped[str] = mapped_column()
    prefile_id: Mapped[int] = mapped_column(ForeignKey("library_system.prefile.id"))
    library_id: Mapped[int] = mapped_column(ForeignKey("library_system.library.id"))
    #relationship
    prefile: Mapped["Prefile"] = relationship(back_populates="user",uselist=False)
    library: Mapped["Library"] = relationship(back_populates="user",uselist=False)

class Prefile(Base):
    __tablename__ = "prefile"
    __table_args__ = {"schema":"library_system"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    bio: Mapped[str] = mapped_column()
    avatar: Mapped[str] = mapped_column()
    #relationship
    user: Mapped["User"] = relationship(back_populates="prefile",uselist=False)

class Library(Base):
    __tablename__ = "library"
    __table_args__ = {"schema":"library_system"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("library_system.book.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("library_system.user.id"), unique=True)
    acquired_at: Mapped[str] = mapped_column()
    #relationship
    user: Mapped["User"] = relationship(back_populates="library",uselist=False)
    book: Mapped["Book"] = relationship(back_populates="library")

class Book(Base):
    __tablename__ = "book"
    __table_args__ = {"schema":"library_system"}

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column()
    subtitle: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    author: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    pdf_url: Mapped[str] = mapped_column()
    number_page: Mapped[int] = mapped_column()
    created_at: Mapped[str] = mapped_column()
    book_cover_image_url: Mapped[str] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey("library_system.category.id"))
    #relationship
    category: Mapped["Category"] = relationship(back_populates="book",uselist=False)
    library: Mapped[list["Library"]] = relationship(back_populates="Book")
    genre: Mapped[list["Genre"]] = relationship(back_populates="book")

class Category(Base):
    __tablename__ = "category"
    __table_args__ = {"schema":"library_system"}

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column()
    #relatioship
    book: Mapped["Book"] = relationship(back_populates="category",uselist=False)

class Genre(Base):
    __tablename__ = "genre"
    __table_args__ = {"schema":"library_system"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    genre: Mapped[str] = mapped_column()
    book_id: Mapped[int] = mapped_column(ForeignKey("library_system.book.id"))
    #relationship
    book: Mapped[list["Book"]] = relationship(back_populates="genre")



Base.metadata.create_all(Engine)

