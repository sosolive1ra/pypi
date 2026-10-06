from art import tprint, text2art

# 1. Imprime direto no terminal com a fonte padrão
tprint("Sophia")

# 2. Imprime com fontes específicas
tprint("Israel", font="block")
tprint("Art", font="fancy5")

# 3. Retorna o texto estilizado como String (para usar em variáveis)
texto_ascii = text2art("Sucesso", font="small")
print(texto_ascii)