def saludo(func):
    func()


def hola():
    print("Hola")


def adios():
    print("Adios")


def run():
    saludo(hola)
    saludo(adios)


# las funciones de orden superior son funciones que reciben a otras funciones para despues ejecutarlos

if __name__ == "__main__":
    run()