from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base  # Імпортуємо твій Base з файлу з моделями

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_db()