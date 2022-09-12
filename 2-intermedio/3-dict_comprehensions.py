def run():
    # crear un diccionario con los 100 primeros numeros naturales que no sean divisibles por 3 y estos elevarlos al cubo
    # for
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    # comprehensions
    my_dict = { i : i**3 for i in range(1, 101) if i % 3 != 0}
    # {key:value for value in iterable if condition}
    # para cada elemento del iterable guardar el elemento key:value solo si cumple la condicion
    print(my_dict)

    # challenge: guardar los mil primero numeros naturales con sus respectivas raices cuadradasa

    challenge = { i: round(i**0.5, 2) for i in range(1, 101) }
    print(challenge)


if __name__ == "__main__":
    run() 