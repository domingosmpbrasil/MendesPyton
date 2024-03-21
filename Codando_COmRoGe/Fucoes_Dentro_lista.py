cidades = []

#Inceri um valor na sequência da lista, sendo esse no final da lista.
cidades.append('Santa Catarina')
cidades.append('irecê')
cidades.append('canarana')
cidades.append('')
cidades.append(1200)
print(cidades)

#removendo um valor específico
cidades.remove(1200)
print(cidades)

#inceri um valor na posição específicada do index
cidades.insert(3, 'Lapão')
print(cidades)

#Retira um valor da posição específicada no index sem excluilo.
cidades.pop(-1)
print(cidades)

#organisa a lista de forma ordenada númericamente ou alfabeticamente
cidades[2] = 'Canarana'
cidades[1] = 'Irecê'
print(cidades)
cidades.sort()
print(cidades)

#removendo um intem com base no index
del cidades[1]
print(cidades)

#Verificando a quantidade de itens em uma lista.
print(len(cidades))

#Buscando um item na lista e mostrando seu index.
print(cidades.index('Lapão'))
print(cidades[cidades.index('Lapão')])
