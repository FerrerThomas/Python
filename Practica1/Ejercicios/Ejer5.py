lista = []

print("Ingrese una lista de 10 numero")
for i in range(0,11):
    num = int(input("Nro: "))
    lista.append(num)
print("Lista cargada correctamente")

#longLista = len(lista)

for i in lista:
    if (i<0):
        print("Se encontro un numero negativo (",i,")")
        break
    else:
        print(i)

print("Temrineeee")