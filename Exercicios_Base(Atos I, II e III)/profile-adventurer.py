# Adventurer profiler settings;
aventureiro = {}
classes = ["Mago","Guerreiro","Feiticeira","Bárbaro","Arqueiro","Sacerdote"]
armas_mago = ["Cajado do Iniciante", "Varinha do Iniciante", "Grimório Básico"]
armas_guerreiro = ["Espada Curta", "Espada Longa", "Lança"]
armas_feiticeira = ["Cajado do Iniciante", "Cetro do Iniciante", "Espada Mágica do Iniciante"]
armas_barbaro = ["Machado do Iniciante", "Clava do Iniciante", "Machados Duplos do Iniciante"]
armas_arqueiro = ["Funda do Iniciante", "Arco Curto do Iniciante", "Besta do Iniciante"]
armas_sacerdote = ["Cetro do Iniciante", "Grimório do Sacerdote Iniciante", "Varinha do Iniciante"]
while True:
    nome = input("Olá aventureiro, digite seu nome (ou 'Sair' para encerrar): ").strip().lower().capitalize()
    if nome == 'Sair':
        print("Saindo do jogo...")
        break
    aventureiro["nome"] = nome
    print(f"Muito bem {nome}! Está pronto para a aventura?")
    classe = input("Por favor, escolha sua classe(Mago/Guerreiro/Feiticeira/Bárbaro/Arqueiro/Sacerdote):").strip().lower().capitalize()
    if classe not in classes:
        print("Classe escolhida inválida, Tente novamente\n")
        continue
    aventureiro["classe"] = classe
    aventureiro["nível"] = 1
    print(f"Muito bem, a classe escolhida foi {classe}")
    print(f"O nível atual é {classe} nível {aventureiro['nível']}")
    if classe == "Mago":
        armas = armas_mago
    elif classe == "Guerreiro":
        armas = armas_guerreiro
    elif classe == "Feiticeira":
        armas = armas_feiticeira
    elif classe == "Bárbaro":
        armas = armas_barbaro
    elif classe == "Arqueiro":
        armas = armas_arqueiro
    elif classe == "Sacerdote":
        armas = armas_sacerdote

    print("\nEscolha sua arma inicial:")
    for ordem, arma in enumerate(armas, 1):
        print(f"{ordem}. {arma}")
    escolha = int(input("Digite o número da arma escolhida: ")) - 1
    aventureiro["arma"] = armas[escolha]
    print("=" * 50)
    print("\n Ficha do Aventureiro")
    print(f'Nome: {aventureiro['nome']}')
    print(f'Classe: {aventureiro['classe']}')
    print(f'Nível: {aventureiro["nível"]}')
    print(f'Arma inical: {aventureiro["arma"]}')
    print("A aventura começa agora, divirta-se!!!\n")
    print('='*50)
    break