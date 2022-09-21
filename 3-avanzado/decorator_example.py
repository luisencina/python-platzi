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