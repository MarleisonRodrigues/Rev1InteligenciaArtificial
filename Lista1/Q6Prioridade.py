import heapq
class Tarefas: 
    def init (self, descricao, prioridade):
        self.descricao=descricao
        self.prioridade=prioridade
    def setDescricao(self,descricao): 
        self.descricao=descricao
    def getDescricao(self):
        return self.descricao
    def setPrioridade(self, prioridade):
        self.prioridade=prioridade
    def getPrioridade(self):
       return self.prioridade
lista=[]
for i in range (0,3):
    x=input('Digite a descrição da tarefa {}: '.format(i+1))
    y=int(input('Digite a prioridade da tarefa {}: '.format(i+1)))
    while y>5 or y<0:
        y=int(input('INVALIDO, digite a prioridade da tarefa {}: '.format(i+1)))
    t=(x,y)
    heapq.heappush(lista,(y, x))
for i in range (0,3):
    print(heapq.heappop(lista))