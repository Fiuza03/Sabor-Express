import os

restaurantes = [
    {'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
    {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False},
]

def exibir_nome_do_programa():
    ''' Essa função é responsável por imprimir na tela o nome do restaurante'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    ''' Essa funçãoé responsável por exibir as opções disponíveis'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Essa função é responsável por finalizar o app'''
    exibir_subtitulo('Finalizando o app')

def voltar_menu_principal():
    ''' Essa função faz o usuário voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    ''' imprime a mensagem "Opção Invlálida" e volta ao menu principa'''
    print('Opção Inválida!')
    voltar_menu_principal()

def exibir_subtitulo(texto):
     ''' Essa função é responsável por limpar o terminal e por detalhes de * em títulos de cada opção escolhida'''
     os.system('cls')
     linha = '*' * (len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()

def cadastrar_novo_restaurante():
     ''' Essa função é responsável por cadastrar um novo restaurante
     Inputs:
     - Nome do restaurante
     - categoria
     
     Output:
     - Adiciona um  novo restaurante a lista de restaurantes
     '''
     exibir_subtitulo('Cadastro de novos restaurantes')
     nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
     categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
     dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
     restaurantes.append(dados_do_restaurante)
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
     voltar_menu_principal()

def listar_restaurantes():
     ''' Essa função é responsável pela listagem dos restaurantes cadastrados'''
     exibir_subtitulo('Listando restaurantes')
     
     print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)}')
     for restaurante in restaurantes:
          nome_restaurante = restaurante['nome']
          categoria = restaurante['categoria']
          ativo = 'ativado' if restaurante['ativo'] else 'desativado' 
          print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

     voltar_menu_principal()

def alternar_estado_restaurante():
     ''' Essa função é responsável por mudar o status do restaurante o ativando e desativando'''
     exibir_subtitulo('Alterando estado restaurante')
     nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
     restaurante_encontrado = False

     for restaurante in restaurantes:
          if nome_restaurante == restaurante['nome']:
               restaurante_encontrado = True
               restaurante['ativo'] = not restaurante['ativo']
               mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
               print(mensagem)

     if not restaurante_encontrado:
          print('O restaurante não foi encontrado.')
     voltar_menu_principal()

def escolher_opcoes():
    ''' Responsável pela escolha das opções na tela'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
               listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
             finalizar_app() 
        else:
            opcao_invalida()
    except:
            opcao_invalida()

def main():
    ''' Responsável por rodar todas as fuções declaradas dentro do main'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
      

if __name__ == '__main__':
         main()