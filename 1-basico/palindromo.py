def palindromo(palabra):
    palabra = str(palabra).lower().replace(" ", "")
    print("cadena ingresada: ", palabra)
    print("invirtiendo: ", palabra[::-1])
    return palabra == palabra[::-1]


def run():
    cadena = input("Inserte oración: ")
    es_palidromo = palindromo(cadena)
    if es_palidromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == "__main__":
    run()