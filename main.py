import os
os.system('cls')


def cadastro():
    os.system('cls')
    biblioteca = open("biblioteca.txt","a", encoding="utf8")
    titulo = input("Digite o nome do livro: ").capitalize()
    genero = input("Selecione o gênero do livro a ser cadastrado: ").capitalize()
    autor = input("Digite o autor do livro: ").capitalize()
    preco = float(input("Digite o preço do livro: "))
    biblioteca.write(f"{titulo};{genero};{autor};{preco};\n")
    print("===============================================")
    print("Livro cadastrado com sucesso!")
    print("===============================================")

    biblioteca.close()    

def visualizar():
    os.system('cls')
    visualizar = int(input('Selecione como você deseja visualizar sua biblioteca:\n1 - Visualizar todos os livros\n2 - Buscar livros por gênero\n3 - Para voltar\n'))
    biblioteca = open("biblioteca.txt", "r", encoding="utf8")
    livros = biblioteca.readlines()
    if visualizar == 1:
        print("==============================================================================")
        for linha in livros:
            separacao = linha.split(";")
            print(f"Livros:\n{separacao[0]} - Gênero: {separacao[1]} - Autor: {separacao[2]} - Preço: R$ {float(separacao[3]):.2f}\n")
        print("==============================================================================")
        
    elif visualizar == 2:
        genero_buscar = input("Digite o gênero que você deseja visualizar: ").capitalize()
        print("==============================================================================")

        for linha in livros:
            separacao = linha.split(";")
            if separacao[1] == genero_buscar:
                print(f"Livro(s) de {genero_buscar}:\n{separacao[0]} - Autor: {separacao[2]} - Preço: R$ {float(separacao[3]):.2f}\n")
            else:
                print(f"Gênero não encontrado")
        print("==============================================================================")

    else:
        pass
    biblioteca.close()

def atualizar():
    livro_atualizar = input("Digite o nome do livro que você deseja atualizar: ")
    opcao_atualizar = input("O que deseja atualizar?\n1 - Título\n2 - Gênero\n3 - Autor\n4 - Preço")
    biblioteca = open("biblioteca.txt", "+a")
    if opcao_atualizar == 1:
            novo_titulo = input("Digite o novo título do livro: ")
            for linha in biblioteca:
                separacao = linha.split(";")
                if separacao[0] == livro_atualizar:
                    separacao[0] == novo_titulo
def excluir():
    pass
def extrato():
    pass
def main():
    while True:
        print("\n==============================================================================")
        print("Seja Bem-Vindo à sua biblioteca preferida!\n1 - Para cadastrar um novo livro \n2 - Para visualizar sua biblioteca \n3 - Para atualizar sua biblioteca\n4 - Para excluir algum livro da sua biblioteca \n5 - Para visualizar os gastos totais até o momento\n")
        print("==============================================================================")
        opcoes = int(input("Digite a opção desejada: "))
    
        if opcoes == 1:
            cadastro()
            decisao = input("Deseja algo mais? Se sim, responda 'sim', caso contrário, digite 'não'\n").capitalize()
            if decisao == "sim":
                print("1 - Para cadastrar um novo livro \n2 - Para visualizar sua biblioteca \n3 - Para atualizar sua biblioteca\n4 - Para excluir algum livro da sua biblioteca \n5 - Para visualizar os gastos totais até o momento\n")
                opcoes = int(input("Digite a opção desejada: "))
                if opcoes == 1:
                    cadastro()
                elif opcoes == 2:
                    visualizar()
                elif opcoes == 3:
                    atualizar()
                elif opcoes == 4:
                    excluir()
                elif opcoes == 5:
                    extrato()
                else:
                    print("Resposta inválida.")
            elif decisao == 'não' or decisao == 'nao':
                break
            else:
                print("Resposta inválida.")

        elif opcoes == 2:
            visualizar()
            decisao = input("Deseja algo mais? Se sim, responda 'sim', caso contrário, digite 'não'\n").capitalize()
            if decisao == "sim":
                os.system('cls')
                print("1 - Para cadastrar um novo livro \n2 - Para visualizar sua biblioteca \n3 - Para atualizar sua biblioteca\n4 - Para excluir algum livro da sua biblioteca \n5 - Para visualizar os gastos totais até o momento\n")
                opcoes = int(input("Digite a opção desejada: "))
                if opcoes == 1:
                    cadastro()
                elif opcoes == 2:
                    visualizar()
                elif opcoes == 3:
                    atualizar()
                elif opcoes == 4:
                    excluir()
                elif opcoes == 5:
                    extrato()
                else:
                    print("Resposta inválida.")
            elif decisao == 'não' or decisao == 'nao':
                break
            else:
                print("Resposta inválida.")

        elif opcoes == 3:
            atualizar()
            decisao = input("Deseja algo mais? Se sim, responda 'sim', caso contrário, digite 'não'\n").capitalize()
            if decisao == "sim":
                os.system('cls')
                print("1 - Para cadastrar um novo livro \n2 - Para visualizar sua biblioteca \n3 - Para atualizar sua biblioteca\n4 - Para excluir algum livro da sua biblioteca \n5 - Para visualizar os gastos totais até o momento\n")
                opcoes = int(input("Digite a opção desejada: "))
                if opcoes == 1:
                    cadastro()
                elif opcoes == 2:
                    visualizar()
                elif opcoes == 3:
                    atualizar()
                elif opcoes == 4:
                    excluir()
                elif opcoes == 5:
                    extrato()
                else:
                    print("Resposta inválida.")
            elif decisao == 'não' or decisao == 'nao':
                break
            else:
                print("Resposta inválida.")

        elif opcoes == 4:
            excluir()
            decisao = input("Deseja algo mais? Se sim, responda 'sim', caso contrário, digite 'não'\n").capitalize()
            if decisao == "sim":
                os.system('cls')
                print("1 - Para cadastrar um novo livro \n2 - Para visualizar sua biblioteca \n3 - Para atualizar sua biblioteca\n4 - Para excluir algum livro da sua biblioteca \n5 - Para visualizar os gastos totais até o momento\n")
                opcoes = int(input("Digite a opção desejada: "))
                if opcoes == 1:
                    cadastro()
                elif opcoes == 2:
                    visualizar()
                elif opcoes == 3:
                    atualizar()
                elif opcoes == 4:
                    excluir()
                elif opcoes == 5:
                    extrato()
                else:
                    print("Resposta inválida.")
            elif decisao == 'não' or decisao == 'nao':
                break
            else:
                print("Resposta inválida.")

        elif opcoes == 5:
            extrato()
            decisao = input("Deseja algo mais? Se sim, responda 'sim', caso contrário, digite 'não'\n").capitalize()
            if decisao == "sim":
                os.system('cls')
                print("1 - Para cadastrar um novo livro \n2 - Para visualizar sua biblioteca \n3 - Para atualizar sua biblioteca\n4 - Para excluir algum livro da sua biblioteca \n5 - Para visualizar os gastos totais até o momento\n")
                opcoes = int(input("Digite a opção desejada: "))
                if opcoes == 1:
                    cadastro()
                elif opcoes == 2:
                    visualizar()
                elif opcoes == 3:
                    atualizar()
                elif opcoes == 4:
                    excluir()
                elif opcoes == 5:
                    extrato()
                else:
                    print("Resposta inválida.")
            elif decisao == 'não' or decisao == 'nao':
                break
            else:
                print("Resposta inválida.")

if __name__ == "__main__":
    main()





