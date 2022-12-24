from conexao import connection

class Funcao:
   def __init__(self, cod, nome):
      self.cod = cod
      self.nome = nome
   
   def verificar_lista_vazia():
      lista_funcao = Funcao.selecionar_tudo_funcao()
      return len(lista_funcao)
   
   def buscar_funcao(cod_busca):
      lista_funcao = Funcao.selecionar_tudo_funcao()
      for index in lista_funcao:
         if index['cod'] == cod_busca:
            print(f'Funcao encontrada!')
            return index['cod']
      print('Funcao não cadastrada na base de dados!')
      novo_cod = input('Informe codigo novamente: ')
      Funcao.buscar_funcao(novo_cod)
      return index['cod']
   
   def buscar_funcao_cadastro(cod_busca):
      lista_funcao = Funcao.selecionar_tudo_funcao()
      for index in lista_funcao:
         if index['cod'] == cod_busca:
            print(f'Funcao encontrada!')
            return index['cod']
   
   def cadastrar_funcao(self):
      cod_pesq = Funcao.buscar_funcao_cadastro(self.cod)
      if cod_pesq != self.cod:
         nome = input('Informe nome: ')
         with connection.cursor() as c:
            sql = f"INSERT INTO funcao (cod, nome)" + f"VALUES ('{self.cod}', '{nome}')"
            c.execute(sql)
            connection.commit()
            print('Cadastrado com sucesso!')
      else:
         print('Funcao já cadastrado!')
   
   def selecionar_tudo_funcao():
      with connection.cursor() as c:
         sql = f"SELECT * FROM funcao "
         c.execute(sql)
         res_all = c.fetchall()
         return res_all
        
   def pesquisar_funcao(cod_busca):
      lista_funcao = Funcao.selecionar_tudo_funcao()
      for index in lista_funcao:
         if index['cod'] == cod_busca:
            print(f'Codico encontrado!')
            print(f"Nome: {index['nome']} || Codigo: {index['cod']}")
            return index['cod']
      print('Funcao não cadastrada na base de dados!')
      novo_cod = input('Informe codigo novamente: ')
      Funcao.pesquisar_funcao(novo_cod)
      return index['cod']

   def editar_funcao(self):
      with connection.cursor() as c:
         codigo = Funcao.buscar_funcao(self.cod)
         name = input('Informe o novo nome da funcao:')
         cod = input('Informe o novo codigo da Funcao: ')
         sql = f"UPDATE funcao SET cod = '{cod}', nome = '{name}' WHERE cod = '{codigo}'"
         c.execute(sql)
         connection.commit()
         print('Dados atualizados com sucesso!')
         
   def deletar_funcao(self):
      with connection.cursor() as c:
         try:
            codigo = Funcao.buscar_funcao(self.cod)
            sql = f"DELETE FROM funcao WHERE cod = '{codigo}'"
            c.execute(sql)
            connection.commit()
            print('Deletado com sucesso!')
         except:
            print('Error: Funcao nao pode ser deletada, pois ha funcionario cadastrado com essa funcao!')

   def buscar_id_funcao(nome_busca):
      res_all = Funcao.selecionar_tudo_funcao()
      for index in res_all:
         if index['nome'] == nome_busca:
            print(f'Funcao encontrada!')
            print(index['id'])
            return index['id']
      print('Funcao não cadastrada na base de dados!')
      novo_nome = input('Informe nome novamente: ')
      Funcao.buscar_id_funcao(novo_nome)
      return index['id']
   


   
