from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

# Modelo de la base de datos
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str

# Esquema para recibir el JSON del cliente (usamos SQLModel para no importar más cosas)
class LoginData(SQLModel):
    username: str
    password: str

# Base de datos local
engine = create_engine("sqlite:///database.db")
app = FastAPI()

# Esto corre solito cuando inicias el servidor
@app.on_event("startup")
def iniciar_base():
    # Crea el archivo de la base de datos
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        # Si la base está vacía, metemos el usuario quemado
        if not session.exec(select(User)).first():
            session.add(User(username="admin", password="123"))
            session.commit()

@app.post("/login")
def login(datos: LoginData):
    with Session(engine) as session:
        # Buscamos al usuario que mandaron
        usuario_db = session.exec(select(User).where(User.username == datos.username)).first()
        
        # Validamos: si no existe el usuario o la clave es diferente, se rechaza
        # (Es mejor mandar un solo error 401 para no dar pistas de qué falló)
        if not usuario_db or usuario_db.password != datos.password:
            raise HTTPException(status_code=401, detail="Usuario o clave incorrecta")
        
        return {"mensaje": "Login exitoso", "usuario": usuario_db.username}