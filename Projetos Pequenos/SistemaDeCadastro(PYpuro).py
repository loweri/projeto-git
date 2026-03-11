# Para reforçar completamente a base dos meus conhecimentos, vou desenvolver um sistema de cadastro de personagens via terminal.
# Os personagens escolhidos aqui foram os de Dragon Ball puramente ilustrativo, sem interface nem biblioteca externa.
# Os pilares e objetivos são:
# [dict] para representar cada personagem
# [list] para armazenar todos os personagens
# [def] para cada operação separada
# [for] para percorrer e buscar
# [input()] para receber dados do usuário
# [return] em toda função que produz dado
# As funcionalidades objetivo são:
# 1 - Cadastrar personagem com nome, raça e nível de poder.
# 2 - Listar todos os personagens cadastrados.
# 3 - Buscar o personagem pelo nome.
# 4 - Sair do Programa.
personagens_DB = []
def cadastro():
    print("Por favor, digite o nome do personagem: ")
    nome_cc = input().strip().lower()
    print(f"Agora digite o poder do personagem, números inteiros apenas (ex: 150mil = 150000): ")
    poder_cc = int(input().strip())
    print(f"Por favor digite a primeira habilidade principal do personagem: ")
    habilidade1_cc = input().strip().lower()
    print(f"Por favor digite a segunda habilidade do personagem: ")
    habilidade2_cc = input().strip().lower()
    perso01 = {"nome":nome_cc,
            "poder":poder_cc,
            "habilidade 1":habilidade1_cc,
            "habilidade 2":habilidade2_cc}
    personagens_DB.append(perso01)
    return perso01
def listar():
    listanomes = []
    for nomes in personagens_DB:
        newname = nomes["nome"]
        listanomes.append(newname)
    return listanomes
print("Bem vindo guerreiros e guerreiras, por favor, escolha uma das opções abaixo:")
print(f"01 - Cadastrar novo personagem!" \
"\n02 - Lista de personagens." \
"\n03 - Buscar por nome." \
"\n04 - Sair do programa.")
print("Digite númericamente ou por extenso a opção selecionada: ") 
while True:
    opcao_selecionada = input().lower().strip()
    if opcao_selecionada == "01":
        print(f"Bem vindo ao sistema de cadastro de personagens, por favor leia com atenção cada pergunta a seguir:")
        print(cadastro())
    elif opcao_selecionada == "um":
        print(f"Bem vindo ao sistema de cadastro de personagens, por favor leia com atenção cada pergunta a seguir:")
        print(cadastro())
    elif opcao_selecionada == "1":
        print(f"Bem vindo ao sistema de cadastro de personagens, por favor leia com atenção cada pergunta a seguir:")
        print(cadastro())
    elif opcao_selecionada == "02":
        print(f"Lista de personagens no banco de dados:")
        print(listar())
    elif opcao_selecionada == "2":
        print(f"Lista de personagens no banco de dados:")
        print(listar())
    elif opcao_selecionada == "dois":
        print(f"Lista de personagens no banco de dados:")
        print(listar())
    elif opcao_selecionada == "03":
        print("Por favor, digite o nome desejado: ")
        buscarnome = input().lower().strip()
        for personagens in personagens_DB:
            if buscarnome == personagens["nome"]:
                print(personagens)
                break
        else:
            print("Erro, resultado da busca não encontrou nenhum nome, garanta que a ortografia esteja correta.")
    elif opcao_selecionada == "3":
        print("Por favor, digite o nome desejado: ")
        buscarnome = input().lower().strip()
        for personagens in personagens_DB:
            if buscarnome == personagens["nome"]:
                print(personagens)
                break
        else:
            print("Erro, resultado da busca não encontrou nenhum nome, garanta que a ortografia esteja correta.")
    elif opcao_selecionada == "três":
        print("Por favor, digite o nome desejado: ")
        buscarnome = input().lower().strip()
        for personagens in personagens_DB:
            if buscarnome == personagens["nome"]:
                print(personagens)
                break
        else:
            print("Erro, resultado da busca não encontrou nenhum nome, garanta que a ortografia esteja correta.")
    elif opcao_selecionada == "tres":
        print("Por favor, digite o nome desejado: ")
        buscarnome = input().lower().strip()
        for personagens in personagens_DB:
            if buscarnome == personagens["nome"]:
                print(personagens)
                break
        else:
            print("Erro, resultado da busca não encontrou nenhum nome, garanta que a ortografia esteja correta.")
    elif opcao_selecionada == "04":
        print("Opção ""Sair"" selecionada, obrigado por utilizar o programa, até a próxima!")
        break
    elif opcao_selecionada == "4":
        print("Opção ""Sair"" selecionada, obrigado por utilizar o programa, até a próxima!")
        break
    elif opcao_selecionada == "quatro":
        print("Opção ""Sair"" selecionada, obrigado por utilizar o programa, até a próxima!")
        break
# finalizado com sucesso, é mais do mesmo que eu já sei, porém havia muita coisa aqui que eu ainda estava travando.