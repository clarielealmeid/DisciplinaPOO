from casa import *
import argparse

casa = CasaInteligente(5) #Definindo um máximo de 5 dispositivos que podem ser criados
fabrica = DispositivoFactory()
system = True

while system:
    print("Casa Inteligente\n"
            "[1] Criar Dispositivo\n"
            "[2] Administrar Seus Dispositivos\n"
            "[3] Obter Status de Todos os Dispositivos\n"
            "[4] Desligar Todas as Luzes\n"
            "[5] Listar Dispositivos Ligados\n"
            "[6] Contar Dispositivos Ligados\n"
            "[7] Configurar Limite de Dispositivos\n"
            "[8] Sair")
    
    choice1 = input("Escolha uma opção: ")

    if choice1 == '1':
        print("Qual dispositivo você quer criar?\n"
                "[1] Luz\n"
                "[2] Termostato\n"
                "[3] Sistema de Segurança")
        
        choice2 = input("Escolha uma opção: ")
        if choice2 == '1':
            luz = fabrica.criar_dispositivo('Luz')
            casa.adicionar_dispositivo(luz)
            observador = EstadoDispositivoObserver()
            luz.adicionar_observador(observador)
            print("Luz criada com sucesso\n")
        
        elif choice2 == '2':
            temperatura_inicial = input("Digite a temperatura inicial: ")
            termostato = fabrica.criar_dispositivo('Termostato', int(temperatura_inicial))
            casa.adicionar_dispositivo(termostato)
            observador = EstadoDispositivoObserver()
            termostato.adicionar_observador(observador)
            print("Termostato criado com sucesso\n")

        elif choice2 == '3':
            sistema_seguranca = fabrica.criar_dispositivo('SistemaSeguranca')
            casa.adicionar_dispositivo(sistema_seguranca)
            observador = EstadoDispositivoObserver()
            sistema_seguranca.adicionar_observador(observador)
            print("Sistema de Segurança criado com sucesso\n")

    elif choice1 == '2':
        print("Seus dispositivos:")
        casa.listar_dispositivos()

        choice3 = input("Escolha o índice do dispositivo para administrar:\n")
        dispositivo_indice = int(choice3)
        dispositivo = casa.dispositivos[dispositivo_indice]

        if isinstance(dispositivo, Luz):
            print("Qual a ação desejada?\n"
                    "[1] Ligar a luz\n"
                    "[2] Desligar a luz\n"
                    "[3] Excluir dispositivo")
            
            choice4 = input("Escolha uma opção:\n")

            if choice4 == '1':
                dispositivo.ligar()
                print("Luz ligada\n")
            
            elif choice4 == '2':
                dispositivo.desligar()
                print("Luz desligada\n")
            
            elif choice4 == '3':
                casa.remover_dispositivo(dispositivo)
                print("Luz removida\n")

        elif isinstance(dispositivo, Termostato):
            print("Qual a ação desejada?\n"
                    "[1] Aquecer ambiente\n"
                    "[2] Resfriar ambiente\n"
                    "[3] Desligar Termostato\n"
                    "[4] Excluir dispositivo")
            
            choice5 = input("Escolha uma opção:\n")

            if choice5 == '1':
                dispositivo.aquecer()
                print("Aquecendo ambiente\n")
            
            elif choice5 == '2':
                dispositivo.esfriar()
                print("Esfriando ambiente\n")
            
            elif choice5 == '3':
                dispositivo.desligar()
                print("Termostato desligado\n")
            
            elif choice5 == '4':
                casa.remover_dispositivo(dispositivo)
                print("Termostato removido\n")

            else:
                print("Opção indisponível")

        elif isinstance(dispositivo, SistemaSeguranca):
            print("Qual a ação desejada?\n"
                    "[1] Armar sistema de segurança com gente em casa\n"
                    "[2] Armar sistema de segurança sem ninguém em casa\n"
                    "[3] Desarmar sistema de segurança\n"
                    "[4] Excluir dispositivo")
            
            choice6 = input("Escolha uma opção:\n")

            if choice6 == '1':
                dispositivo.armar_com_gente_em_casa()
                print("Sistema de segurança armado\n")
            
            elif choice6 == '2':
                dispositivo.armar_sem_ninguem_em_casa()
                print("Sistema de segurança armado\n")
            
            elif choice6 == '3':
                dispositivo.desarmar()
                print("Sistema de segurança desarmado\n")
            
            elif choice6 == '4':
                casa.remover_dispositivo(dispositivo)
                print("Sistema de segurança removido\n")

            else:
                print("Opção indisponível\n")

    elif choice1 == '3':
        print("Status de todos os dispositivos:\n")
        for status in casa.obter_status_todos_dispositivos():
            print(status)

    elif choice1 == '4':
        casa.desligar_todas_luzes()
        print("Todas as luzes foram desligadas\n")

    elif choice1 == '5':
        print("Dispositivos ligados:\n")
        for dispositivo in casa.obter_dispositivos_ligados():
            print(dispositivo.obter_status())

    elif choice1 == '6':
        total_ligados = casa.contar_dispositivos_ligados()
        print(f"Total de dispositivos ligados: {total_ligados}\n")

    elif choice1 == '7':
        novo_limite = int(input("Digite o novo limite de dispositivos:"))
        casa.set_max_dispositivos(novo_limite)
        print(f"Limite de dispositivos atualizado")
        
    elif choice1 == '8':
        system = False
    
    else:
        print("Escolha inválida\n")

