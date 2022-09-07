# guaranies = input('Cuántos guaranies tienes?: ')
# guaranies = float(guaranies)
# valor_dolar = 6890
# dolares = guaranies / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)

# print("Tienes $"+dolares+" dólares.")

options = [
    {
        "option": "1",
        "moneda": "Dólares",
        "simbolo": "$",
        "valor": 6890
    },
    {
        "option": "2",
        "moneda": "Pesos Argentinos",
        "simbolo": "$",
        "valor": 20
    },
    {
        "option": "3",
        "moneda": "Soles",
        "simbolo": "S/",
        "valor": 1788
    }
]
def get_moneda(op):

    ret = False

    for option in options:
        if option['option'] == op:
            ret =  option

    return ret

def get_options():

    cadena = "\n"

    for option in options:
        cadena += option['option'] + "- " + option['moneda']  + "\n"

    return cadena


try:
    seleccion = input("""
Bienvenido!!!
Seleccione la moneda a la que quiere convertir sus guaranies:
        """
    +get_options()+
        """
Ingrese opción: """)
    moneda = get_moneda(seleccion)

    if moneda != False:
    
        guaranies = input('Cuántos guaranies tienes?: ')
        guaranies = float(guaranies)
        cambio = guaranies / float(moneda['valor'])
        cambio = round(cambio, 2)

        print("Tienes "+moneda['simbolo']+" "+str(cambio)+" "+moneda['moneda'])
    
    else: 
        print("Opción no válida")

except Exception as e:
     print("Error: ", e)