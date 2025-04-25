from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Cambia estos datos por los de tu entorno local
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/autosysbd"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT DATABASE();"))
        db_name = result.fetchone()[0]
        print(f"✅ Conectado correctamente a la base de datos: {db_name}")
except SQLAlchemyError as e:
    print(f"❌ Error al conectar: {e}")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()