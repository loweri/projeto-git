ano_atual = 2025
while True:
    ano_nascimento_str = input("Digite o ano de nascimento (ou 'sair' para encerrar): ")
    if ano_nascimento_str == 'sair':
        break
    ano_nascimento = int(ano_nascimento_str)
    if ano_nascimento > ano_atual:
        print(f"Ano de nascimento está no futuro. Tente novamente.")
    elif ano_nascimento < 1915:
        print(f"Uau, {ano_nascimento} você deve ser muito sábio(a)!")
    else:
        minha_idade = ano_atual - ano_nascimento
        print(f"Com base na sua informação, sua idade é {minha_idade} anos.")
    print("Obrigado por usar o programa!" 
          " Se quiser tentar novamente, digite outro ano de nascimento."
          " Caso contrário, digite 'sair' para encerrar."
          " Até mais!")