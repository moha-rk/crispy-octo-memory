#Arquivo com funções relacionadas à abertura, leitura e manipulação de arquivos

from os import listdir

def conteudo_dirertorio(path: str) -> list:
    """Recebe um caminho e devolve a lista de nomes de arquivos e pastas dentro desse caminho"""
    
    onlyfiles = [f for f in listdir(path)]
    return onlyfiles

def nomes_alunos_edisciplinas(path: str) -> list:
    """Recebe um caminho com pastas de trabalhos de alunos gerada pelo e-disciplinas
       e devolve a lista nomes dentro desse caminho"""
    
    onlyfiles = conteudo_dirertorio(path)
    names = []
    for name in onlyfiles:
        i = 0
        while (name[i] != '_'):
            i += 1
        names.append(name[0:i])
    return names

nome_do_trabalho = ''
lista_alunos = []

def set_nome_trabalho(nome: str) -> int:
    """Seta o nome do trabalho. Devolve 1 em caso de suesso, 
    0 em caso de falha (nome já existente, nome não permitido)"""

    if nome in conteudo_dirertorio("."):
        return 0

    if nome.find('/') != -1:
        return 0 

    global nome_do_trabalho
    nome_do_trabalho = nome

def get_nome_trabalho() -> str:
    return nome_do_trabalho

def nome_pasta() -> str:
    return f'./{get_nome_trabalho()}'

def nome_arquivo_chamada() -> str:
    return f'{nome_pasta()}/lista_chamada.txt'

def gera_lista_alunos(path_trabalhos: str, novo_trabalho: int) -> None:
    """Essa função deve ser chamada na criação de um novo trabalho (1) 
    passando na chamada o caminho da pasta contendo as pastas com nomes dos alunos
    ou na abertura de um trabalho (0), passando vazio em path_trabalhos (será ignorado)
    """
    global lista_alunos

    if novo_trabalho:
        lista_nome_alunos = nomes_alunos_edisciplinas(path_trabalhos)
        gera_arquivo_nomes_alunos(lista_nome_alunos)
        lista_alunos = [[aluno, []] for aluno in lista_nome_alunos]

    else:
        lista_alunos = le_lista_alunos_arquivo()


def gera_arquivo_nomes_alunos(nome_alunos) -> None:
    """Essa função gera o arquivo contendo os nomes dos alunos, 
    onde serão adicionados os descontos futuramente"""
    with open(nome_arquivo_chamada(), 'w') as f:
        for i in range (len(nome_alunos)):
            entry = f'{nome_alunos[i]}\n'
            f.write(entry)

def le_lista_alunos_arquivo() -> None:
    """Essa função lê o arquivo contendo a lista de alunos e guarda globalmente
       os nomes dos alunos junto de seus descontos (se existentes)"""
    lista_alunos = []
    with open(nome_arquivo_chamada(), 'r') as f:
        for line in f:
            line_split = line.split()
            if len(line_split) >= 1:
                entry = [line_split[0], []]
                for i in range (1, len(line_split)):
                    entry[1].append(int(line_split[i]))
                lista_alunos.append(entry)
    return lista_alunos

def adiciona_desconto(aluno: str, desconto: int) -> None:
    """Essa função recebe o nome do aluno a levar o desconto, e também recebe o número
       do desconto, alterando em memória e no arquivo. Trata adição de desconto repetido"""
    
    for a in lista_alunos:
        if a[0] == aluno:
            if not (desconto in a[1]):
                a[1].append(desconto)
                a[1].sort()
                #Atualizar a cada desconto feito.
                #Ineficiente, mas mais fácil para protótipo inicial
                atualiza_arquivo_chamada()
            break

def atualiza_arquivo_chamada() -> None:
    """Essa função deve ser chamada com a list lista_alunos atualizada
       e então escreverá seu conteúdo no arquivo"""
    with open(nome_arquivo_chamada(), 'w') as f:
        for i in range (len(lista_alunos)):
            str_descontos = ' '
            for desconto in lista_alunos[i][1]:
                str_descontos += f'{desconto} '
            str_descontos = str_descontos[:-1] #remove ultimo espaço em branco
            entry = f'{lista_alunos[i][0]}{str_descontos}\n'
            f.write(entry)