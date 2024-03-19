lista = [32,45,35,12,32,2,33]
listaPares = []
listaImpares = []

for i in lista:
    if  (i % 2 ==0):
        listaPares.append(i)
    else:
        listaImpares.append(i)

print('Lista total:')
for i in lista:
    print(i)

print('Lista Pared:')
for i in listaPares:
    print(i)

print('Lista Impares')
for i in listaImpares:
    print(i)

