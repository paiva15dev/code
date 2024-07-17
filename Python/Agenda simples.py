def menu():
    while True:
        opcao = input('''
  MENU :
[1]CADASTRAR CONTATO
[2]VISUALIZAR LISTA         
[3]EDITAR CONTATO
[4]FAVORITAR CONTATO
[5]VISUALIZAR FAVORITOS
[6]DELETAR CONTATO        
[7]SAIR DO PROGRAMA         
          
Escolha uma opção: ''')
    
        if opcao == "1":
            cadastrarcontato()
        elif opcao == "2":
            listacontato()
        elif opcao == "3":
            editarcontato()
        elif opcao == "4":
            favoritarcontato()
        elif opcao == "5":
            visualizarfavoritos()
        elif opcao == "6":
            deletarcontato()
        elif opcao == "7":
            sair_do_programa()
        else:
            print("Opção inválida. Tente novamente.")

def cadastrarcontato():
    nome = input("Digite o nome do contato: ")
    email = input("Digite o email do contato: ")
    telefone = input("Digite o telefone do contato: ")
    favorito = input("Deseja favoritar o contato? (y/n): ").lower() == 'y'
    try:
        with open("lista.txt", "a") as lista:
            dados = f'{nome};{email};{telefone};{"sim" if favorito else "não"}\n'
            lista.write(dados)
        print("Contato cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar o contato: {e}")

def listacontato():
    try:
        with open("lista.txt", "r") as lista:
            for contato in lista:
                print(contato.strip())
    except FileNotFoundError:
        print("Nenhum contato cadastrado ainda.")

def deletarcontato():
    deletarNome = input("Digite o nome que deseja remover: ")
    try:
        with open("lista.txt", "r") as lista:
            contatos = lista.readlines()
        
        with open("lista.txt", "w") as lista:
            for contato in contatos:
                if deletarNome not in contato.split(';')[0]:
                    lista.write(contato)
        
        print(f'Contato deletado')
    except Exception as e:
        print(f"Erro ao deletar o contato: {e}")

def editarcontato():
    nome = input("Digite o nome do contato que deseja editar: ")
    try:
        with open("lista.txt", "r") as lista:
            contatos = lista.readlines()

        for i, contato in enumerate(contatos):
            if nome in contato:
                print(f"Contato encontrado: {contato.strip()}")
                novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
                novo_email = input("Digite o novo email (ou pressione Enter para manter o atual): ")
                novo_telefone = input("Digite o novo telefone (ou pressione Enter para manter o atual): ")
                favorito = input("Deseja favoritar o contato? (y/n): ").lower() == 'y'
                
                dados = contato.strip().split(';')
                dados[0] = novo_nome if novo_nome else dados[0]
                dados[1] = novo_email if novo_email else dados[1]
                dados[2] = novo_telefone if novo_telefone else dados[2]
                dados[3] = "sim" if favorito else "não"
                
                contatos[i] = ';'.join(dados) + '\n'
                break
        else:
            print("Contato não encontrado.")

        with open("lista.txt", "w") as lista:
            lista.writelines(contatos)
        
        print("Contato editado com sucesso!")
    except Exception as e:
        print(f"Erro ao editar o contato: {e}")

def favoritarcontato():
    nome = input("Digite o nome do contato que deseja favoritar/desfavoritar: ")
    try:
        with open("lista.txt", "r") as lista:
            contatos = lista.readlines()

        for i, contato in enumerate(contatos):
            if nome in contato:
                dados = contato.strip().split(';')
                dados[3] = "não" if dados[3] == "sim" else "sim"
                contatos[i] = ';'.join(dados) + '\n'
                break
        else:
            print("Contato não encontrado.")

        with open("lista.txt", "w") as lista:
            lista.writelines(contatos)
        
        print("Contato atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar o contato: {e}")

def visualizarfavoritos():
    try:
        with open("lista.txt", "r") as lista:
            for contato in lista:
                if 'sim' in contato.strip().split(';')[3]:
                    print(contato.strip())
    except FileNotFoundError:
        print("Nenhum contato cadastrado ainda.")

def sair_do_programa():
    print("Saindo do programa...")
    exit()

def main():
    menu()

if __name__ == "__main__":
    main()
