import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamanho = int(input('insira o comprimento da senha'))
senha = ''
for i in range(tamanho):
    caracteres = random.choice(caracteres)
    senha += caracteres
print(f"Sua senha gerada é: {senha}")