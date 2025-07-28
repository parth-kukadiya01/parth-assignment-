from sqlmodel import create_engine, Session
from app.core.config import Settings

settings = Settings()
engine = create_engine(settings.database_url, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    from app.models.models import SQLModel

    SQLModel.metadata.create_all(engine)
