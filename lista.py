from tarefa import Tarefa
class To_do:
    def __init__(self):
        self.inicio_lista  = None # vai ser o inicio da lista
        self.final_lista = None # final da lista
        self.tamanho = 0 # tamanho 
    
   
    def vazia(self):
        if self.inicio_lista is None: # se  o inicio da lista é vazio então não existe lista
            return True
        return False

    def inserir_inicial(self, nova_tarefa):
        if self.vazia() is True:
            tarefa = Tarefa(nova_tarefa) 
            self.inicio_lista = self.final_lista = tarefa #define tanto o inicio quanto o final com a mesma tarefa porque só existe uma
            self.inicio_lista.proximo = self.final_lista #aponta que o próximo da lista vai ser o final da lista
            self.final_lista.anterior = self.inicio_lista # aponta que o inicio do final é o anterior
            print(f"Tarefa {self.inicio_lista.tarefa} adicionada a sua lista!")
            self.tamanho += 1
            


    def inserir_inicio(self, nova_tarefa): # lista [1]
        tarefa = Tarefa(nova_tarefa) # recebe a nova tarefa
        self.inicio_lista = tarefa #adiciona a nova tarefa inicio da lista
        self.inicio_lista.proximo = self.final_lista #coloca o primeiro elemento da lista agora como o próximo 
        self.tamanho +=1
        print(f"Tarefa {self.inicio_lista.tarefa} adicionada a sua lista!")

        
    
    def inserir_final(self, nova_tarefa): #[2,1]
        tarefa = Tarefa(nova_tarefa) # recebe a nova tarefa
        self.final_lista = tarefa #o ultimo número agora vira o anterior 
        self.final_lista.anterior = self.final_lista.tarefa # o ultimo agora é a próxima tarefa
        self.tamanho +=1
        print(f"Tarefa {self.final_lista.tarefa} adicionada a sua lista!")


    def excluir_inicio(self):
        self.inicio_lista = self.inicio_lista.proximo

        

    def excluir_final(self):
        self.final_lista = self.final_lista.anterior
    
    def deletar_lista(self):
        while self.tamanho != 0: 
            self.excluir_inicio()

    def alterar_tarefas(self,tarefa, tarefa_antes,tarefa_depois):
        altera = Tarefa(tarefa)
        altera.anterior = tarefa_antes
        altera.proximo = tarefa_depois
        tarefa_antes = altera
        tarefa_depois = altera
        return altera
    
    def printar_lista(self):
        lista = []
        temporario = self.inicio_lista
        for x in range(self.tamanho):
            lista.append(temporario.tarefa)
            temporario = temporario.proximo
        return print(lista)
                

