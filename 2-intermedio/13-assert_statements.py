def divisors(num):
    try:
        
        # validación con raise
        if num < 0:
            raise ValueError("Error: Sólo se aceptan números positivos")
        
        divisors = [i for i in range(1, num+1) if num % i == 0]
        # for i in range(1, num + 1):
        #     if num % i == 0:
        #         divisors.append(i)
        
        return divisors
    except ValueError as ve:
        # corresponde al raise
        return ve


def run():
    try:
        num = input("Ingrese un número: ")
        assert num.isnumeric() and int(num) > 0, "Error: Sólo se aceptan números positivos"
        print(divisors(int(num)))
        print("Terminó el programa.")
    except AssertionError as ae:
        print(ae)


if __name__ == "__main__":
    run()