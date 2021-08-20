from arquivos import *
from modo_nota import *
from modo_correcao import *
from funcoes_impressao import *

def main():

    print("Seja bem-vindo ao suporte de correção.")
    state = 0

    try:
        while True:
            if state == 0:
                print("\nVocê deseja:\n(1) Criar um novo Trabalho\n(2) Abrir um trabalho existente\n(3) Encerrar a execução do programa")
                try:
                    com = int(input(prompt))
                except ValueError:
                    com = ''
                if com == 1:
                    nome_trabalho, lista_alunos, lista_comentarios, state = cria_trabalho()
                    
                elif com == 2:
                    nome_trabalho, lista_alunos, lista_comentarios, state = acessa_trabalho()
                    
                elif com == 3:
                    print("\nAdeus!")
                    return
                else:
                    print("\nComando inválido")
            elif state == 1:
                print(f"\nTrabalho {nome_trabalho} acessado! Você deseja:\n(1) Entrar no modo de Correção\n(2) Entrar no modo de Nota\n(3) Editar trabalho (exercícios, tópicos)\n(4) Sair para a tela inicial")
                try:
                    com = int(input(prompt))
                except ValueError:
                    com = ''
                if com == 1:
                    modo_correcao(lista_alunos, lista_comentarios)
                elif com == 2:
                    modo_nota(lista_alunos)
                elif com == 3:
                    edita_trabalho(nome_trabalho)
                elif com == 4:
                    fecha_trabalho()
                    state = 0
                else:
                    print("\nComando inválido")
    except KeyboardInterrupt:
        print()


def cria_trabalho():

    nome_trabalho = input("Digite o nome do Trabalho: ")
    while not set_nome_novo_trabalho(nome_trabalho):
        print(f"O projeto {nome_trabalho} não pôde ser criado")
        nome_trabalho = input("Digite o nome do Trabalho: ")
    cria_pasta()
    pasta_trabalhos = input("Digite o caminho contendo as pastas do Trabalho: ")
    lista_alunos = gera_lista_alunos(pasta_trabalhos, 1)
    lista_comentarios = le_comentarios_arquivo()
    state = 1

    return nome_trabalho, lista_alunos, lista_comentarios, state


def acessa_trabalho():
    nome_trabalho = input("\nDigite o nome do Trabalho: ")
    while not set_nome_trabalho_antigo(nome_trabalho):
        print(f"O projeto {nome_trabalho} não pôde ser aberto")
        nome_trabalho = input("Digite o nome do Trabalho: ")
    lista_alunos = gera_lista_alunos('', 0)
    lista_comentarios = le_comentarios_arquivo()
    state = 1

    return nome_trabalho, lista_alunos, lista_comentarios, state


def edita_trabalho(nome_trabalho):

    state = 0
    while True:
        if state == 0:
            print(f"Edição do trabalho {nome_trabalho}. Você deseja:\n(1) Alterar a nota máxima\n(2) Adicionar tópicos/exercícios\n(3) É um trabalho em grupo?\n(4) Retornar a tela anterior")
            try:
                com = int(input(prompt))
            except ValueError:
                com = ''
            
            if com == 1:
                pass
            elif com == 2:
                pass
            elif com == 3:
                com_interno = -1
                while com != 1 and com != 0:
                    print("\n(1)Sim\n(0)Não")
                    try:
                        com = int(input(prompt))
                    except ValueError:
                        com = -1

                set_trabalho_em_grupo(com)
                
            elif com == 4:
                return
            else:
                print("\nComando inválido")
    


main()