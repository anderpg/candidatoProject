from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definición del modelo de Candidato
class Candidato(Base):
    __tablename__ = "candidatos"
    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, unique=True, index=True)
    nombre = Column(String)
    apellido = Column(String)

# Crear la tabla en la base de datos
Base.metadata.create_all(bind=engine)

# Iniciar la aplicación FastAPI
app = FastAPI()

# Definición del modelo Pydantic para la solicitud POST
class CandidatoCreate(BaseModel):
    dni: str
    nombre: str
    apellido: str

# Endpoint para crear un nuevo candidato
@app.post("/candidato")
async def create_candidato(candidato: CandidatoCreate):
    db = SessionLocal()
    db_candidato = Candidato(dni=candidato.dni, nombre=candidato.nombre, apellido=candidato.apellido)
    db.add(db_candidato)
    db.commit()
    db.refresh(db_candidato)
    return {"mensaje": "Candidato creado exitosamente", "candidato": db_candidato}

# Definir un punto de partida para el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
