tarefas = {}
id_tarefa = 1

while True:
    print('AGENDADOR DE TAREFAS')
    print ('''         
        [1] Adicionar Tarefa
        [2] Visualizar Tarefas
        [3] Remover Tarefa
        [4] Sair. ''')
    opcao = int(input('O que você deseja fazer ? '))

    if opcao == 1:
        desc_tarefa = input('Qual tarefa deseja adicionar ? ')
        tarefas[id_tarefa] = desc_tarefa
        print('Tarefa adicionada com sucesso!')
        print (f"{id_tarefa} => {tarefas[id_tarefa]}")
        id_tarefa += 1

    elif opcao == 2:
        if len(tarefas) == 0:
            print('Nenhuma tarefa cadastrada.')
        else:
            for id,desc in tarefas.items():
                print (id,desc)

    elif opcao ==3:
        id_tarefa = int(input('Qual o id da tarefa que você deseja remover ? '))
        if id_tarefa in tarefas:
            del tarefas[id_tarefa]
            print('Tarefa removida com sucesso! ')
        else: 
            print('Tarefa não encontrada.')
    elif opcao == 4:
        print('FIM')
        time.sleep(2)
        break 
    else: 
        print ("Opção inválida. Tente novamente ")
    print ("\n")
     