# -*- coding: utf-8 -*-

'''
Esse script ilustra um pequeno exemplo de uso da biblioteca sqlite3

mais informações em: https://docs.python.org/3/library/sqlite3.html

'''

import sqlite3

if __name__ == '__main__':

    conexao = sqlite3.connect('lab05-ex01.sqlite')

    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM Pessoa')
    print(cursor.fetchall())



    pessoa = ('Juca',)

    cursor.execute("SELECT * FROM Pessoa WHERE nome = ? ", pessoa)

    for linha in cursor.fetchall():
        print("Id: {}, nome: {}".format(linha[0], linha[1]))


    cursor.close()
    conexao.close()