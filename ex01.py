from lista import To_do
def menu():  
    lista = To_do()

    try: 
        opcao_escolhida = int(input("Escolha entre: \n 1 -Inserir \n 2- Deleter \n 3 - Remover \n 4 - Alterar \n 5 - Sair \n >>> "))  
        if opcao_escolhida == 1:
            if lista.vazia() is True:
                lista.inserir_inicial(input("Opa! Parece que é a primeira vez que adiciona uma tarefa! \n Comece digitando uma nova tarefa:"))
            else:
                try:
                    escolha = int(input("Deseja colocar sua nova tarefa onde? \n 1-Inicio da lista \n 2-Final da lista"))
                    if escolha == 1:
                        lista.inserir_inicio(input("Digite aqui a tarefa:"))
                    elif escolha == 2:
                        lista.inserir_final(input("Digite aqui a tarefa:"))
                except ValueError:
                    print("Você não digitou algo válido!")
                              
        elif opcao_escolhida == 2:
            try:
                escolha = int(input("Deseja apagar sua tarefa do início ou do final da lista? \n 1-Inicio da lista \n 2-Final da lista"))
                if escolha == 1:
                    lista.excluir_inicio
                elif escolha == 2:
                    lista.excluir_final
            except ValueError:
                print("Você não digitou algo válido!")
            
        elif opcao_escolhida == 3:
            lista.deletar_lista()
        elif opcao_escolhida == 4:
            lista.alterar_tarefas(input("Digite a tarefa a ser alterada:", input("Digite a nova tarefa:")))
        elif opcao_escolhida == 5:
            exit()
    except ValueError():
         print("Você precisa digitar um número válido!")





teste = To_do()

teste.inserir_inicial("Tarefa 1")
teste.printar_lista()
teste.inserir_inicio("tarefa 2")
teste.inserir_final("tarefa 3")
teste.printar_lista()