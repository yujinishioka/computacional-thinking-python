def isEmpty(fila):
    if(len(fila) == 0):
        return True
    else:
        return False

def isFull(fila):
    return False

def put(fila, info):
    fila.append(info)

def get(fila):
    return fila.pop(0)

def peek(fila):
    return fila[0]