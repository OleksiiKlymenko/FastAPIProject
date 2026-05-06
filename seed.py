from database import SessionLocal
from model import Workers, Child, Sallary
from datetime import date

def seed_data():
    # Використовуємо контекстний менеджер для безпечної роботи з базою
    with SessionLocal() as session:
        # 1. Створюємо 5 працівників
        workers = [
            Workers(first_name=f"Worker_{i}", last_name=f"Surname_{i}", ipn=1000+i, passport=f"AB{123450+i}")
            for i in range(1, 6)
        ]
        session.add_all(workers)
        session.flush()

        children = [
            Child(child_name=f"Child_{i}", birth_date=date(2015, 1, i), parrent_ipn=workers[i-1].ipn)
            for i in range(1, 6)
        ]
        session.add_all(children)


        salaries = [
            Sallary(ipn=workers[i-1].ipn, month=5, payment=20000 + (i * 1000))
            for i in range(1, 6)
        ]
        session.add_all(salaries)


        session.commit()
        print("База успішно заповнена по 5 рядків у кожній таблиці!")

if __name__ == "__main__":
    seed_data()