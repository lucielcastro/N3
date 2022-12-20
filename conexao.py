
import pymysql.cursors

connection = pymysql.connect(host='localhost', # Nome do host (servidor) do SGBD
                                user='root', # Usuário que irá conectar ao banco
                                password='', # Senha da conexão
                                database='prova03', # Nome o banco que será utilizado
                                charset='utf8mb4', # Conjunto de caracteres a utilizar
                                cursorclass=pymysql.cursors.DictCursor) # Classe do cursor que será gerado