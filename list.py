import sqlite3

# Criando a conexão
conexao = sqlite3.connect('clientes.db')
ponteiro = conexao.cursor()

ponteiro.execute('select * from clientes')

#Recuperando resultados
retorno = ponteiro.fetchall()

#Apresentando
for i in retorno:
    print(i)

#Fechando conexão
conexao.close()