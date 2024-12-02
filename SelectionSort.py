import csv

def SelectionSort(lista):
    n = len(lista)
    qtdTrocas = 0
    for i in range(n):
        menor_indice = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        if menor_indice != i:
            lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
            qtdTrocas += 1
        
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

lista = criarlista(listaPrecos[2])  
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
qtdTrocas = SelectionSort(lista)
print("-"*25 + "\n" + "Lista depois: \n" + "-"*25)
print(lista)
print("-"*25 + "\n" + f"Trocas realizadas: {qtdTrocas}.")