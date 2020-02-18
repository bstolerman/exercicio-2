# exercicio 2
dias_da_semana = {1 : 'domingo', 2 : 'segunda', 3 : 'terça', 4 : 'quarta', 5 : 'quinta', 6 : 'sexta', 7 : 'sábado'}
número = int(input("Digite o número: "))

if número >= 1 and número <= 7:
    print('Hoje é: ', dias_da_semana[número])
else:
    print('Insira outro número ')
