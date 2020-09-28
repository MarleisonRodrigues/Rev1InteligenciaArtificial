from collections import deque
fila=deque([])
for i in range(0,10):
    fila.append(int(input('Digite um número: ')))
for i in range(0,10):
    print(fila.popleft())