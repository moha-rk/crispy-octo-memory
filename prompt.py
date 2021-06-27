from os import stat
from arquivos import *

def main():

    print("Seja bem-vindo ao suporte de correção.")
    state = 0

    while True:
        if state == 0:
            print("Você deseja:\n(1) Criar um novo Trabalho\n(2) Abrir um trabalho existente")
            com = int(input())
            if com == 1:
                nome_trabalho = input("Digite o nome do Trabalho: ")
                while not set_nome_novo_trabalho(nome_trabalho):
                    print(f"O projeto {nome_trabalho} não pôde ser criado")
                    nome_trabalho = input("Digite o nome do Trabalho: ")
                cria_pasta()
                pasta_trabalhos = input("Digite o caminho contendo as pastas do Trabalho: ")
                lista_alunos = gera_lista_alunos(pasta_trabalhos, 1)
                lista_comentarios = le_comentarios_arquivo()
                state = 1
            elif com == 2:
                nome_trabalho = input("Digite o nome do Trabalho: ")
                set_nome_trabalho_antigo(nome_trabalho)
                lista_alunos = gera_lista_alunos('', 0)
                lista_comentarios = le_comentarios_arquivo()
                state = 1
            else:
                print("Comando inválido")
        elif state == 1:
            print(f"Trabalho {nome_trabalho} acessado! Você deseja:\n(1) Entrar no modo de Correção\n(2) Entrar no modo de Nota\n(3) Sair para a tela inicial")
            com = int(input())
            if com == 1:
                modo_correcao(lista_alunos, lista_comentarios)
            elif com == 2:
                modo_nota()
            elif com == 3:
                state = 0
            else:
                print("Comando inválido")




def modo_correcao(lista_alunos, lista_comentarios):

    state = 0
    while True:
        if state == 0:
            print("Modo de Correção. Você deseja:\n(1) Mostrar os alunos por ordem alfabética\n(2) Selecionar um aluno específico\n(3) Voltar à tela anterior")
            com = int(input())
            if com == 1:
                state = 1
                n_alunos = len(lista_alunos)
            elif com == 2:
                state = 2
            elif com == 3:
                break
            else:
                print("Comando inválido")
        elif state == 1:
            for aluno in lista_alunos:
                if state == 0:
                    break
                continuar = False
                while not continuar:
                    print(f"Aluno:\n{aluno[0]}\nComentários:")
                    for i_c in aluno[1]:
                        l_com = devolve_comentario_e_desconto_por_indice(i_c)
                        print(f"{l_com[0]} ({l_com[1]})")
                    print("Você deseja:\n(1) Adicionar um novo comentário\n(2) Adicionar um comentário existente\n(3) Remover um comentário\n(4) Passar para o próximo aluno\n(5) Voltar à tela anterior")
                    com = int(input())
                    if com == 1:
                        coment = input("Digite o comentário: ")
                        if coment[-1] != '.':
                            coment += '.'
                        desconto = int(input("Desconto (0 caso ainda não possua um valor): "))
                        if desconto > 0:
                            desconto = -desconto
                        adiciona_comentario(aluno[0], coment, desconto)
                    elif com == 2:
                        i = 0
                        for c in lista_comentarios:
                            print(f"({i}) {c[0]} ({c[1]})")
                            i += 1
                        coment = int(input("Digite o índice do comentário: "))
                        adiciona_desconto(aluno[0], coment)
                    elif com == 3:
                        #Remove comentário
                        print("Precisa fazer a função ainda")
                        pass
                    elif com == 4:
                        continuar = True
                    elif com == 5:
                        state = 0
                        break
                    else:
                        print("Comando inválido")



def modo_nota():
    pass

main()