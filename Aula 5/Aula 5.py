
nome = 'Roberto'
idade = 29
altura = 1.84
e_maior = idade > 18
peso = 88
imc = peso / (altura **2)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)

if e_maior:
    print('Maior de idade')
else:
    print('Menor de idade')