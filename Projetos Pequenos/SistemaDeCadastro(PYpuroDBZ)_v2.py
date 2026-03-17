# Aqui o foco agora é aprimorar o sistema de cadastro.
# A v2 traz a mudança de dict pra class, e também vamos simplificar as estruturas de código pra diminuir e ficar mais limpo.
import json
# ================= definindo o que vai na classe do objeto ================= #
class Personagem_DB:
    def __init__(self, nome, poder, habilidades):
        self.nome = nome
        self.poder = poder
        self.habilidades = habilidades
    def __str__(self):
        return f"Nome: {self.nome} | Poder: {self.poder} | Habilidades: {', '.join(self.habilidades)}"
# ================= lista para guardar os personagens ================= #
personagens_DB = []
# ================= conversão para json, salvamento e carregamento ================= #
# salvar > objeto para lista de dicionario
def salvar():
    Personagem_DBJson = []
    for personagem in personagens_DB:
        pers_dict_to_json = {"nome": personagem.nome,"poder":personagem.poder,"habilidades":personagem.habilidades}
        Personagem_DBJson.append(pers_dict_to_json)
    with open("Projetos Pequenos/Personagem_DBJson.json", "w") as arquivo:
        json.dump(Personagem_DBJson, arquivo)
# carregar > lista json_dict para objeto
def carregar():
    with open("Projetos Pequenos/Personagem_DBJson.json", "r") as arquivo:
        temp_data = json.load(arquivo)
        for per in temp_data:
            temp_name = per["nome"]
            temp_power = per["poder"]
            temp_skill = per["habilidades"]
            rebuilt = Personagem_DB(temp_name, temp_power, temp_skill)
            personagens_DB.append(rebuilt)
# ================= função para atualizar personagens cadastrados ================= #
def atualizar():
    print("Buscando lista de personagens...")
    if not personagens_DB:
        print("Ainda não há personagens registrados. Digite novamente uma opção válida do menu.")
        return
    for p in personagens_DB:
        print(p)
    print("Qual personagem gostaria de atualizar?")
    atualizar_p = input().strip().lower()
    for personagem in personagens_DB:
        if atualizar_p == personagem.nome:
            print(f"Personagem {atualizar_p} foi encontrado, escolha qual atributo deseja alterar:")
            print("Digite o número correspondente: 1 - Nome; 2 - Poder; 3 - Habilidades:")
            pe_escolha = int(input().strip())
            if pe_escolha == 1:
                print(f"Opção 'Alterar nome' escolhida para {atualizar_p}, forneça a correção:")
                pe1_corrigir = input().strip().lower()
                personagem.nome = pe1_corrigir
                print(f"O nome com alteração agora é: {pe1_corrigir}.")
            elif pe_escolha == 2:
                print(f"Opção 'Alterar Poder' escolhida para {atualizar_p}, forneça a correção (apenas numeros inteiros, sem virgula ou ponto):")
                pe2_corrigir = int(input().strip())
                personagem.poder = pe2_corrigir
            elif pe_escolha == 3:
                print(f"Opção 'Alterar Habilidade', forneça a correção:")
                print("Habilidade 1 - correção:")
                pe3_1_corrigir = input().strip().lower()
                print("Habilidade 2 - correção:")
                pe3_2_corrigir = input().strip().lower()
                personagem.habilidades = [pe3_1_corrigir,pe3_2_corrigir]
            salvar()
            break
    else:
        print("Parece que a busca não encontrou, verifique a ortografia e tente novamente!")
# ================= função para funcionar o sistema de cadastro ================= #
def cadastro():
    print("Por favor, digite o nome do personagem: ")
    nome = input().strip().lower()
    print(f"Agora digite o poder do personagem, números inteiros apenas (ex: 150mil = 150000): ")
    poder = int(input().strip())
    print(f"Por favor digite a primeira habilidade principal do personagem: ")
    habilidade1 = input().strip().lower()
    print(f"Por favor digite a segunda habilidade do personagem: ")
    habilidade2 = input().strip().lower()
    habilidades = [habilidade1, habilidade2]
    novo_personagem = Personagem_DB(nome,poder,habilidades)
    personagens_DB.append(novo_personagem)
    return novo_personagem
# ================= funções para mostrar a lista de personagens ================= #
def listar():
    listanomes = []
    for Personagem in personagens_DB:
        newname = Personagem.nome
        listanomes.append(newname)
    return listanomes
# ================= inicio da parte de design e front ================= #
try:
    carregar()
except FileNotFoundError:
    personagens_DB = []
print("Bem vindo guerreiros e guerreiras, por favor, escolha uma das opções abaixo:")
print(f"01 - Cadastrar novo personagem!" \
"\n02 - Lista de personagens." \
"\n03 - Buscar por nome." \
"\n04 - Atualizar informação de personagem." \
"\n05 - Sair do programa.")
print("Digite apenas o numero individual (1, 2, 3, 4 ou 5): ")
while True:
    opcao_selecionada = int(input())
    if opcao_selecionada == 1:
        print(f"Bem vindo ao sistema de cadastro de personagens, por favor leia com atenção cada pergunta a seguir:")
        print(cadastro())
        salvar() ## salvar adicionado pra toda vez que criar um personagem transformar em dicionário e adicionar na lista pra JSON
    elif opcao_selecionada == 2:
        print(f"Lista de personagens no banco de dados:")
        print(listar())
    elif opcao_selecionada == 3:
        print("Por favor, digite o nome desejado: ")
        buscarnome = input().lower().strip()
        for personagens in personagens_DB:
            if buscarnome == personagens.nome:
                print(personagens)
                break
        else:
            print("Erro, personagem não encontrado. Verifique a ortografia e tente novamente!")
    elif opcao_selecionada == 4:
        print("Atualizar informações:")
        atualizar()
    elif opcao_selecionada == 5:
        print("Opção ""Sair"" selecionada, obrigado por utilizar o programa, até a próxima!")
        break
# ================= fim da v2 - em breve v3 com mais adições: deletar personagem, validar input e tratar erro, função de comparação entre dois personagens ================= #