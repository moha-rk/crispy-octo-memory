from funcoes_impressao import *
from arquivos import *

def modo_correcao(lista_alunos, lista_comentarios):

    state = 0
    while True:
        if state == 0:
            print("\nModo de Correção. Você deseja:\n(1) Mostrar os alunos por ordem alfabética\n(2) Selecionar um aluno específico\n(3) Voltar à tela anterior")
            try:
                com = int(input(prompt))
            except ValueError:
                com = ''
            if com == 1:
                state = 1
            elif com == 2:
                state = 2
            elif com == 3:
                return
            else:
                print("\nComando inválido")

        elif state == 1:
            avalia_ordem_alfabetica()
            state = 0

        elif state == 2:
            avalia_individual()
            state = 0

def avalia_aluno(lista_comentarios: list, aluno: list, individual: int) -> int:

    continuar = False
    while not continuar:
        imprime_estado_aluno(aluno)

        print("\nVocê deseja:\n(1) Adicionar um novo comentário\n(2) Adicionar um comentário existente\n(3) Remover um comentário")
        if individual:
            print("(4) Voltar à tela anterior")
        else:
            print("(4) Passar para o próximo aluno\n(5) Voltar à tela anterior")

        try:
            com = int(input(prompt))
        except ValueError:
            com = 0

        if com == 1:
            coment = input("\nDigite o comentário: ")
            if coment[-1] != '.':
                coment += '.'
            
            desconto = -1
            while desconto < 0:
                try:
                    desconto = float(input("Desconto (0 caso ainda não possua um valor): "))
                except:
                    desconto = -1

            if desconto > 0:
                desconto = -desconto
            adiciona_comentario(aluno[0], coment, desconto)

        elif com == 2:
            imprime_lista_comentarios(lista_comentarios)
            try:
                coment = int(input("\nDigite o índice do comentário: "))
            except ValueError:
                coment = -1
            adiciona_desconto(aluno[0], coment)

        elif com == 3:
            print("\nComentários:")

            lista_indices_comentarios = aluno[1]
            lista_comentarios_aluno = []

            for i_c in lista_indices_comentarios:
                lista_comentarios_aluno.append(devolve_comentario_e_desconto_por_indice(i_c))
            imprime_lista_comentarios(lista_comentarios_aluno)
            
            try:
                coment = int(input("\nDigite o índice do comentário: "))
            except ValueError:
                coment = -1
            remove_desconto(aluno[0], lista_indices_comentarios[coment])

        elif com == 4 and not individual:
            continuar = True
            state_interno = 1

        elif com == 4 or (com == 5 and not individual):
            state_interno = 0
            continuar = True
        
        else:
            print("\nComando inválido")
    return state_interno


def avalia_ordem_alfabetica(lista_alunos, lista_comentarios):

    for aluno in lista_alunos:
        continuar = avalia_aluno(lista_comentarios, aluno, 0)
        if continuar == 0:
            break
    return

def avalia_individual(lista_alunos, lista_comentarios):
    imprime_lista_alunos(lista_alunos)

    try:
        i_aluno = int(input("\nSelecione o índice do aluno: "))
    except ValueError:
        i_aluno = -1

    while i_aluno < 0 or i_aluno >= len(lista_alunos):
        print("Índice incorreto")
        try:
            i_aluno = int(input("\nSelecione o índice do aluno: "))
        except ValueError:
            i_aluno = -1

    aluno = lista_alunos[i_aluno]
    avalia_aluno(lista_comentarios, aluno, 1)