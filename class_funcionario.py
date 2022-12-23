from class_funcao import Funcao
from conexao import connection

class Funcioario:
   def __init__(self, cpf: str, nome: str, funcao: Funcao, salario: float, telefone: str ):
      self.cpf = cpf
      self.nome = nome
      self.funcao = funcao
      self.salario = salario
      self.telefone = telefone
   
   def buscar_id_funcao(nome_busca):
      res_all = Funcao.selecionar_tudo_funcao()
      for index in res_all:
         if index['nome'] == nome_busca:
            print(f'Funcao encontrada!')
            return index['id']
      print('Funcao não cadastrada na base de dados!')
      novo_nome = input('Informe nome novamente: ')
      Funcioario.buscar_id_funcao(novo_nome)
   
   def buscar_funcionario(cpf_busca):
      with connection.cursor() as c:
         sql = f"SELECT * FROM funcionario "
         c.execute(sql)
         res_all = c.fetchall()
         for index in res_all:
            if index['cpf'] == cpf_busca:
               print(f'Funcionario encontrado!')
               return index['cpf']
         print('Funcionario não cadastrado na base de dados!')
         cpf_nome = input('Informe CPF novamente: ')
         Funcioario.buscar_funcionario(cpf_nome)
   
   def cadastrar_funcionario(self):
      with connection.cursor() as c:
         cpf_busca = Funcioario.buscar_funcionario(self.cpf)
         if cpf_busca == self.cpf:
            print('Funcionaro já cadastrado!')
         else:
            busca_id_funcao = Funcioario.buscar_id_funcao(self.funcao)
            sql = f"INSERT INTO funcionario (cpf, nome, funcao, salario, telefone)" + f" VALUES ( '{self.cpf}','{self.nome}','{busca_id_funcao}','{self.salario}', '{self.telefone}')"
            c.execute(sql)
            connection.commit()
            print('Cadastrado com sucesso!')
   
   def pesquisar_funcionario(cpf_busca):
      with connection.cursor() as c:
         sql = f"SELECT * FROM funcionario "
         c.execute(sql)
         res_all = c.fetchall()
         #print(res_all)
         for index in res_all:
            if index['cpf'] == cpf_busca:
               print(f'\n******* DADOS DO FUNCIONARIO *******')
               print(f"Nome: {index['nome']}|CPF: {index['cpf']}|Funcao_id: {index['funcao']}|Salario: R${index['salario']}|Telefone: {index['telefone']}")
               return index['cpf']
         print('CPF não cadastrado na base de dados!')
         novo_cpf = input('Informe CPF novamente: ')
         Funcioario.pesquisar_funcionario(novo_cpf)
   
   def buscar_funcionario(cpf_busca):
      with connection.cursor() as c:
         sql = f"SELECT * FROM funcionario "
         c.execute(sql)
         res_all = c.fetchall()
         for index in res_all:
            if index['cpf'] == cpf_busca:
               print(f'Funcionario encontrado!')
               return index['cpf']
         print('Funcionario não cadastrado na base de dados!')
         cpf_nome = input('Informe CPF novamente: ')
         Funcioario.buscar_funcionario(cpf_nome)

   def editar_funcionario(self):
      with connection.cursor() as c:
         cpf = Funcioario.buscar_funcionario(self.cpf)
         name = input('Informe o novo nome:')
         novo_cpf = input('Informe o novo CPF: ')
         funcao_nome = input('Nome da funcao')
         busca_id_funcao = Funcioario.buscar_id_funcao(funcao_nome)
         salario = float(input('Salario: '))
         telefone = input('Telefone: ')
         sql = f"UPDATE funcionario SET cpf = '{novo_cpf}', nome = '{name}', funcao = '{busca_id_funcao}', salario = '{salario}', telefone = '{telefone}' WHERE cpf = '{cpf}'"
         c.execute(sql)
         connection.commit()
         print('Dados atualizados com sucesso!')
   
   def deletar_funcionario(self):
      with connection.cursor() as c:
         nome = Funcioario.buscar_funcionario(self.nome)
         sql = f"DELETE FROM funcionario WHERE nome = '{nome}'"
         c.execute(sql)
         connection.commit()
         print('Deletado com sucesso!')

