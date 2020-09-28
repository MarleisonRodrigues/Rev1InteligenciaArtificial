matriz=[]
for i in range (0,4):
    local=[]
    for i in range(0,4):
        local.append(int(input('Digite um número:')))
    matriz.append(local)
for i in range (0,4):
    print(matriz[i])