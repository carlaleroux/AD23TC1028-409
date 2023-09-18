f = open("/workspaces/AD23TC1028-409/5-Ciclos/alumnos.txt","r")

for linea in f:
    print(linea)

palabra = "ITESM CEM"

i=0
for letra in palabra:
    print(letra)
    i = i +1
print(i)

for i in range(5):
    for j in range (5,0,-1):
        print(i,j)
        if i == j:
            break
