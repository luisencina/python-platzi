# Que es FastAPI?

Es el framework mas veloz para el desarrollo backend con Python.


Compiten directamente contra GO y Nodejs.

Es OpenSource.

# FastAPI utiliza otros frameworks dentro de si para funcionar

1. Uvicorn: es una librería de Python que funciona de servidor, es decir, permite que cualquier computadora se convierta en un servidor.

1. Starlette: es un framework de desarrollo web de bajo nivel, para desarrollar aplicaciones con este requieres un amplio conocimiento de Python, entonces FastAPI se encarga de añadirle funcionalidades por encima para que se pueda usar mas fácilmente.

1. Pydantic: Es un framework que permite trabajar con datos similar a pandas, pero este te permite usar modelos los cuales aprovechara FastAPI para crear la API

# Hello World

Creemos nuestro primer hello world con fastAPI, para ello, necesitamos instalar el framework fastAPI y uvicorn.

>λ pip install fastapi uvicorn

El hello world se ve algo así 

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}
```

Se iporta el módilo fastapi de FastAPI, lo asociamos a una variable con FastAPI().

```
from fastapi import FastAPI

app = FastAPI()
```

Creamos un decorador y añadimos el metodo con el path que estará "decorando" la función que atenderá esta petición.
 ```
@app.get("/")
def home():
    return {"Hello": "World"}
```

Para correr el servicio ejecutamos el siguiente comando en nuestra terminal.

> λ uvicorn hello_world:app --reload

hello_world es el nombre del archivo.


app es la variable que instancia el framework FastAPI.

--reload es un flag para hacer hotreloading


```C:\labs\platzi\python\4-FastAPI_Fundamentos(master)
(venv) λ uvicorn hello_world:app --reload
←[32mINFO←[0m:     Will watch for changes in these directories: ['C:\\labs\\platzi\\python\\4-FastAPI_Fundamentos']
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://127.0.0.1:8000←[0m (Press CTRL+C to quit)
←[32mINFO←[0m:     Started reloader process [←[36m←[1m18620←[0m] using ←[36m←[1mStatReload←[0m
←[32mINFO←[0m:     Started server process [←[36m11812←[0m]
←[32mINFO←[0m:     Waiting for application startup.
←[32mINFO←[0m:     Application startup complete.
```

Una vez listo, vamos a nuestro navegador a la url que nos indica la salida "http://127.0.0.1:8000"


# Documentación
FastAPI por defecto realiza la documentación de los rescursos que exponemos en nuestras API con swagger o redoc.


Acceder a la documentación interactiva con Swagger UI:

>{localhost}/docs

Ej: http://127.0.0.1:8000/docs

Redoc:

> {localhost}/redoc

Ej: Ej: http://127.0.0.1:8000/redoc

# Path Operations

¿Que es un path?

Un path es lo mismo que un route o endpoints y es todo aquello que vaya después de nuestro dominio a la derecha del mismo.

¿Que son las operations?

Un operations es exactamente lo mismo que un método http y tenemos las siguientes más populares: GET, POST, PUT y DELETE

Y otros métodos como OPTIONS, HEAD, PATCH …

Entonces, cuando alguien nos hable de ""Path Operations" realmente lo que hacemos referencia es "realizar peticiones" a un dominio específico con un metodo http.

![Path Operations](/4-FastAPI_Fundamentos/docs/path_operations.png)

## Path Operation Decorator
Denominamos Decorator cuando el "decorador" de la app es consumido con un metodo http y un path específico.
```
@app.get("/")
```
## Path Operation Function
La función del operador es la encargada de manejar la lógica del recurso que accedemos.
```
def home():
    return {"Hello": "World"}
```
## Path Parameter
son los parámetros que son enviados en un path específico.
Si el path en cuestión requiere un parámetro éste es OBLIGATORIO para que la petición entre a ese recurso.

Los parámetros de ruta son partes variables de una ruta URL . Por lo general, se utilizan para señalar un recurso específico dentro de una colección, como un usuario identificado por ID. Una URL puede tener varios parámetros de ruta.
```
@app.get("/{id}")
```
![Path Parameter](/4-FastAPI_Fundamentos/docs/path_parameters.png)

## Query Parameter
Cuando deseamos enviar parámetros opcionales utilizamos query parameters.

Un Query Patameter es un conjunto de elementos opcionales los cuales son añadidos al finalizar la ruta, con el objetivo de definir contenido o acciones en la url,
estos elementos se añaden despues de un ?
para agregar más query parameters utilizamos &

```
@app.get("/{id}/details?age=123")
```

![Query Parameters](/4-FastAPI_Fundamentos/docs/query_parameters.png)