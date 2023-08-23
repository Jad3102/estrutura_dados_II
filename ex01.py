import timeit

lista = []

def gerar(tamanho,valor):
    start = timeit.default_timer()
    for i in range(tamanho):
        lista.append(valor)
    end = timeit.default_timer()
    print(f"tempo descorrido:{float(end - start)}")
    return lista

def buscar(index):
    start = timeit.default_timer()
    for x in lista:
        if index == x:
            print("Achei", x)
        else:
            print ("ops, parece que não encontrei este valor na lista!")
    end = timeit.default_timer()
    print(f"tempo descorrido:{float(end - start)}")

def buscabinaria(index):
    inicio = 0
    fim = len(lista)
    meio = lista[len(lista)/2]

    if meio == index:
        return 
gerar(10000,1)
buscar(int(input("Numero:")))


