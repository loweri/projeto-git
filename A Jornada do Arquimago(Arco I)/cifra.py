cifra = {
    "1": "o", "2": "b", "3": "r", "4": "i",
    "5": "g", "6": "a", "7": "d", "8": "p",
    "9": "e", "0": "l", "-": "s", "_": "c"
}
mensagem_codificada = "1234567_890-9-1"
mensagem_decodificada = ""
for codigo in mensagem_codificada:
    tradução = cifra[codigo]
    mensagem_decodificada += tradução + ""
print(f"Tradução da cifra: {mensagem_decodificada}")
