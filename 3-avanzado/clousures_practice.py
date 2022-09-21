# hola 3 -> holaholahola
# luis 2 -> luisluis

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo se acepta string"
        return string * n
    return repeater

def make_division_by(n):
    assert type(n) == int, "Solo se aceptan numeros"
    def division(x):
        assert type(x) == int, "Solo se aceptan numeros"
        return x/n
    return division

def run():
    repeat3 = make_repeater_of(3)
    print(repeat3("hola"))
    
    repeat2 = make_repeater_of(2)
    print(repeat2("luis"))

    division_by_3 = make_division_by(3)
    print(division_by_3(18))

if __name__ == "__main__":
    run()

