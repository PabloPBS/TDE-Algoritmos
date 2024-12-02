def SelectionSort(lista):
    # Obtém o tamanho da lista
    n = len(lista)
    
    # Inicializa a contagem de trocas como 0
    qtdTrocas = 0
    
    # Loop externo percorre cada posição da lista
    for i in range(n):
        # Assume que o menor elemento está na posição 'i'
        menor_indice = i
        
        # Loop interno procura o menor elemento na sublista não ordenada
        for j in range(i + 1, n):
            # Se encontrar um elemento menor, atualiza o índice do menor elemento
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        
        # Após o loop interno, verifica se encontrou um índice diferente
        if menor_indice != i:
            # Troca o elemento atual (lista[i]) com o menor elemento encontrado
            lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
            
            # Incrementa o contador de trocas
            qtdTrocas += 1
    
    # Retorna o número total de trocas realizadas
    return qtdTrocas



def InsertionSort(lista):
    # Inicializa o contador de trocas
    qtdTrocas = 0
    
    # Loop externo percorre os elementos da lista, começando do segundo (índice 1)
    for i in range(1, len(lista)):
        # A "chave" é o elemento atual a ser inserido na posição correta
        chave = lista[i]
        
        # Define o índice inicial para comparação, começando pelo elemento anterior
        j = i - 1
        
        # Loop interno: move os elementos maiores que a chave uma posição à frente
        while j >= 0 and lista[j] > chave:
            # Desloca o elemento para a direita
            lista[j + 1] = lista[j]
            
            # Decrementa o índice para continuar comparando com os elementos anteriores
            j -= 1
            
            # Incrementa o contador de trocas
            qtdTrocas += 1
        
        # Insere a chave na posição correta (após os deslocamentos)
        lista[j + 1] = chave
    
    # Retorna o número total de trocas realizadas
    return qtdTrocas



def BubbleSort(lista):
    # Variável que indica se houve alguma troca na iteração atual
    trocar = True
    
    # Define o número de passadas (iterações) necessário
    passnum = len(lista) - 1  # A última posição a ser comparada na primeira passagem
    
    # Inicializa o contador de trocas
    qtdTrocas = 0
    
    # Loop externo: continua enquanto houver trocas e ainda houver elementos a verificar
    while passnum > 0 and trocar:
        # Supõe inicialmente que nenhuma troca será feita nesta iteração
        trocar = False

        # Loop interno: percorre os elementos ainda não ordenados
        for i in range(passnum):
            # Compara o elemento atual com o próximo
            if lista[i] > lista[i + 1]:  # Ordenação crescente
                # Realiza a troca caso o elemento atual seja maior que o próximo
                trocar = True
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
                
                # Incrementa o contador de trocas
                qtdTrocas += 1

        # Reduz o número de elementos a verificar na próxima passagem
        passnum -= 1
    
    # Retorna o número total de trocas realizadas
    return qtdTrocas