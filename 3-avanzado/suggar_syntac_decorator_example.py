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

def mayuscula(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayuscula
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje("Luis"))