import csv

def InsertionSort(lista):
    qtdTrocas = 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        # Move os elementos maiores que a chave uma posição à frente
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
            qtdTrocas += 1
        # Insere a chave na posição correta
        lista[j + 1] = chave
        
    return qtdTrocas

def criarlista(arquivo_csv):
    valores = []
    with open(arquivo_csv, mode='r') as file:
        leitor_csv = csv.reader(file)
        for linha in leitor_csv:
            for valor in linha:
                try:
                    valores.append(float(valor))
                except ValueError:
                    pass
    return valores

listaPrecos = ['CSVs/ListadePrecos10.csv', 'CSVs/ListadePrecos100.csv', 'CSVs/ListadePrecos10000.csv', 'CSVs/ListadePrecos10Ordenado.csv', 'CSVs/ListadePrecos100Ordenado.csv', 'CSVs/ListadePrecos10000Ordenado.csv', 'CSVs/ListadePrecos10Inversa.csv', 'CSVs/ListadePrecos100Inversa.csv', 'CSVs/ListadePrecos10000Inversa.csv']

lista = criarlista(listaPrecos[3])
# Troque o índice para ordenar arquivos diferentes: 
# 0 - lista de 10; 
# 1 - lista de 100; 
# 2 - lista de 10000; 
# 3 - lista de 10 já ordenada; 
# 4 - lista de 100 já ordenada; 
# 5 - lista de 10000 já ordenada;
# 6 - lista de 10 inversamente ordenada;
# 7 - lista de 100 inversamente ordenada;
# 8 - lista de 10000 inversamente ordenada

print("Lista antes:\n" + "-"*25)
print(lista)
qtdTrocas = InsertionSort(lista)
print("-"*25 + "\n" + "Lista depois: \n" + "-"*25)
print(lista)
print("-"*25 + "\n" + f"Trocas realizadas: {qtdTrocas}.")