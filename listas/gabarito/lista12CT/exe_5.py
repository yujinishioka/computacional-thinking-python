from pilha import pilha

def isOpen(s):
    if s == '(' or s == '[' or s == '{':
        return True
    else:
        return False

def match(a, b):
    if a == '(' and b == ')':
        return True
    elif a == '[' and b == ']':
        return True
    elif a == '{' and b == '}':
        return True
    else:
        return False

seq = "((([[]]{}[]{}{()})))"
pilha = pilha()

for simbolo in seq:
    
    if isOpen(simbolo):
        pilha.put(simbolo)
    
    else:
        if pilha.isEmpty():
            print("Error: Closed")
            exit()
        
        info = pilha.pop()
        
        if not match(info, simbolo):
            print("Error: No match")
            exit()

if pilha.isEmpty():
    print("Sequencia Valida")

else:
    print("Sequencia Nao Valida")