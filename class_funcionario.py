from class_funcao import Funcao
from conexao import connection

class Funcioario:
   def __init__(self, cpf: str, nome: str, funcao: Funcao, salario: float, telefone: str ):
      self.cpf = cpf
      self.nome = nome
      self.funcao = funcao
      self.salario = salario
      self.telefone = telefone
   
   
   def buscar_funcionario_cadastro(cpf_busca):
      with connection.cursor() as c:
         sql = f"SELECT * FROM funcionario "
         c.execute(sql)
         res_all = c.fetchall()
         for index in res_all:
            if index['cpf'] == cpf_busca:
               return index['cpf']
   
   def cadastrar_funcionario(self):
      with connection.cursor() as c:
         cpf_busca = Funcioario.buscar_funcionario_cadastro(self.cpf)
         busca_id_funcao = Funcao.buscar_id_funcao(self.funcao)
         if cpf_busca == self.cpf:
            print('Funcionario já cadastrado!')
         else:
            sql = f"INSERT INTO funcionario (cpf, nome, funcao, salario, telefone) VALUES ('{self.cpf}','{self.nome}','{busca_id_funcao}','{self.salario}','{self.telefone}')"
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
         cpf_busca = Funcioario.buscar_funcionario(self.cpf)
         sql = f"DELETE FROM funcionario WHERE cpf = '{cpf_busca}'"
         c.execute(sql)
         connection.commit()
         print('Deletado com sucesso!')

