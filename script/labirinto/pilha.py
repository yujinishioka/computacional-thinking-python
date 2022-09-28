class pilha:

    def __init__(self):
        self.lista = []

    def isFull(self):
        return False

    def isEmpty(self):
        return len(self.lista) == 0    

    def put(self, info):
        self.lista.append(info)

    def pop(self):
        return self.lista.pop()

    def peek(self):
        pos = len(self.lista) - 1
        return self.lista[pos] 
