
from class_funcao import Funcao
from class_funcionario import Funcioario

op = 1
while op !=0:
   print('\n********** MENU PRINCIPAL **********')
   print('#  1. Manter Funcoes\n#  2. Manter Funcionarios\n#  0. Sair')
   print('####################################')
   op=int(input('\nInforme uma das opcoes acima: '))

   if op == 1:
      op2=1
      while op2 !=0:
         print('\n*********** MANTER FUNCAO ***********')
         print('#  1. Cadastrar Funcao\n#  2. Pesquisar Funcao\n#  3. Editar Funcao\n#  4. Deletar Funcao \n#  0. Voltar ao Menu Principal')
         print('####################################')
         op2=int(input('\nInforme uma das opcoes acima: '))

         if op2 == 1:
            print('\n********** CADASTRAR FUNCAO *********')
            obj = Funcao( cod = input('Informe codigo: '),
                          nome = '')
            obj.cadastrar_funcao()
   
         elif op2 == 2:
            print('\n********* PESQUISAR FUNCAO *********')
            if Funcao.verificar_lista_vazia() != 0:
               cod_funcao = input('Informe codigo da Funcao: ')
               Funcao.pesquisar_funcao(cod_funcao)
            else:
               print('NAO HA FUNCAO CADASTRADA NO SISTEMA')

         elif op2 == 3:
            print('\n********** EDITAR FUNCAO **********')
            if Funcao.verificar_lista_vazia() != 0:
               cod = input('Informe codigo da Funcao a ser editada: ')
               obj = Funcao(cod, nome = '' )
               Funcao.editar_funcao(obj)
            else:
               print('NAO HA FUNCAO CADASTRADA NO SISTEMA')
   
         elif op2 == 4:
            print('\n********* DELETAR FUNCAO *********')
            if Funcao.verificar_lista_vazia() != 0:
               obj = Funcao(nome = '', 
                      cod = input('Informe codigo da funcao: ')).deletar_funcao()
            else:
               print('NAO HA FUNCAO CADASTRADA NO SISTEMA')

   elif op == 2:
      op3=1
      while op3 !=0:
         print('\n******** MANTER FUNCIONARIO ********')
         print('#  1. Cadastrar Funcionario\n#  2. Pesquisar Funcionario\n#  3. Editar Funcionario\n#  4. Deletar Funcionario \n#  0. Voltar ao Menu Principal')
         print('####################################')
         op3=int(input('\nInforme uma das opcoes acima: '))
         
         if op3 == 1:
            print('\n******* CADASTRAR FUNCIONARIO ******')
            obj = Funcioario( cpf = input('Informe cpf: '),
            nome = input('Informe nome: '),
            funcao = input('Nome da Funcao: '),
            salario = float(input('Salario: ')),
            telefone = input('Telefone: '))
            Funcioario.cadastrar_funcionario(obj)
           

         elif op3 == 2:
            print('\n******* PESQUISAR FUNCIONARIO ******')
            if Funcioario.verificar_lista_vazia_funcionario() != 0:
               cpf = input('Informe CPF do Funcionario: ')
               Funcioario.pesquisar_funcionario(cpf)
            else:
               print('NAO HA FUNCIONARIO CADASTRADO NO SISTEMA')

         elif op3 == 3:
            print('\n******** EDITAR FUNCIONARIO ********')
            if Funcioario.verificar_lista_vazia_funcionario() != 0:
               cpf = input('Informe CPF do Funcionario a ser editado: ')
               obj = Funcioario(cpf, nome='', funcao = 0, salario = 0.0, telefone = '' )
               Funcioario.editar_funcionario(obj)
            else:
               print('NAO HA FUNCIONARIO CADASTRADO NO SISTEMA')

         elif op3 == 4:
            print('\n******** DELETAR FUNCIONARIO ********')
            if Funcioario.verificar_lista_vazia_funcionario() != 0:
               obj = Funcioario(cpf = input('Informe CPF: '), 
                      nome = '',funcao = 0, salario = 0.0, telefone = '' ).deletar_funcionario()
            else:
               print('NAO HA FUNCIONARIO CADASTRADO NO SISTEMA')

