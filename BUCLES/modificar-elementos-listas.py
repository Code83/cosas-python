lista = [10,20,30,-10,-20,50]
i = 0
for n in lista:
    lista[i] = n + 1
    i = i + 1
print(lista)    

listaC = ['abd','def','ghi','jkl','nmñ']
i = 0

for x in listaC:
    listaC[i] = x + '-P'
    i = i + 1
print(listaC)    

for i in range (0,len(listaC),2):
    listaC[i] = "python"
print(listaC)    