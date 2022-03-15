# arquivo db.py

import sqlite3

# conecta ao banco de dados 'app'
# caso o banco não exista ele será criado
conn = sqlite3.connect("app.db")

# def add_filme(name,url):
#     conn.execute("insert into filme (name, url) values ("name.",".url.")")
#     conn.commit()

# def remove_filme(id):
#     """ remove o filme da tabela """
#     conn.execute("delete from tarefa where cd_tarefa = ?", (id, ))
#     conn.commit()

def get_filmes(): # retorna um cursor
    """ retorna a lista de filmes """
    return conn.execute("select id, name, url from filme;")