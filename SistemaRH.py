import time
def calculo_SalarioLiquido():
    # Cálculo do Salário Líquido
    # Variaveis/Listas

    salIRRF = [1903.98, 2826.65, 3751.05, 4664.68]  # Lista de divisão de salários - IRRF
    aliIRRF = [0, 7.5, 15, 22.5, 27.5]  # Lista de divisão de aliquotas em relação aos salários - IRRF
    parIRRF = [0, 142.80, 354.8, 636.13, 869.36]  # Lista de divisão de dedução do IRRF referente aos salários

    salINSS = [1100, 2203.48, 3305.22, 6433.57]  # Lista de divisão de salários - INSS
    aliINSS = [7.50, 9, 12, 14]  # Lista de divisão de aliquotas em relação aos salários - INSS
    parINSS = [82.5, 99.31, 132.20]

    salarioBruto = 0
    salarioBrutoB = salarioBruto
    taxaIRRF = 0
    taxaINSS = 0

    try:
        salarioBruto = float(input("Informe seu salário bruto: "))
        # IRRF
        if (salarioBruto <= salIRRF[0]):  # Salário igual ou menor a 1903,98.
            taxaIRRF = salarioBruto * (aliIRRF[0] / 100) - parIRRF[0]
        elif (salarioBruto <= salIRRF[1]):  # Salário igual ou menor a 2826,65.
            taxaIRRF = salarioBruto * (aliIRRF[1] / 100) - parIRRF[1]
        elif (salarioBruto <= salIRRF[2]):  # Salário igual ou menor a 3751,05.
            taxaIRRF = salarioBruto * (aliIRRF[2] / 100) - parIRRF[2]
        elif (salarioBruto <= salIRRF[3]):  # Salário igual ou menor a 4664,68.
            taxaIRRF = salarioBruto * (aliIRRF[3] / 100) - parIRRF[3]
        elif (salarioBruto < 0):  # Salário deve ser positivo.
            print("O valor deve ser positivo.")
        else:  # Salário maior que 4664,68.
            taxaIRRF = salarioBruto * (aliIRRF[4] / 100) - parIRRF[4]
        # INSS
        if (salarioBruto <= salINSS[0]):  # Salário igual ou menor a 1100
            taxaINSS = salarioBruto * (aliINSS[0] / 100)
        elif (salarioBruto <= salINSS[1]):  # Salário igual ou menor a 2203,48
            salarioBrutoB = salarioBruto - salINSS[0]
            taxaINSS = salarioBrutoB * (aliINSS[1] / 100) + parINSS[0]
        elif (salarioBruto <= salINSS[2]):  # Salário igual ou menor a 3305,22
            salarioBrutoB = salarioBruto - salINSS[1]
            taxaINSS = salarioBrutoB * (aliINSS[2] / 100) + (parINSS[0] + parINSS[1])
        elif (salarioBruto <= salINSS[3]):  # Salário igual ou menor a 6433,57
            salarioBrutoB = salarioBruto - salINSS[2]
            taxaINSS = salarioBrutoB * (aliINSS[3] / 100) + (parINSS[0] + parINSS[1] + parINSS[2])
        else:  # Salário acima do teto do INSS
            taxaINSS = (salINSS[0] * (aliINSS[0] / 100)) + ((salINSS[1] - salINSS[0]) * (aliINSS[1] / 100)) + (
                        (salINSS[2] - salINSS[1]) * (aliINSS[2] / 100)) + (
                                   (salINSS[3] - salINSS[2]) * (aliINSS[3] / 100))

    except ValueError:
        print("\nO valor informado não é compativel com o programa.\n")

    salarioLiquido = salarioBruto - (taxaIRRF + taxaINSS)

    print(f"Salário Bruto Informado: {salarioBruto:.2f}")
    print(f"Taxa do IRRF: {taxaIRRF:.2f}")
    print(f"Taxa do INSS: {taxaINSS:.2f}")
    print(f"Valor Final: {salarioLiquido:.2f}")


