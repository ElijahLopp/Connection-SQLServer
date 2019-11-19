# Linguagem de Programação II
# AC09 ADS2D - Querys LMS
# alunos: elias.dias@aluno.faculdadeimpacta.com.br
#         leonardo.perez@aluno.faculdadeimpacta.com.br

from lms import (engine, Usuario, Aluno, Professor,
                 Coordenador, Disciplina, Curso)
from sqlalchemy.orm import sessionmaker
from typing import List, Dict

# Setup: não alterar
Session = sessionmaker(engine)
ses = Session()

# Funções de Query para implementar


def lista_logins() -> List[str]:
    '''
    retorna uma lista com todos os logins de Usuarios presentes no banco.
    '''
    login = ses.query(Usuario.login).all()
    lst = []
    for nomelogin in login:
        lst.append(nomelogin[0])
    return lst


def lista_alunos() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os Alunos do banco.
    '''
    nomes = ses.query(Aluno.nome).all()
    lst = []
    for nomealu in nomes:
        lst.append(nomealu[0])
    return lst


def lista_cursos() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os Cursos do banco.
    '''
    cursos = ses.query(Curso.nome).all()
    lst = []
    for nomecur in cursos:
        lst.append(nomecur[0])
    return lst


def lista_professores() -> List[str]:
    '''
    retorna uma lista com os apelidos de todos os professores do banco.
    '''
    apelido = ses.query(Professor.apelido).all()
    lst = []
    for nomeap in apelido:
        lst.append(nomeap[0])
    return lst


def lista_coordenadores() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os coordenadores do banco.
    '''
    nmecoo = ses.query(Coordenador.nome).all()
    lst = []
    for name in nmecoo:
        lst.append(name[0])
    return lst


def lista_disciplinas() -> List[str]:
    '''
    retorna uma lista com o nome de todas as Discplinas do banco.
    '''
    nmdisc = ses.query(Disciplina.nome).all()
    lst = []
    for name in nmdisc:
        lst.append(name[0])
    return lst


def carga_horaria_total() -> int:
    '''
    retorna a soma da carga horária de todas as diciplinas do banco
    '''
    somacarga = ses.query(Disciplina.carga_horaria).all()
    soma = 0
    for valor in somacarga:
        soma += valor[0]
    return soma


def monta_coordenadores() -> Dict[str, List[str]]:
    '''
    Retorna um dicionario cujo as chaves são os nome dos
    coordenadores, e o valor é uma lista com os nomes das
    disciplinas que ele coordena. Caso um professor não coordene
    nenhuma diciplina o valor é uma lista vazia.
    '''
    # num = 1
    # tamanho_da_lista_dos_nomes = int(len(ses.query(Coordenador.nome).all()))
    # dictt = {}
    # lst = []
    # while num <= tamanho_da_lista_dos_nomes:
    #     coor = ses.query(Coordenador).get(num)
    #     if coor.disciplina == []:
    #         lst = []
    #         dictt[coor.nome] = lst
    #     else:
    #         for x in range(int(len(coor.disciplina))):
    #             lst.append(coor.disciplina[x])
    #             dictt[coor.nome] = lst
    #     num += 1
    # return dictt
    resumo_coordenador = {}
    lista_coor = lista_coordenadores()
    for x in range(len(lista_coor)):
        q = ses.query(Coordenador).get(x+1)
        if q.disciplina == []:
            resumo_coordenador[q.nome] = []
        for y in range(len(q.disciplina)):
            resumo_coordenador[q.nome] = [q.disciplina[y]]
    return resumo_coordenador


if __name__ == '__main__':
    # Use esta área para testar sua funções, compare o resultado
    # obtido aqui com o feito direto com SELECT no SQL SERVER
    print(monta_coordenadores())
