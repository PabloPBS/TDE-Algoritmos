import csv

def BubbleSort(lista):
    trocar = True
    passnum = len(lista)-1
    qtdTrocas = 0
    while passnum > 0 and trocar: # Checa se a lista já está ordenada
        trocar = False
        for i in range(passnum):
            if lista[i]>lista[i+1]: # Para ordenar de forma decrescente, basta mudar o ">" para "<="
                trocar = True
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                qtdTrocas += 1

        passnum -= 1
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

lista = criarlista(listaPrecos[0]) 
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
qtdTrocas = BubbleSort(lista)
print("-"*25 + "\n" + "Lista depois: \n" + "-"*25)
print(lista)
print("-"*25 + "\n" + f"Trocas realizadas: {qtdTrocas}.")