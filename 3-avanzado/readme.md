# python en modo tipado estatico

Como sabemos, python es de tipado dinamico pero a partir de python 3.6 es posible simular tipado estatico.

Como?

Añadiendo el tipo de la variable al declararlo.

Ej:

variable: type = value
a: int = 5
b: str = "Hola"
c: bool = True


## Functions
Podemos definir los tipos de variables que podemos recibir como así también que tipo de variable estaremos respondiendo.

```
def function_name(variable: type) -> type:
    return .....

def suma(a: int, b: int) -> int:
    return a + b
```

Ej: creamos archivo 1-palindrome.py

```
def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

is_palindrome("ana")
//True

```

Ahora, testeamos con un numero
is_palindrome(1000)
//AttributeError: 'int' object has no attribute 'replace'

Espera, y la validación? Bueno, para validar correctamente este tipo de casos (numéricos) ejecutamos lo siguiente (con el anterior)

```
λ mypy 1-palindrome.py --check-untyped-defs
```
Resultado

```
1-palindrome.py:8: error: Argument 1 to "is_palindrome" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
```

# clousure

reglas para encontrar un clousure

- debemos tener una nested function
- la nested function debe referenciar un valor de un scope superior
- la función que envuelve la nested debe retornarla también

cuando tenemos una clase que tiene solo un método
cuando trabajamos con decoradores

Ej:
```
def main():
    a=1
    def nested():
        print(a)
    
    return nested

my_func = main()
my_func() //1
```

# decorador
funcion que recibe como parámetro otra funcion, le añade cosas y retorna una funcion diferente.

```
def decorador(fun):
    def envoltura():
        print("Esto se añade a mi funcion original")
        fun()
    return envoltura

def saludo():
    print("Hola")

saludo() 
#Hola

saludo = decorador(saludo)
saludo()
# Esto se añáde a mi funcion original
# Hola
```

Podemos mejorar el código con azucar sintactica, cómo?
```
def decorador(fun):
    def envoltura():
        print("Esto se añade a mi funcion original")
        fun()
    return envoltura

@decorador
def saludo():
    print("Hola")

saludo() 
#Esto se añade a mi funcion original
# Hola
```

@decorador define que la función "saludo" formará parte de la funcion "decorador"
Esto es lo mismo que hacer 
```
def saludo():
    print("Hola")
saludo = decorador(saludo)
```
Entonces, en vez de definir la funcion saludo y después enviar la funcion saludo a "decorador" primero se indica de que la función bajo el @ formará parte de tu clousure
Ojo, se debe de hacer referencia al clousere que deseas envolver con @
```
 @decorador
def saludo():
    print("Hola")

saludo() 
#Esto se añade a mi funcion original
# Hola
```

Otro ejemplo
```
def mayuscula(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayuscula
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje("Luis")) -> LUIS, RECIBISTE UN MENSAJE
```