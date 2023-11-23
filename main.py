import os
os.system('cls')

def decisao():
    while True:
        decisao = input("Deseja algo mais? Se sim, responda 'sim', caso contrário, digite 'não'\n").capitalize()
        if decisao == "Sim":
            return True
        elif decisao == 'Não' or decisao == 'Nao':
            return False
        else:
            print("Resposta inválida.")


def cadastro():
    os.system('cls')
    with open("biblioteca.txt","a", encoding="utf8") as biblioteca:
        titulo = input("Digite o nome do livro: ").capitalize()
        genero = input("Digite o gênero do livro a ser cadastrado: ").capitalize()
        autor = input("Digite o autor do livro: ").capitalize()
        review = input("O livro é bom? Conta a história de que? Você gostou? Escreva a sua opnião sobre o livro: ")
        try:
            preco = float(input("Digite o preço do livro: "))
        except ValueError:
            print("Digite com números entre os dígitos 0-9!")
        else:
            biblioteca.write(f"{titulo};{genero};{autor};{preco};{review};\n")
            print("===============================================")
            print("Livro cadastrado com sucesso!")
            print("===============================================")
            return decisao()    

def visualizar():
    os.system('cls')
    visualizar = int(input('Selecione como você deseja visualizar sua biblioteca:\n1 - Visualizar todos os livros\n2 - Buscar livros por gênero\n3 - Para voltar\n'))
    biblioteca = open("biblioteca.txt", "r", encoding="utf8")
    livros = biblioteca.readlines()
    if visualizar == 1:
        print("==============================================================================")
        print(f"Livros:\n")
        for linha in livros:
            separacao = linha.split(";")
            print(f"{separacao[0]} - Gênero: {separacao[1]} - Autor: {separacao[2]} - Preço: R$ {float(separacao[3]):.2f}\n")
        print("==============================================================================")
        
    elif visualizar == 2:
        genero_buscar = input("Digite o gênero que você deseja visualizar: ").capitalize()
        print("==============================================================================")
        vazio = True
        for linha in livros:
            separacao = linha.split(";")
            if separacao[1] == genero_buscar:
                print(f"Livro(s) de {genero_buscar}:\n{separacao[0]} - Autor: {separacao[2]} - Preço: R$ {float(separacao[3]):.2f}\n")
                vazio = False
        if vazio == True:
            print("Gênero não encontrado")

        print("==============================================================================")

    else:
        print("Digite apenas '1' ou '2'")
    biblioteca.close()
    return decisao()  

def atualizar():

    with open('biblioteca.txt', "r", encoding="utf8") as file:
        livros = file.readlines()
    livro_atualizar = input("Digite o livro que você deseja atualizar: ").capitalize()
    print("Atualizações: ")
    novo_titulo = input("Digite o novo título do livro: ").capitalize()
    novo_genero = input("Digite o novo genêro do livro: ").capitalize()
    novo_autor = input("Digite o novo nome do autor: ").capitalize()
    novo_preco = float(input("Digite o novo preço do livro: "))
    novo_review = input("Digite a resenha do seu livro ").capitalize()
    
    with open('biblioteca.txt', 'w', encoding='utf8') as file:
        for linha in livros:
            separacao = linha.split(";")
            if separacao[0] != livro_atualizar:
                file.write(linha)
            else:
                file.write((f"{novo_titulo};{novo_genero};{novo_autor};{novo_preco};{novo_review};\n"))
                print("===============================================")
                print("Livro atualizado com sucesso!")
                print("===============================================")

    return decisao() 

def excluir():
    os.system('cls')

    livro_excluir = input("Digite o nome do livro que você deseja excluir:\n").capitalize()

    with open("biblioteca.txt", "r", encoding="utf8") as biblioteca:
        livros = biblioteca.readlines()

    with open('biblioteca.txt', 'w') as nova_lista:
        for livro in livros:
            temp = livro.split(';')
            if temp[0] != livro_excluir:
                nova_lista.write(livro)
            else:
                print(f"Livro excluído com sucesso!")
    return decisao()  

def extrato():
    gastos = 0
    with open('biblioteca.txt', 'r', encoding = 'utf8') as biblioteca:
        livros = biblioteca.readlines()

    for livro in livros:
        temp = livro.split(';')
        gastos += float(temp[3])

    print (f'Foram gastos {gastos} reais com sua biblioteca até o momento.\n')
    return decisao()  

primeira_vez = True
def main():
    global primeira_vez
    while True:
        os.system('cls')
        print("==============================================================================")
        if primeira_vez == True:
            print("Seja Bem-Vindo à sua biblioteca preferida!")
        print("1 - Para cadastrar um novo livro \n2 - Para visualizar sua biblioteca \n3 - Para atualizar sua biblioteca\n4 - Para excluir algum livro da sua biblioteca \n5 - Para visualizar os gastos totais até o momento\n6 - Para sair")
        print("==============================================================================")
        try:
            opcoes = int(input("Digite a opção desejada: "))
        except ValueError:
             print("Escreva com dígitos de 1-6!")
        else:
            if opcoes == 1:
                continuar = cadastro()
            elif opcoes == 2:
                continuar = visualizar()
            elif opcoes == 3:
                continuar = atualizar()
            elif opcoes == 4:
                continuar = excluir()
            elif opcoes == 5:
                continuar = extrato()
            elif opcoes == 6:
                break
            else:
                print("Resposta inválida.")
            
            primeira_vez = False
            if continuar == False:
                break

if __name__ == "__main__":
    main()