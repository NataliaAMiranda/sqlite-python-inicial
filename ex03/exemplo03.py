# -*- coding: utf-8 -*-

'''
Esse script ilustra um pequeno exemplo de uso da biblioteca sqlalchemy

Esse exemplo criará o esquema do banco

https://www.pythonsheets.com/notes/python-sqlalchemy.html
'''


from ex03.base import Session, engine, Base
from ex03.pessoa import Pessoa
from ex03.telefones import Telefones

# gerando o esquema do banco de dados
Base.metadata.create_all(engine)

def populando_base():

    session = Session()

    # Criando objeto pessoas
    juca = Pessoa("Juca")
    ana = Pessoa("Ana")
    pedro = Pessoa("Pedro")
    julia = Pessoa("Julia")

    # Persistindo dados
    session.add(juca)
    session.add(ana)
    session.add(pedro)
    session.add(julia)

    # Adicionando telefone
    juca_telefone_casa = Telefones("48 3332-1222", juca)
    juca_telefone_celular = Telefones("48 99999-1234", juca)
    ana_telefone = Telefones("49 91313-1213",ana)

    # Persistindo dados
    session.add(juca_telefone_casa)
    session.add(juca_telefone_celular)
    session.add(ana_telefone)


    # Efetivando a persistência
    session.commit()
    # fechando a conexão
    session.close()


def listando_pessoas():
    session = Session()
    # Listando somente as pessoas (e seus telefones) que possuem telefones
    pessoas = session.query(Pessoa).join(Telefones).all()
    print("..: Todas pessoas :..")
    for pessoa in pessoas:
        print(f'{pessoa.idPessoa}\t {pessoa.nome}')
        for telefone in pessoa.Telefones:
            print(f"{telefone.numero}")

    session.close()


if __name__ == '__main__':
    # Populando base
    # populando_base()
    listando_pessoas()





