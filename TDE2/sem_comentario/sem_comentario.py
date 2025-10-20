def fifo(paginas, quadros=8):
    memoria = []
    for pagina in paginas:
        if pagina not in memoria:
            if len(memoria) < quadros:
                memoria.append(pagina)
            else:
                memoria.pop(0)
                memoria.append(pagina)
    return memoria



def lru(paginas, quadros=8):
    memoria = []
    for pagina in paginas:
        if pagina in memoria:
            memoria.remove(pagina)
        elif len(memoria) == quadros:
            memoria.pop(0)
        memoria.append(pagina)
    return memoria



def mru(paginas, quadros=8):
    memoria = []
    for pagina in paginas:
        if pagina in memoria:
            memoria.remove(pagina)
        elif len(memoria) == quadros:
            memoria.pop()
        memoria.append(pagina)
    return memoria


sequencia_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
sequencia_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
sequencia_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

print("FIFO A:", fifo(sequencia_a))
print("LRU A:", lru(sequencia_a))
print("MRU A:", mru(sequencia_a))

print()

print("FIFO B:", fifo(sequencia_b))
print("LRU B:", lru(sequencia_b))
print("MRU B:", mru(sequencia_b))

print()

print("FIFO C:", fifo(sequencia_c))
print("LRU C:", lru(sequencia_c))
print("MRU C:", mru(sequencia_c))
