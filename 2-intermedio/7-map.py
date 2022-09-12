def run():
    # retornar una nueva lista con sus cuadrados
    my_list = [1,2,3,4,5]

    # for
    arr = []
    for i in my_list:
        arr.append(i**2)

    print("for: ",arr)

    # list comprehensions

    arr_comp = [ i**2 for i in my_list ]
    print("comprehensions: ",arr_comp)

    # lambdas
    arr_lamb = lambda x: [ i**2 for i in my_list ]
    print("arr_lamb",arr_lamb(my_list))

    # filter
    odd = list(map(lambda x: x ** 2, my_list))
    print("map", odd)

if __name__ == "__main__":
    run()