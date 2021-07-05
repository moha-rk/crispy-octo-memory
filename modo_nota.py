from funcoes_impressao import *
from arquivos import *

def modo_nota(lista_alunos):
    nota_maxima = 10

    state = 0
    while True:
        if state == 0:
            print("\nModo de Nota. Você deseja:\n(1) Mostrar os alunos por ordem alfabética\n(2) Selecionar um aluno específico\n(3) Voltar à tela anterior")
            try:
                com = int(input(prompt))
            except ValueError:
                com = ''
            if com == 1:
                state = 1
            elif com == 2:
                state = 2
            elif com == 3:
                break
            else:
                print("\nComando inválido")

        elif state == 1:
            mostra_notas_ordem_alfabetica(lista_alunos, nota_maxima)
            state = 0

        elif state == 2:
            mostra_nota_individual(lista_alunos, nota_maxima)
            state = 0


def mostra_notas_ordem_alfabetica(lista_alunos, nota_maxima):

    for aluno in lista_alunos:
        nota_aluno(aluno, nota_maxima)
        com = input("\nPara continuar, dê um Enter. Para sair, digite 0: ")
        if com == '0':
            return

def mostra_nota_individual(lista_alunos, nota_maxima):
    imprime_lista_alunos(lista_alunos)

    i_aluno = -1
    while i_aluno < 0 or i_aluno >= len(lista_alunos):
        try:
            i_aluno = int(input("\nSelecione o índice do aluno: "))
        except ValueError:
            i_aluno = -1

    aluno = lista_alunos[i_aluno]
    nota_aluno(aluno, nota_maxima)


def nota_aluno(aluno: list, nota_maxima: int) -> None:
    nota_final = 10
    for desconto_indice in aluno[1]:
        nota_final += devolve_desconto_por_indice(desconto_indice)
    print(f"\nAluno: {aluno[0]}\nNota: {nota_final}\nComentários:")
    for desconto_indice in aluno[1]:
        print(f"{devolve_comentario_por_indice(desconto_indice)} ({devolve_desconto_por_indice(desconto_indice)})")