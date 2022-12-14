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

## Request Body y Response Body

Es el cuerpo de una petición HTTP.


```
@app.post("/person/new")
def create_person(req):
    your_code
```

![Query Parameters](/4-FastAPI_Fundamentos/docs/req_res_body.png)


# Antes de continuar...

## Modelos

Un modelo es la representacion de una entidad en codigo, al menos de una manera descriptiva. Una entidad es un objeto de la vida real, que tiene ciertos atributos. Por ejemplo:

- Carro: color, motor, año, marca
- Persona: edad, nombres, apellidos, altura

Para poder crear modelos en el código se utiliza la librería Pydantic, importando la clase BaseModel:

```
#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

#Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

# Request and Response Body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person
```


![Query Parameters](/4-FastAPI_Fundamentos/docs/req_body.png)

## Validations

Todo elemento o atributo del request pueden realizar validaciones.

Con Body, Query y Path podemos indicar cualquier tipo de validacion, los mas comunes son:
- None (indica que éste es opcional, al ser opcional fastAPI lo recibe como None)
- min_length, define la cantidad minima de caracteres
- max_length, define la cantidad maxima de caracteres
- regex, para realizar validaciones con cadenas (solo para strings)
- ge, (int) greater or equal than, mayor o igual que
- le, (int) less or equal than, menor o igual que
- gt, (int) greater than, mayor que
- lt, (int) less than, menor que
- title, para añadir un titulo en mi parámetro
- description, añadir una descripción a mi parámetro

con los tres puntos "..." indicamos que ese atributo será obligatorio.


### Body


En FastAPI, para definir que trabajaremos con Body debemos de importarlo.

> from fastapi import Body


Con la librería Optional indicamos cuáles son opcionales

```
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.post("/person/new")
def create_person(
    person: Person = Body(...)
):
    return person

```


### Query

Importamos Query de fastapi
```
 from fastapi import Query
```

```
# Validations: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: int = Query(...)
):
    return { name: age }
```

### Path

Importamos Path de fastapi
```
 from fastapi import Path

# Validations: Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person id",
        description="It's required"
        )
):
    return { person_id: "OK" }
```

### Validacion de body params

fastapi no realiza las validaciones de los atributos del body, para esto, necesitamos otra librería.
pydantic posee un metodo de validación de atributos para un payload gracias a "Field"

```
from pydantic import Field

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    hair_color: Optional[str] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)
```

En caso que querramos realizar validaciones con Enums

```

from enum import Enum
from pydantic import Field

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    yellow = "yellow"
    blonde = "blonde"
    red = "red"


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)
```


### Tipos de datos en Python para validaciones con pydantic

![Query Parameters](/4-FastAPI_Fundamentos/docs/types.png)