#Cálculo do 13° salário
def calculo_13():
    print(f'=====Calculo do 13° salário do funcionário=====\nInforme o salário bruto e o número de meses trabalhados até outubro')  #
    #inputs
    SB = 0
    NMT = 0
    print()
    while True:
        try:
            SB = float(input('\nSalário bruto:'))
            if SB <1100:
                raise
            else:
                break
        except:
            if SB > 0:
                print('\nERRO:O salário mínimo definido pela lei é R$1.100,00\n ')
            else:
                print('\nERRO:Digite um valor válido\n ')

    while True:
        try:
            NMT = float(input('\nTempo total de trabalho esse ano(meses):'))
            if NMT <= 0:
                raise
            else:
                break
        except:
            print('\nERRO:Digite um número válido\n')
        if SB > 1100 and NMT >= 0:
            break

    #Cálculo INSS (OK)

    SBB = SB    #Variável de controle p cálculo progressivo
    #Parcelas de cada faixa de salário da tabela
    PD = 0
    PA1 = 82.5
    PA2 = 99.31
    PA3 = 132.2

    AL = 0
    if SB < 6433.58:
        if SB <= 1100:
            AL = 0.075
            PD = 0
        elif SB >= 1100.01 and SB <= 2203.48:
            SBB = SB - 1100
            AL = 0.09
            PD = PA1
        elif SB >= 2203.49 and SB <= 3305.22:
            SBB = SB - 2203.48
            AL = 0.12
            PD = PA1 + PA2
        elif SB >= 3305.23 and SB <= 6433.57:
            SBB = SB - 3305.22
            AL = 0.14
            PD = PA1 + PA2 + PA3
        INSS = SBB*AL + PD
        round(INSS, 2)
    else:
        INSS = 751.97
    AL = 0

    #Cálculo do IRRF (OK)

    SB2 = SB - INSS  # base de cálculo

    if SB2 <= 1903.98:
        IRRF = 0
    else:
        if SB2 >= 1903.99 and SB2 <=2862.65:
            AL = 0.075
            PD = 142.8
        elif SB2 >= 2862.66 and SB2 <= 3751.05:
            AL = 0.15
            PD = 354.8
        elif SB2 >= 3751.06 and SB2 <= 4664.68:
            AL = 0.225
            PD = 636.13
        else:
            AL = 0.275
            PD = 869.36
        IRRF = SB2*AL - PD
    #Cálculo das parcelas
              # Parcela 1
    VEP = (SB / 12) * NMT
    PP = VEP / 2
              # Parcela 2
    VES = (SB - INSS - IRRF) / 12 * NMT
    SP = VES - PP

    #Output
    print(f'\n===Descontos===\nIRRF = R${IRRF:.2f}\nINSS = R${INSS:.2f}')
    print(f'\n===A receber===\n1° parcela = R${PP:.2f}\n2° parcela = R${SP:.2f}\nTotal = R${PP+SP:.2f}')

#Começo do programa

while True:
    print('\t\t\t=========SistemaRH=========\n\t\t\t\t       \n ')
    try:
        comando = int(input('\n[1] Calcular salário líquido\t[2] Calcular férias líquida\n[3] Calcular 13° salário\t\t[4] Sair do programa\n\nO que precisa ser feito?:'))
        if comando != 1 and comando != 2 and comando !=3 and comando !=4:
            raise
        elif comando == 1:
            while True:
                calculo_SalarioLiquido()
                print()
                try:
                    c = int(input('[1] Calcular novamente [2] Sair\nR:'))
                    if c != 1 and c != 2:
                        raise
                except:
                    print('ERRO Digite um ou dois\n')
                if c == 2:
                    break
        elif comando == 3:
            while True:
                calculo_13()
                print()
                try:
                    c = int(input('[1] Calcular novamente [2] Sair\nR:'))
                    if c != 1 and c != 2:
                        raise
                except:
                    print('ERRO Digite um ou dois\n')
                if c == 2:
                    break
        elif comando == 4:
            print('Até a próxima\n\n')
            print('Saindo', end='')
            for n in range(1,4):
                print('.', end='')
                time.sleep(1)

            break
    except:
        print('Digite um comando válido')
        time.sleep(1)