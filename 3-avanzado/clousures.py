def make_multiplier(x):

    def multiplier(n):
        return x * n
    
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

# print(times10(3))         #30
# print(times4(4))          #20
# print(times10(times4(2))) #80