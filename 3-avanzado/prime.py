def is_prime(num: int) -> bool:
    result =  [i for i in range(1, num+1) if num%i==0]
    return len(result) == 2


def run():
    print(is_prime(13))


if __name__ == "__main__":
    run()