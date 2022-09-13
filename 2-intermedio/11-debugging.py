def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError("Error: Sólo se aceptan números positivos")
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        
        return divisors
    except ValueError as ve:
        return ve


def run():
    try:
        num = int(input("Ingrese un número: "))
        print(divisors(num))
        print("Terminó el programa.")
    except ValueError:
        print("Sólo se aceptan números.")


if __name__ == "__main__":
    run()