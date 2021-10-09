
print('Preencha os dados abaixo para seguir no processo.')
print()
nome = input('Nome completo: ')
cpf = input('CPF: ')
idade = input('Idade: ')
idade = int(idade)
cidade = input('Cidade: ')
ano_nascimento = 2021 - idade
email = input('E-mail: ')
telefone = input('Telefone com DDD: ')
print()


print(f'{nome} portador do CPF: {cpf}')
print(f'E-mail: {email}, reside em {cidade} atualmente')
print(f'Nasceu no ano de {ano_nascimento}.')
print(f'Telefone para contato: {telefone}')
print()

if idade >= 18:
    print('Você foi "aprovado" para a próxima etapa')
else:
    print('Infelizmente você não foi "aprovado" para a próxima fase')