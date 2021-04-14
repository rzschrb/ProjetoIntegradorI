'''
[RF 03]: Calcular 13°

O cálculo do 13° é feito referente ao salário do funcionário como também do número de meses trabalhado.

Legenda:

SB = Salário Bruto. INPUT
IRRF = Alíquota referente ao salário bruto.
INSS = Imposto Salarial INSS.
NMT = Número de Meses Trabalhados INPUT
NMTO = Número de Meses Trabalhados até outubro INPUT
VEP = Valor Encontrado Primeira Parcela
VES = Valor Encontrado Segunda Parcela
PP = Primeira Parcela do Decimo Terceiro OUTPUT
SP = Segunda Parcela do Decimo Terceiro OUTPUT

As fórmulas abaixo representam o cálculo feito para chegar a primeira parcela do decimo terceiro.

VEP = (SB / 12) * NMTO
PP = VEP / 2

As fórmulas abaixo representam o cálculo feito para chegar a segunda e última parcela do decimo terceiro.

VES = (SB / 12) * NMT
SP = VES - (PP + INSS + IRRF)
'''
'''
PD - parcela a deduzir
AL - alíquota

A fórmula abaixo representa o cálculo feito referente ao IRRF:
SB * (AL/100) - PD = IRRF

A fórmula abaixo representa o cálculo feito referente ao INSS:
SB * (AL/100) = INSS

==tabela INSS==
    Faixa salarial         | Alíquota   |Parcela
até R$ 1.100,00            |   7,50%    |82.5
R$ 1.100,01 até R$ 2.203,48|   9,00%    |99.31
R$ 2.203,49 até R$ 3.305,22|   12,00%   |132.2
R$ 3.305,23 até R$ 6.433,57|   14,00%   |
acima = 751.97

==tabela IRRF==
    Faixa de salário         | Alíquota | Parcela a deduzir(PD)
Até R$1.903,98               |  Isento  | R$ 0
De R$1.903,99 até R$2.826,65 |   7,5%   | R$142,80
De R$ 2.826,66 a R$ 3.751,05 |   15%    | R$354,80
De R$ 3.751,06 a R$ 4.664,68 |   22,5%  | R$636,13
Acima de R$4.664,68          |   27,5%  | R$869,36



'''
#def acrescimo_horaextra():

def calculo_13():
    print(f'=====Calculo do 13° salário do funcionário=====\nInforme o salário bruto, número de meses trabalhados e número de meses trabalhados até outubro')  #
    #inputs

    SB = float(input('Salário bruto:'))
    NMT = float(input('Tempo total de trabalho esse ano(meses):'))
    NMTO = NMT - 2

    #Cálculo INSS 

    SBB = SB    #Variável de controle p cálculo progressivo
    #Parcelas de cada faixa de salário da tabela
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

    #Cálculo do IRRF 

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
    print(f'CONTROLECONTROLECONTROLE ==== sb2-{SB2}, pd-{PD}, al-{AL} ')
    #Cálculo das parcelas
              # Parcela 1
    VEP = (SB / 12) * NMTO
    PP = VEP / 2
              # Parcela 2
    VES = (SB / 12) * NMT
    SP = VES - (PP + INSS + IRRF)

    #Output
    print(f'Descontos:\nIRRF = R${IRRF:.2f}\nINSS = R${INSS:.2f}')
    print(f'O funcionário vai receber:\n1° parcela = R${PP:.2f}\n2° parcela = R${SP:.2f}\nTotal = R${PP+SP:.2f}')

calculo_13()

