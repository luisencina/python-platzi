def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }

    # obtener solo los keys
    for llave in mi_diccionario.keys():
        print(llave)

    # obtener solo los values
    for value in mi_diccionario.values():
        print(value)

    # obtener key/value
    for llave, value in mi_diccionario.items():
        print("el valor de "+llave+ " es "+ str(value))


if __name__ == "__main__":
    run()