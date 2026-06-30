from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from app.config.settings import settings

DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


from sqlalchemy import text
from sqlalchemy.orm import Session

def check_postgres():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print(f"Postgres Error: {e}")
        return False


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

print("=" * 50)
print("HOST:", settings.POSTGRES_HOST)
print("PORT:", settings.POSTGRES_PORT)
print("USER:", settings.POSTGRES_USER)
print("PASSWORD:", settings.POSTGRES_PASSWORD)
print("DB:", settings.POSTGRES_DB)
print("DATABASE_URL:", DATABASE_URL)
print("=" * 50)