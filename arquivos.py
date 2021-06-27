#Arquivo com funções relacionadas à abertura, leitura e manipulação de arquivos

from os import mkdir, listdir

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
    names.sort()
    return names

nome_do_trabalho = ''
lista_alunos = []
lista_comentarios = []

def set_nome_novo_trabalho(nome: str) -> int:
    """Seta o nome do trabalho. Devolve 1 em caso de suesso, 
    0 em caso de falha (nome já existente, nome não permitido)"""

    if nome in conteudo_dirertorio("."):
        return 0

    if nome.find('/') != -1:
        return 0 

    global nome_do_trabalho
    nome_do_trabalho = nome

    return 1

def set_nome_trabalho_antigo(nome: str) -> int:
    """Seta o nome do trabalho. Devolve 1 em caso de suesso, 
    0 em caso de falha (nome não existente)"""

    if not (nome in conteudo_dirertorio(".")):
        return 0

    global nome_do_trabalho
    nome_do_trabalho = nome

    return 1    

def cria_pasta() -> None:
    mkdir(nome_pasta())

def get_nome_trabalho() -> str:
    return nome_do_trabalho

def nome_pasta() -> str:
    return f'./{get_nome_trabalho()}'

def nome_arquivo_chamada() -> str:
    return f'{nome_pasta()}/lista_chamada.txt'

def nome_arquivo_coments() -> str:
    return f'{nome_pasta()}/comentarios.txt'

def gera_lista_alunos(path_trabalhos: str, novo_trabalho: int) -> list:
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

    return lista_alunos


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
            line = line.strip('\n')
            i = 0
            while i < len(line) and not line[i].isnumeric():
                i += 1
            if i == len(line):
                entry = [line, []]
                lista_alunos.append(entry)
            else:
                numeros = line[i:].split()
                for n in range(len(numeros)):
                    numeros[n] = int(numeros[n])
                entry = [line[:i-1], numeros]
                lista_alunos.append(entry)
    return lista_alunos

def adiciona_desconto(aluno: str, desconto: int) -> None:
    """Essa função recebe o nome do aluno a levar o desconto, e também recebe o número
       do desconto, alterando em memória e no arquivo. Trata adição de desconto repetido"""
    global lista_alunos
    for i in range (len(lista_alunos)):
        if lista_alunos[i][0] == aluno:
            if not (desconto in lista_alunos[i][1]):
                lista_alunos[i][1].append(desconto)
                lista_alunos[i][1].sort()
                #Atualizar a cada desconto feito.
                #Ineficiente, mas mais fácil para protótipo inicial
                atualiza_arquivo_chamada(lista_alunos)
            break

def atualiza_arquivo_chamada(lista_alunos: list) -> None:
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

def le_comentarios_arquivo() -> list:
    """Devolve uma lista de comentários, onde o índice do comentário equivale ao seu código"""
    global lista_comentarios
    lista_comentarios = []
    try:
        with open(nome_arquivo_coments(), 'r') as f:
            for line in f:
                line = line.strip('\n')
                entry = []
                if line[-1] == '.':
                    entry = [line, None]
                else:
                    size_desconto = 1
                    while size_desconto < len(line) and line[-size_desconto] != '(':
                        size_desconto += 1
                    desconto = int(line[len(line)-size_desconto+1: -1])
                    entry = [line[:-size_desconto-1], desconto]
                lista_comentarios.append(entry)

    except FileNotFoundError:
        open(nome_arquivo_coments(), 'w')
    
    return lista_comentarios

def adiciona_comentario(aluno: str, comentario: str, valor_desconto: int) -> list:
    global lista_comentarios

    for coment in lista_comentarios:
        if coment[0] == comentario:
            print("Comentário já existente")
            return
    
    if valor_desconto == 0:
        valor_desconto = None
    lista_comentarios.append([comentario, valor_desconto])
    adiciona_desconto(aluno, len(lista_comentarios)-1)
    atualiza_arquivo_comentario()


def atualiza_desconto_comentario(comentario: str, desconto: int) -> list:
    """Recebe um comentario e o novo desconto atrelado a este comentario,
       atualiza a lista global e a devolve"""
    global lista_comentarios
    if desconto > 0:
        desconto = -desconto
    
    for i in range (len(lista_comentarios)):
        if lista_comentarios[i][0] == comentario:
            lista_comentarios[i][1] = desconto
            #Atualizar a cada desconto feito.
            #Ineficiente, mas mais fácil para protótipo inicial
            atualiza_arquivo_comentario(lista_comentarios)
            break

def atualiza_arquivo_comentario() -> None:
    """Essa função deve ser chamada com a list lista_comentarios atualizada
       e então escreverá seu conteúdo no arquivo"""
    with open(nome_arquivo_coments(), 'w') as f:
        for i in range (len(lista_comentarios)):
            if lista_comentarios[i][1]:
                entry = f'{lista_comentarios[i][0]} ({lista_comentarios[i][1]})\n'
            else:
                entry = f'{lista_comentarios[i][0]}\n'
            f.write(entry)

def devolve_comentario_e_desconto_por_indice(index: int) -> list:
    #return lista_comentarios[index+1]
    return lista_comentarios[index]

def devolve_comentario_por_indice(index: int) -> str:
    #return lista_comentarios[index+1][0]
    return lista_comentarios[index][0]

def devolve_desconto_por_indice(index: int) -> int:
    #return lista_comentarios[index+1][1]
    return lista_comentarios[index][1]

#def remove_comentario(index: int, coment: str) -> None:
