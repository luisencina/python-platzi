from functools import reduce

def run():
    # sumar todos los elementos del arreglo
    my_list = [2,2,2,2,2]

    # for
    val = 0
    for i in my_list:
        val = val + i

    print("for: ",val)

    # reduce
    odd = reduce(lambda a, b: a + b, my_list)
    print("reduce: ", odd)

if __name__ == "__main__":
    run()