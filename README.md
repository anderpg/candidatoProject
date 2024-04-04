Proyecto en Fastapi, que tiene un endpoint "/candidato", que debe ser un método POST que reciba el DNI, Nombre y Apellido, que escriba esos datos en un sqlite.

Para crear un proyecto básico de FastAPI que cumpla estos requisitos, primero hay que instalar FastAPI y SQLAlchemy (para trabajar con la base de datos SQLite). 

Luego, configurar la aplicación con un endpoint /candidato que acepte solicitudes POST y almacene los datos recibidos en una base de datos SQLite. 

Para instalar FastAPI y SQLAlchemy: 'pip install fastapi uvicorn sqlalchemy'

En el repositorio hay un archivo llamado 'main.py' que tiene:

 1. La configuración de la base de datos SQLite.
 2. La definición del modelo de Candidato.
 3. La creación de la tabla en la base de datos.
 4. La iniciación de la aplicación FastAPI.
 5. La definición del modelo Pydantic para la solicitud POST.
 6. Endpoint para crear un nuevo candidato ("/candidato").
 7. La definición de un punto de partida para el servidor.

Para iniciar el servidor ejecutar: 'uvicorn main:app --reload' y la aplicación estará arrancada en http://localhost:8000

Con todo esto en funcionamiento, se podrán realizar solicitudes POST a http://localhost:8000/candidato con los datos del candidato en el cuerpo de la solicitud.
