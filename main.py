nomes = ["João", "Maria", "Pedro", "Ana", "Lucas", "Carla", "Mateus", "Juliana",
         "Felipe", "Laura", "Rafael", "Camila", "Gustavo", "Amanda", "Marcos"]

# Usuario infomra o nome que deseja pesquisar
pesquisa = str(input("Insira a pesquisa: ")).strip().capitalize()

# Retorna o indice do nome pesquisado caso exista, se não existir não retorna nada

try:
    indice = nomes.index(pesquisa)

# verifica se o nome está ou não na lista
    print(f"nome encontrado: {pesquisa}, na posição {indice}")

except:
    print(f"O nome {pesquisa} não esta na lista ")
