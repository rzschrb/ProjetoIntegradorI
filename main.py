from ProjetoIntegradorI.classModules import *

CRED = '\033[91m'
CGREEN = '\033[92m'
CEND = '\033[0m'

# Inicio com nome e salario

while True:
    try:
        nome = input('Qual seu nome: ')
        salario = float(input('Digite seu salário bruto: '))
        if salario < 1100:
            print(CRED + 'ERRO: ' + CEND + 'O salário minimo definido pela lei é R$ 1100.')
        else:
            Sistema = SistemaRH(0, 0, 0)
            Sistema.set_salarioBruto(salario)
            Sistema.calc_inss(Sistema.get_salarioBruto())
            Sistema.calc_irrf(Sistema.get_salarioBruto(), Sistema.get_taxaINSS())
            break
    except ValueError:
        print("Você digitou um valor inválido.")

while True:
    print("\n[1] Cálculo de Salário Líquido.")
    print("[2] Cálculo de Férias Líquida.")
    print("[3] Cálculo de Décimo Terceiro.")
    print("[4] Fechar o programa.")

    try:
        x = int(input(CGREEN + "\n>" + CEND + " Digite uma opção: "))
    except ValueError:
        print(CRED + 'ERRO: ' + CEND + 'Opção inválida.')

    if x == 1:
        Sistema.calc_liquidsal(Sistema.get_salarioBruto(), Sistema.get_taxaINSS(), Sistema.get_taxaIRRF())

        print(f'\nTaxa INSS: R$ {Sistema.get_taxaINSS()}')
        print(f'Taxa IRRF: R$ {Sistema.get_taxaIRRF()}')
        print(f'Salário Líquido: R$ {Sistema.get_salarioLiquido()}')
    if x == 2:
        Sistema.calc_ferias(Sistema.get_salarioBruto(), Sistema.get_taxaINSS(), Sistema.get_taxaIRRF())
    if x == 4:
        print(CRED + '\nFechando o programa.' + CEND)
        exit()

prin