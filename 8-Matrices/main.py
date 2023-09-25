def lectura_archivo(datos):
    f = open("/workspaces/AD23TC1028-409/8-Matrices/"+ datos)
    matriz = []
    for linea in f:
        linea = linea [0:-1] #quitar retorno de carro enter
        linea = linea.split(",") #separar numeros en comas 
        matriz .append(linea)
    return (matriz)

def calcula_transpuesta(matriz):
    transpuesta=[]
    for j in range (len(matriz[0])):
        lista =[]
        for i in range (len(matriz)):
            lista.append(matriz[i][j]) #moverse en matriz 
        transpuesta.append (lista)
    return (transpuesta)


def main():
    pass
    mat = lectura_archivo("datos.txt")
    trans = calcula_transpuesta (mat)
    print (mat)
    print (trans)

if __name__ == "__main__":
    main()