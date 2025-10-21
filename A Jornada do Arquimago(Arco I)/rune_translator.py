tradutor_runico = {
    "a" : "Fogo",
    "b" : "Água",
    "c" : "Terra",
    "d" : "Ar"
}
mensagem_runica = "abdcad"
runas = ["a", "b", "c", "d"]
mensagem_traduzida = ""
for runa in mensagem_runica:
    runa_atual = tradutor_runico[runa]
    mensagem_traduzida += runa_atual + " "
print(f"A mensagem decodificada é: {mensagem_traduzida}!")