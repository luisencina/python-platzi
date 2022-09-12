def run():
    # retornar solo los pares
    my_list = [1,2,3,4,5,6,7,8,9]

    # for
    arr = []
    for i in my_list:
        if i % 2 == 0:
            arr.append(i)

    print("for: ",arr)

    # list comprehensions

    arr_comp = [ i for i in my_list if i % 2 == 0 ]
    print("comprehensions: ",arr_comp)

    # lambdas
    arr_lamb = lambda x: [ i for i in my_list if i % 2 == 0 ]
    print("arr_lamb",arr_lamb(my_list))

    # filter
    odd = list(filter(lambda x: x % 2 == 0, my_list))
    print("filter", odd)

if __name__ == "__main__":
    run()