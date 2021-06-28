from arquivos import *

def main():

    print("Seja bem-vindo ao suporte de correção.")
    state = 0

    try:
        while True:
            if state == 0:
                print("\nVocê deseja:\n(1) Criar um novo Trabalho\n(2) Abrir um trabalho existente\n(3) Encerrar a execução do programa")
                com = int(input())
                if com == 1:
                    nome_trabalho = input("\nDigite o nome do Trabalho: ")
                    while not set_nome_novo_trabalho(nome_trabalho):
                        print(f"O projeto {nome_trabalho} não pôde ser criado")
                        nome_trabalho = input("Digite o nome do Trabalho: ")
                    cria_pasta()
                    pasta_trabalhos = input("Digite o caminho contendo as pastas do Trabalho: ")
                    lista_alunos = gera_lista_alunos(pasta_trabalhos, 1)
                    lista_comentarios = le_comentarios_arquivo()
                    state = 1
                elif com == 2:
                    nome_trabalho = input("\nDigite o nome do Trabalho: ")
                    while not set_nome_trabalho_antigo(nome_trabalho):
                        print(f"O projeto {nome_trabalho} não pôde ser aberto")
                        nome_trabalho = input("Digite o nome do Trabalho: ")
                    lista_alunos = gera_lista_alunos('', 0)
                    lista_comentarios = le_comentarios_arquivo()
                    state = 1
                elif com == 3:
                    print("\nAdeus!")
                    break
                else:
                    print("\nComando inválido")
            elif state == 1:
                print(f"\nTrabalho {nome_trabalho} acessado! Você deseja:\n(1) Entrar no modo de Correção\n(2) Entrar no modo de Nota\n(3) Sair para a tela inicial")
                com = int(input())
                if com == 1:
                    modo_correcao(lista_alunos, lista_comentarios)
                elif com == 2:
                    modo_nota(lista_alunos, lista_comentarios)
                elif com == 3:
                    state = 0
                else:
                    print("\nComando inválido")
    except KeyboardInterrupt:
        print()




def modo_correcao(lista_alunos, lista_comentarios):

    state = 0
    while True:
        if state == 0:
            print("\nModo de Correção. Você deseja:\n(1) Mostrar os alunos por ordem alfabética\n(2) Selecionar um aluno específico\n(3) Voltar à tela anterior")
            com = int(input())
            if com == 1:
                state = 1
                n_alunos = len(lista_alunos)
            elif com == 2:
                state = 2
            elif com == 3:
                break
            else:
                print("\nComando inválido")
        elif state == 1:
            for aluno in lista_alunos:
                if state == 0:
                    break
                state = avalia_aluno(lista_comentarios, aluno, 0)
        elif state == 2:
            print("\nLista de Alunos:")
            i = 0
            for aluno in lista_alunos:
                print(f'({i}) {aluno[0]}')
                i += 1
            i_aluno = int(input("\nSelecione o índice do aluno: "))
            aluno = lista_alunos[i_aluno]
            state = avalia_aluno(lista_comentarios, aluno, 1)
            

def avalia_aluno(lista_comentarios: list, aluno: list, individual: int) -> int:

    continuar = False
    while not continuar:
        print(f"\nAluno:\n{aluno[0]}\nComentários:")
        for i_c in aluno[1]:
            l_com = devolve_comentario_e_desconto_por_indice(i_c)
            print(f"{l_com[0]} ({l_com[1]})")
        print("\nVocê deseja:\n(1) Adicionar um novo comentário\n(2) Adicionar um comentário existente\n(3) Remover um comentário")
        if individual:
            print("(4) Voltar à tela anterior")
        else:
            print("(4) Passar para o próximo aluno\n(5) Voltar à tela anterior")
        com = int(input())
        if com == 1:
            coment = input("\nDigite o comentário: ")
            if coment[-1] != '.':
                coment += '.'
            desconto = float(input("Desconto (0 caso ainda não possua um valor): "))
            if desconto > 0:
                desconto = -desconto
            adiciona_comentario(aluno[0], coment, desconto)
        elif com == 2:
            i = 0
            for c in lista_comentarios:
                print(f"({i}) {c[0]} ({c[1]})")
                i += 1
            coment = int(input("\nDigite o índice do comentário: "))
            adiciona_desconto(aluno[0], coment)
        elif com == 3:
            print("\nComentários:")
            i = 0
            for i_c in aluno[1]:
                l_com = devolve_comentario_e_desconto_por_indice(i_c)
                print(f"({i}) {l_com[0]} ({l_com[1]})")
                i += 1
            coment = int(input("\nDigite o índice do comentário: "))
            remove_desconto(aluno[0], coment)
        elif com == 4 and not individual:
            continuar = True
            state_interno = 1
        elif com == 4 or (com == 5 and not individual):
            state_interno = 0
            continuar = True
        else:
            print("\nComando inválido")
    return state_interno


def modo_nota(lista_alunos, lista_comentarios):
    nota_maxima = 10

    state = 0
    while True:
        if state == 0:
            print("\nModo de Nota. Você deseja:\n(1) Mostrar os alunos por ordem alfabética\n(2) Selecionar um aluno específico\n(3) Voltar à tela anterior")
            com = int(input())
            if com == 1:
                state = 1
                n_alunos = len(lista_alunos)
            elif com == 2:
                state = 2
            elif com == 3:
                break
            else:
                print("\nComando inválido")
        elif state == 1:
            for aluno in lista_alunos:
                if state == 0:
                    break
                nota_aluno(aluno, nota_maxima)
                com = input("\nPara continuar, dê um Enter. Para sair, digite 0: ")
                if com == '0':
                    state = 0
        elif state == 2:
            print("\nLista de Alunos:")
            i = 0
            for aluno in lista_alunos:
                print(f'({i}) {aluno[0]}')
                i += 1
            i_aluno = int(input("\nSelecione o índice do aluno: "))
            aluno = lista_alunos[i_aluno]
            nota_aluno(aluno, nota_maxima)
            state = 0


def nota_aluno(aluno: list, nota_maxima: int) -> None:
    nota_final = 10
    for desconto_indice in aluno[1]:
        nota_final += devolve_desconto_por_indice(desconto_indice)
    print(f"\nAluno: {aluno[0]}\nNota: {nota_final}\nComentários:")
    for desconto_indice in aluno[1]:
        print(f"{devolve_comentario_por_indice(desconto_indice)} ({devolve_desconto_por_indice(desconto_indice)})")

main()