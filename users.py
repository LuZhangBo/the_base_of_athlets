import uuid
import datetime

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):
    """
    Описываем структуру таблицы athelete
    """
    __tablename__ = 'user'

    id = sa.Column(sa.String(36), primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)


def connect_db():
    """
    Устанавливаем соединение с базой данных, и создаём таблицу
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def request_data():
    """
    Добавляем полученные у пользователя данные в список users
    """
    print("Здравствуйте! Введите, пожалуйста, Ваши данные!")
    first_name = input("Введите Ваше имя: ")
    last_name = input("А теперь фамилию: ")
    gender = input("Введите Ваш пол (Male или Female): ")
    email = input("Нам также понадобится адрес Вашей электронной почты: ")
    birthdate = input(
        "Введите, пожалуйста, Вашу дату рождения (в формате ГГГГ-ММ-ДД): ")
    height = input(
        "Нам также понадобится Ваш рост (в м, целую и десятичную часть отделяйте точкой): ")

    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )

    return user


def main():
    """
    Осуществляем взаимодействие с пользователем, обрабатываем вводимые данные
    """
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Ваши данные успешно сохранены в базе данных. Спасибо за сотрудничество!")


if __name__ == "__main__":
    main()
