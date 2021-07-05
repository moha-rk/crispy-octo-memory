from arquivos import *

prompt = '>>> '

def imprime_estado_aluno(aluno):
    print(f"\nAluno:\n{aluno[0]}\nComentários:")
    for i_c in aluno[1]:
        l_com = devolve_comentario_e_desconto_por_indice(i_c)
        print(f"{l_com[0]} ({l_com[1]})")

def imprime_index_e_comentario(i, c):
    print(f"({i}) {c[0]} ({c[1]})")

def imprime_lista_comentarios(lista_comentarios):
    i = 0
    for c in lista_comentarios:
        imprime_index_e_comentario(i, c)
        i += 1

def imprime_lista_alunos(lista_alunos):
    print("\nLista de Alunos:")
    i = 0
    for aluno in lista_alunos:
        print(f'({i}) {aluno[0]}')
        i += 1