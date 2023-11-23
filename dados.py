import sqlite3

# Criando a conexão
conexao = sqlite3.connect('clientes.db')
ponteiro = conexao.cursor()

# comando para inserir dados
sql = 'insert into clientes values(null, ?,?)'

# Dados
gravando = [('Matilda', 12), ('Pituca', 8),('Nenny',1)]

# Laço para inserção
for i in gravando:
    ponteiro.execute(sql, i)

#Confirmando transação
conexao.commit()

#Fechando conexão
conexao.close()
