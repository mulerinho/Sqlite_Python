import sqlite3



#Criando Uma tabela SqLite 
sql = 'create table clientes'\
      '(id interger primary key,'\
      'nome varchar(20)'\
      'idade int)'  

# Executando o comando sql.
ponteiro.execute(sql)

#Fechando conexão
conexao.close() 

#Confirmando:
print('DB SQlite criado com sucesso.')
