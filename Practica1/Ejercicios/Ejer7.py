lista = []

print('Ingresar una lista de numero la cual finaliza con el numero 0')

num = int(input('Nro:'))
while (num != 0 ):
    lista.append(num)
    num = int(input('Nro:'))

cadenaFinal = ''

for i in lista:
    if (i % 3 != 0):
        cadenaFinal += str(i) + '-'

print('Cadena creada: | '+cadenaFinal+' |')
