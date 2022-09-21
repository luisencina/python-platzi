# creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

print(next(my_iter)) # retorna 1

# como recorrer toda la lista?

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

# como hacer mas facil esto?
# python ya tiene un alias para esto, los ciclos for
# for es una asucar sintáctica del while descrito arriba

for element in my_list:
    print(element)