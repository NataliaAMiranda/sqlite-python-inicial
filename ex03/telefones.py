# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ex03.base import Base


class Telefones(Base):
    __tablename__ = 'Telefones'

    idTelefone = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(String)
    idPessoa = Column(Integer, ForeignKey('Pessoa.idPessoa'))
    Pessoa = relationship("Pessoa", backref="Telefones")

    def __init__(self, numero, pessoa):
        self.numero = numero
        self.Pessoa = pessoa
