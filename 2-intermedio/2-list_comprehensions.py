def module(i):
    if i % 4 == 0 and i % 6 == 0 and i % 9 == 0:
        return True
    else:
        return False  

def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [ i**2 for i in range(1,101) if i % 3 !=0 ]
    # [ element for element in iterable if condition ]
    # pero como se lee?
    # para cada elemento en el iterable, guardaré ese elemento solo si cumple la condicion

    print(squares)

    # imprimir una lista de numeros que sean divisible entre 4,6 y 9
    challenge = [ i for i in range(1, 500) if module(i)]
    print(challenge)

if __name__ == "__main__":
    run()