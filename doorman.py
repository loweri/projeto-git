# O Porteiro do Salão Arcano
# Objetivo: Verificar a lista de convidados para barrar a entrada de magos do mal
convidados = ["Gandalf","Aragorn","Sauron","Legolas","Gimli","Saruman"]
lista_negra = ["Sauron", "Saruman"]
for convidado in convidados:
    if convidado in lista_negra:
        print(f"\nVerificando permissão...\n{convidado} acesso negado.")
    else:
        print(f"\nVerificando permissão... \n{convidado} bem vindo, acesso permitido.")

print('\nAproveitem a festa')