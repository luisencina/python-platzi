from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print("Pasaron " + str(time_elapse.total_seconds()) + " segundos.")
    return wrapper

@execution_time
def random_func():
    print("random_func")
    for _ in range(1, 10000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    print("suma")
    return a + b

@execution_time
def saludo(nombre):
    print("saludo")
    print("Hola ", nombre)

random_func()
suma(1,2)
saludo("Luis")