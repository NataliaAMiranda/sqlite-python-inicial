# -*- coding: utf-8 -*-

'''
Esse script ilustra um pequeno exemplo de uso da biblioteca sqlalchemy

mais informações em: https://www.sqlalchemy.org/

Dialeto do SQLAchemy para o SQLite:

https://docs.sqlalchemy.org/en/latest/dialects/sqlite.html

https://www.pythonsheets.com/notes/python-sqlalchemy.html

'''

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine("sqlite:///lab05-ex02.sqlite")
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session() # unidade de trabalho. Para garantir que todas alterações nos objetos em uma transação sejam persistidos

    # Fazendo  Mapeamento objeto relacional (Object Relational Mapper - ORM) com engenharia reversa - refletion
    # Será criada uma classe para cada tabela existente no banco de dados
    # https://docs.sqlalchemy.org/en/latest/orm/extensions/automap.html
    Base = automap_base()
    Base.prepare(engine, reflect=True)


    # Tabelas existentes no SQLLite
    Pessoa = Base.classes.Pessoa
    Telefones = Base.classes.Telefones


    # Listando todas pessoas
    pessoas = session.query(Pessoa).all()

    print("..: Todas pessoas :.. \nid\t nome")
    for pessoa in pessoas:
        print(f'{pessoa.idPessoa}\t {pessoa.nome}')

    # Listando todas pessoas com o nome iniciado com J
    pessoas = session.query(Pessoa).filter(Pessoa.nome.ilike('J%')).all()

    print("..: Todas pessoas com o nome iniciado por J:.. \nid\t nome")
    for pessoa in pessoas:
        print(f'{pessoa.idPessoa}\t {pessoa.nome}')

    # Listando somente as pessoas (e seus telefones) que possuem telefones
    # outra_forma = session.query(Pessoa).join(Telefones, Pessoa.idPessoa == Telefones.idPessoa).all()
    pessoas = session.query(Pessoa).join(Telefones).all()
    print("..: Todas pessoas :..")
    for linha in pessoas:
        print(f'{linha.idPessoa}\t {linha.nome}')
        for telefone in linha.telefones_collection:
            print(f"{telefone.numero}")


    print("Outra listagem")

    pessoas = session.query(Pessoa).all()
    for linha in pessoas:
        print(f'{linha.idPessoa}\t {linha.nome}')
        telefones = session.query(Telefones).filter(Telefones.idPessoa == linha.idPessoa)
        for tel in telefones:
            print(f'{tel.numero}')
