try:
    edad = int(input("Escribe tu edad: "))
    if edad >= 18:
        print("Eres Mayor de edad")
    else:
        print("Eres Menor de edad")
except Exception as e:
    print("Ingrese un número válido, error: ", e)