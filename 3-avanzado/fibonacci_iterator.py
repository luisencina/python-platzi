from html.entities import name2codepoint
import time


class FiboIter():

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
            if self.max == 0:
                raise StopIteration
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                if self.max:
                    if self.aux >= self.max:
                        raise StopIteration
                # self.n1 = self.n2
                # self.n2 = self.aux
                # la siguiente linea es lo mismo que las dos anteriores (swapping)
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
            


if __name__ == "__main__":
    
    # máximo número acumulado
    fibonacci = FiboIter(10)
    # hasta el infinito
    fibonacci = FiboIter()
    
    for element in fibonacci:
        print(element)
        time.sleep(0.05)