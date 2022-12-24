from class_funcao import Funcao
from conexao import connection


class Funcioario:
    def __init__(self, cpf: str, nome: str, funcao: Funcao, salario: float, telefone: str):
        self.cpf = cpf
        self.nome = nome
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
      
    def verificar_lista_vazia_funcionario():
      with connection.cursor() as c:
         sql = f"SELECT * FROM funcionario "
         c.execute(sql)
         res_all = c.fetchall()
         return len(res_all)

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
            if cpf_busca != self.cpf:
               busca_id_funcao = Funcao.buscar_id_funcao(self.funcao)
               sql = f"INSERT INTO funcionario (cpf, nome, funcao, salario, telefone) VALUES ('{self.cpf}','{self.nome}','{busca_id_funcao}','{self.salario}','{self.telefone}')"
               c.execute(sql)
               connection.commit()
               print('Cadastrado com sucesso!')
            else:
               print('Funcionario já cadastrado!')

    def pesquisar_funcionario(cpf_busca):
        with connection.cursor() as c:
            sql = f"SELECT * FROM funcionario "
            c.execute(sql)
            res_all = c.fetchall()
            # print(res_all)
            for index in res_all:
                if index['cpf'] == cpf_busca:
                    print(f'\n******* DADOS DO FUNCIONARIO *******')
                    print(
                        f"Nome: {index['nome']}|CPF: {index['cpf']}|Funcao_id: {index['funcao']}|Salario: R${index['salario']}|Telefone: {index['telefone']}")
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
            return index['cpf']

    def editar_funcionario(self):
         with connection.cursor() as c:
            cpf = Funcioario.buscar_funcionario(self.cpf)
            opcesEditar = None
            while (opcesEditar != 0):
                print('--------------------------')
                print(
                    '\n1 - Novo nome\n2 - Novo CPF\n3 - Nova Função\n4 - Novo Salario\n5 - Novo Telefone\n0 - Voltar ao Menu do Funcionario')
                print('--------------------------')
                opcesEditar = int(
                    input('Digite o numero da opcão que deseja fazer: '))

                if (opcesEditar == 1):
                  novo_nome = input('Novo Nome: ')
                  sql = f"UPDATE funcionario SET nome = '{novo_nome}' WHERE cpf = '{cpf}'"

                  c.execute(sql)
                  connection.commit()
                  print('Alterado com sucesso')

                elif (opcesEditar == 2):
                  with connection.cursor() as c:
                     novo_cpf = input('Novo CPF: ')
                     sql = f"UPDATE funcionario SET cpf = '{novo_cpf}' WHERE cpf = '{cpf}'"

                     c.execute(sql)
                     connection.commit()
                     print('Alterado com sucesso')

                elif (opcesEditar == 3):
                  with connection.cursor() as c:
                     nova_funcao = input('Nova Função: ')
                     novo_id_funcao = Funcao.buscar_id_funcao(nova_funcao)
                     sql = f"UPDATE funcionario SET funcao = '{novo_id_funcao}' WHERE cpf = '{cpf}'"

                     c.execute(sql)
                     connection.commit()
                     print('Alterado com sucesso')
                elif (opcesEditar == 4):
                  with connection.cursor() as c:
                     novo_salario = input('Novo Salario: ')
                     sql = f"UPDATE funcionario SET salario = '{novo_salario}' WHERE cpf = '{cpf}'"
                     c.execute(sql)
                     connection.commit()
                     print('Alterado com sucesso')

                elif (opcesEditar == 5):
                  with connection.cursor() as c:
                     novo_telefone = input('Novo Telefone: ')
                     sql = f"UPDATE funcionario SET telefone = '{novo_telefone}' WHERE cpf = '{cpf}'"
                     c.execute(sql)
                     connection.commit()
                     print('Alterado com sucesso')

    def deletar_funcionario(self):
        with connection.cursor() as c:
            cpf_busca = Funcioario.buscar_funcionario(self.cpf)
            print(cpf_busca)
            sql = f"DELETE FROM funcionario WHERE cpf = '{cpf_busca}'"
            c.execute(sql)
            connection.commit()
            print('Deletado com sucesso!')
