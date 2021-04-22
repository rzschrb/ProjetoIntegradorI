print("PROGRAMA PARA CALCULAR FÉRIAS LÍQUIDA \n")

salIRRF = [1903.98, 2826.65, 3751.05, 4664.68] # Lista de divisão de salários - IRRF
aliIRRF = [0, 7.5, 15, 22.5, 27.5] # Lista de divisão de aliquotas em relação aos salários - IRRF
parIRRF = [0, 142.80, 354.8, 636.13, 869.36] # Lista de divisão de dedução do IRRF referente aos salários

salINSS = [1100, 2203.48, 3305.22, 6433.57] # Lista de divisão de salários - INSS
aliINSS = [7.50, 9, 12, 14] # Lista de divisão de aliquotas em relação aos salários - INSS
parINSS = [82.5, 99.31, 132.20]

taxaIRRF = 0
taxaINSS = 0

try:
    sb = float(input("Digite quanto você recebe de salário bruto R$ "))
    df = int(input("Digite quantos dias de férias você quer tirar "))

    if sb < 0 or df < 0:
        print("Os valores devem ser positivos!!")
    else:
        pv = (sb/30)*df

        print("Seu primeiro pagamento será R$", "%.2f" %pv);

        sv = pv/3

        print("Este valor represente 1/3 da férias líquidas conforme o Abono Pecuniário R$", "%.2f" %sv)

        tb = pv + sv

        print("O seu Total Bruto é de com o acréscimo de 1/3 ", "%.2f" %tb)

        #Cálculo IRRF listas do Ricardão

        if (sb <= salIRRF[0]): # Salário igual ou menor a 1903,98.
            irrf = sb * (aliIRRF[0]/100) - parIRRF[0]
        elif (sb <= salIRRF[1]): # Salário igual ou menor a 2826,65.
            taxaIRRF = sb * (aliIRRF[1]/100) - parIRRF[1]
        elif (sb <= salIRRF[2]): # Salário igual ou menor a 3751,05.
            taxaIRRF = sb * (aliIRRF[2]/100) - parIRRF[2]
        elif (sb <= salIRRF[3]): # Salário igual ou menor a 4664,68.
            taxaIRRF = sb * (aliIRRF[3]/100) - parIRRF[3]
        elif (sb < 0): # Salário deve ser positivo.
            print("O valor deve ser positivo.")
        else: # Salário maior que 4664,68.
            taxaIRRF = sb * (aliIRRF[4]/100) - parIRRF[4]

        #Cálculo INSS listas do Ricardão

        if (sb <= salINSS[0]): # Salário igual ou menor a 1100
            taxaINSS = sb * (aliINSS[0]/100)
        elif (sb <= salINSS[1]): # Salário igual ou menor a 2203,48
            sbB = sb - salINSS[0]
            taxaINSS = sbB * (aliINSS[1]/100) + parINSS[0]
        elif (sb <= salINSS[2]): # Salário igual ou menor a 3305,22
            sbB = sb - salINSS[1]
            taxaINSS = sbB * (aliINSS[2]/100) + (parINSS[0] + parINSS[1])
        elif (sb <= salINSS[3]): # Salário igual ou menor a 6433,57
            sbB = sb - salINSS[2]
            taxaINSS = sbB * (aliINSS[3]/100) + (parINSS[0] + parINSS[1] + parINSS[2])
        else: # Salário acima do teto do INSS
            taxaINSS = (salINSS[0]*(aliINSS[0]/100)) + ((salINSS[1]-salINSS[0])*(aliINSS[1]/100)) + ((salINSS[2]-salINSS[1])*(aliINSS[2]/100)) + ((salINSS[3]-salINSS[2])*(aliINSS[3]/100))

        tl = tb - (taxaIRRF + taxaINSS)

        print(f"Seu total líquido será de R$ {tl: .2f}")
        print(f"O valor do desconto da Taxa IRRF foi de: {taxaIRRF: .2f}")
        print(f"O valor do desconto da Taxa INSS foi de: {taxaINSS: .2f}")


except ValueError:
    print("Os valores devem ser númericos!!")