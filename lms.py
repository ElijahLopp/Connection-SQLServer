# Linguagem de Programação II
# AC08 ADS2D - LMS
# alunos: nome1.sobrenome@aluno.faculdadeimpacta.com.br
#         nome2.sobrenome@aluno.faculdadeimpacta.com.br


from sqlalchemy import (create_engine, MetaData, Column, Integer, String,
                        ForeignKey, Date)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

# Setup do ambiente - Não é preciso alterar
load_dotenv()

# modifique o arquivo .env com os seus dados para realizar a conexão
user = os.environ.get("DB_USER")
pwd = os.environ.get("DB_PASS")
server = os.environ.get("DB_HOST")

engine = create_engine(f"mssql+pymssql://{user}:{pwd}@{server}/fit_alunos")
Base = declarative_base(bind=engine, metadata=MetaData(schema="lms"))

# Classes a serem criadas
# Crie todos os atributos (colunas) para as classes abaixo, e
# também  implemente o método __repr__


class Usuario(Base):
    '''
    Classe Usuario: mapeia a tabela usuário do Banco de dados
    '''
    __tablename__ = 'Usuario'
    idUse = Column('idUsuario', Integer, autoincrement=True, primary_key=True)
    Login = Column('idLogin', String(30), unique=True,  nullable=False)
    Senha = Column('Senha', String(30))
    DtExpiracao = Column('DtExpiracao', Date, default='19000101')
    alunos = relationship('Aluno', backref='Usuario')
    professor = relationship('Professor', backref='Usuario')
    Coordenador = relationship('Coordenador', backref='Usuario')

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f'<Usuario: {self.Login}>'


class Aluno(Base):
    '''
    Classe Aluno: mapeia a tabela Aluno do Banco de Dados
    possui um realacionamento com Usuario de nome usuario, e cria
    a backref perfil_aluno.
    '''
    __tablename__ = 'Aluno'
    idAl = Column('idAluno', Integer, autoincrement=True, primary_key=True)
    idusuario = Column('idUsuario', Integer,
                       ForeignKey('Usuario.idUse'),
                       nullable=False)
    Nome = Column('Nome', String(30), nullable=False)
    Email = Column('Email', String(50), unique=True, nullable=False)
    Celular = Column('Celular', String(14), unique=True, nullable=False)
    RA = Column('RA', Integer, nullable=False)

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Alunos: {self.Nome}>"


class Professor(Base):
    '''
    Classe Professor: mapeia a tabela Profesor do Banco de Dados
    possui um realacionamento com Usuario de nome usuario, e cria
    a backref perfil_professor.
    '''
    __tablename__ = 'Professor'
    idPr = Column('idProfessor', Integer, autoincrement=True, primary_key=True)
    idusuario = Column('idUsuario', Integer,
                       ForeignKey('Usuario.idUse'),
                       nullable=True)
    Email = Column('Email', String(50), nullable=False, unique=True)
    Celular = Column('Celular', String(14), nullable=False, unique=True)
    Apelido = Column('Apelido', String(15), nullable=False)

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Professor: {self.Apelido}>"


class Coordenador(Base):
    '''
    Classe Coordenador: mapeia a tabela Profesor do Banco de Dados
    Possui um realacionamento com Usuario, de nome usuario, e cria
    a backref perfil_coordenador.
    Possui um relaciomento com Disciplina de nome disciplinas e cria
    a backref coordenador.
    '''
    __tablename__ = 'Coordenador'
    idCo = Column('idCoordenador', Integer,
                  autoincrement=True,
                  primary_key=True)
    idusuario = Column('idUsuario', Integer,
                       ForeignKey('Usuario.idUse'),
                       nullable=False)
    Nome = Column('Nome', String(30), nullable=False)
    Email = Column('Email', String(50), nullable=False, unique=True)
    Celular = Column('Celular', String(14),
                     nullable=False,
                     unique=True)
    disciplina = relationship('Disciplina', backref='Coordenador')

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Coordenador: {self.Nome}>"


class Disciplina(Base):
    '''
    Classe Disciplina: mapeia a tabela Disciplina do Banco de Dados.
    Não é necessário colocar as restições das colunas: PercentualPrático,
    PercentualTeórico, CargaHoraria e StatusDisciplina
    '''
    __tablename__ = 'Disciplina'
    idDi = Column('idDisciplina', Integer,
                  autoincrement=True,
                  primary_key=True)
    Nome = Column('Nome', String(50), unique=True, nullable=False)
    DataDisciplina = Column('DataDisciplina', Date)
    StatusDisciplina = Column('StatusDisciplina', String(8))
    PlanoDeEnsino = Column('PlanoDeEnsino', String(500))
    CargaHoraria = Column('CargaHoraria', Integer, nullable=False)
    Competencias = Column('Competencias', String(500))
    Habilidades = Column('Habilidades', String(500))
    Ementa = Column('Ementa', String(500))
    idCoordenador = Column('idCoordenador', Integer,
                           ForeignKey('Coordenador.idCo'),
                           nullable=False)
    ConteudoProgramatico = Column('ConteudoProgramatico',
                                  String(500))
    BibliografiaBasica = Column('BibliografiaBasica',
                                String(500))
    BibliografiaComplementar = Column('BibliografiaComplementar',
                                      String(500))
    PercentualPratico = Column('PercentualPratico', Integer,
                               nullable=False)
    PercentualTeorico = Column('PercentualTeorico', Integer,
                               nullable=False)

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Disciplina: {self.Nome}>"


class Curso(Base):
    '''
    Classe Curso: mapeia a tabela Curso do Banco de Dados.
    '''
    __tablename__ = 'Curso'
    idCu = Column('idCurso', Integer,
                  autoincrement=True, primary_key=True)
    Nome = Column('Nome', String(50), nullable=False, unique=True)

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Curso: {self.Nome}>"


# with engine.connect() as conn:
#     rs = conn.execute('SELECT * FROM lms.Disciplina')
#     print(rs.keys())
