def palindromo(string):
    if string == string[::-1]:
        return True
    else:
        return False


def run():
    # crear funcion para corroborar si es palindromo
    print(palindromo("ana"))

    # lambda en python son funciones anonimas cuyo identificador es la variable, deben de describirse en una sola linea
    # estos retornan un obtejo te tipo funcion
    # para invocarlas le llaman a las variables y se las pasan las variables dentro de parentesis

    # si nos fijamos, la linea de abajo realiza la misma validacion que la funcion "palindromo" descrita en la linea 1
    lambda_palindromo = lambda string: string == string[::-1]
    print(lambda_palindromo("ana"))

if __name__ == "__main__":
    run()