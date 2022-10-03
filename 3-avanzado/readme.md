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

# Iteradores

creando un iterador

```
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

--Iterando un iterador---

print(next(my_iter)) 
# 1

```

como recorrer toda la lista?

```
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break
# 1
# 2
# 3
# 4
# 5
```
## como hacer mas fácil esto?

python ya tiene un alias para esto, los ciclos for

for es una asucar sintáctica del while descrito arriba

```
my_list = [1,2,3,4,5]

for element in my_list:
    print(element)
# 1
# 2
# 3
# 4
# 5

```

## SET

SET, estructura de datos inmutables y únicos.

```
my_set = {3, 4, 5}
print(my_set) # {3, 4, 5}
```

Set de diferentes tipos de datos

```
my_set = {1.0, "Hi", (1, 4, 7)}
print(my_set) # {1.0, "Hi", (1, 4, 7)}
```

ejemplo de operaciones sobre sets 

```
my_set = {1, 2, 3} 
print(my_set) #Output {1, 2, 3} 
```

añadiendo un elemento al set 

```
my_set.add(4) 
print(my_set) #Output {1, 2, 3, 4}
```

añadiendo varios elementos al set, python ignorará elementos repetidos 

```
my_set.update([1, 5, 6]) 
print(my_set) #Output {1, 2, 3, 4, 5, 6}
```

Eliminado elementos del set 

```
my_set.discard(1) 
print(my_set) #Output {2, 3, 4, 5, 6}
```

Borrando un elemento aleatorio 

```
my_set.pop()
print(my_set) #Output el set menos un elemento aleatorio 
```

limpiar el set 

```
my_set.clear()
print(my_set) # Output set() 
```

### Podemos utilizar estructuras de datos existentes para transformarlas a sets utilizando el método set:

usando listas para crear sets

```
my_list = [1, 2, 3, 3, 4, 5]
my_set = set(my_list)
print(my_set)  #output {1, 2, 3, 4, 5}
```

#usando tuplas para crear sets 

```
my_tuple =  ("hola", "hola", 1, 2)
my_set2 = set(my_tuple)
print(my_set2) #Output {'hola', 1}
```

### unión de sets

Combina todos los elementos sin repetirlos

```
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 | my_set2
print(my_set3) {3, 4, 5, 6, 7}
```

### intersección de sets

Une solo los elementos en comun
```
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 & my_set2
print(my_set3) {5}
```

### diferencias de sets

Nos entrega como resultado el set obtenido de eliminar de un primer set todos los elementos que comunes o que se repiten del segundo set.
```
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 - my_set2
print(my_set3) {3, 4}

my_set3 = my_set2 - my_set1
print(my_set3) {6, 7}
```

### diferencias simetricas

devuelve todos los elementos de dos sets sin los elementos en comunes

```
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}
my_set3 = my_set2 ^ my_set1
print(my_set3) {3, 4, 6, 7}
```