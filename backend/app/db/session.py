from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./test.db'  # Update with your database URL

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()