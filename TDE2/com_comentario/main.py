#FIFO
def fifo(paginas, quadros=8):
    memoria = []  #aqui vai listar os que representa os quadros de memoria
    for pagina in paginas:  #dai percorre cada pagina da sequencia
        if pagina not in memoria:  #se a pagina não está na memoria
            if len(memoria) < quadros:  #ainda tem espaço nos quadros
                memoria.append(pagina)  #dps adiciona a pagina
            else:  #memoria cheia
                memoria.pop(0)  #isso vai remove a pagina mais antiga que eh a primeira
                memoria.append(pagina)  #dai adiciona nova pagina
    return memoria  #dps retorna o estado final da memoria



#LRU
def lru(paginas, quadros=8):
    memoria = []  #lista que representa os quadros de memoria
    for pagina in paginas:
        if pagina in memoria:  #se a pagina ja está na memoria
            memoria.remove(pagina)  #remove para atualizar como mais recente
        elif len(memoria) == quadros:  #se a memoria está cheia
            memoria.pop(0)  #remove a pagina menos recentemente usada
        memoria.append(pagina)  #adiciona a pagina atual como a mais recente
    return memoria



#MRU
def mru(paginas, quadros=8):
    memoria = []  #lista que representa os quadros de memoria
    for pagina in paginas:
        if pagina in memoria:  # se a pagina ja está na memoria
            memoria.remove(pagina)  #remove para atualizar a posição
        elif len(memoria) == quadros:  #se a memoria está cheia
            memoria.pop()  #remove a pagina mais recentemente usada
        memoria.append(pagina)  #adiciona a pagina atual como a mais recente
    return memoria



#variaveis com sequencias
sequencia_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
sequencia_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
sequencia_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

#aqui vai testar todos os algoritmos com as sequencias
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

