# Cálculo do Salário Líquido
# Variaveis/Listas

salIRRF = [1903.98, 2826.65, 3751.05, 4664.68] # Lista de divisão de salários - IRRF
aliIRRF = [0, 7.5, 15, 22.5, 27.5] # Lista de divisão de aliquotas em relação aos salários - IRRF
parIRRF = [0, 142.80, 354.8, 636.13, 869.36] # Lista de divisão de dedução do IRRF referente aos salários

salINSS = [1100, 2203.48, 3305.22, 6433.57] # Lista de divisão de salários - INSS
aliINSS = [7.50, 9, 12, 14] # Lista de divisão de aliquotas em relação aos salários - INSS

salarioBruto = 0
taxaIRRF = 0
taxaINSS = 0

try:
    salarioBruto = float(input("Informe seu salário bruto: "))
# IRRF
    if (salarioBruto <= salIRRF[0]): # Salário igual ou menor a 1903,98.
        taxaIRRF = salarioBruto * (aliIRRF[0]/100) - parIRRF[0]
    elif (salarioBruto <= salIRRF[1]): # Salário igual ou menor a 2826,65.
        taxaIRRF = salarioBruto * (aliIRRF[1]/100) - parIRRF[1]
    elif (salarioBruto <= salIRRF[2]): # Salário igual ou menor a 3751,05.
        taxaIRRF = salarioBruto * (aliIRRF[2]/100) - parIRRF[2]
    elif (salarioBruto <= salIRRF[3]): # Salário igual ou menor a 4664,68.
        taxaIRRF = salarioBruto * (aliIRRF[3]/100) - parIRRF[3]
    elif (salarioBruto < 0): # Salário deve ser positivo.
        print("O valor deve ser positivo.")
    else: # Salário maior que 4664,68.
        taxaIRRF = salarioBruto * (aliIRRF[4]/100) - parIRRF[4]
# INSS
    if (salarioBruto <= salINSS[0]): # Salário igual ou menor a 1100
        taxaINSS = salarioBruto * (aliINSS[0]/100)
    elif (salarioBruto <= salINSS[1]): # Salário igual ou menor a 2203,48
        taxaINSS = salarioBruto * (aliINSS[1]/100)
    elif (salarioBruto <= salINSS[2]): # Salário igual ou menor a 3305,22
        taxaINSS = salarioBruto * (aliINSS[2]/100)
    elif (salarioBruto <= salINSS[3]): # Salário igual ou menor a 6433,57
        taxaINSS = salarioBruto * (aliINSS[3]/100)
    else: # Salário acima do teto do INSS
        taxaINSS = (salINSS[0]*(aliINSS[0]/100)) + ((salINSS[1]-salINSS[0])*(aliINSS[1]/100)) + ((salINSS[2]-salINSS[1])*(aliINSS[2]/100)) + ((salINSS[3]-salINSS[2])*(aliINSS[3]/100))

except ValueError:
    print("\nO valor informado não é compativel com o programa.\n")

print("Salário Bruto Informado: ", salarioBruto)
print("Taxa do IRRF: ", taxaIRRF)
print("Taxa do INSS: ", taxaINSS)
print("Valor Final: ", salarioBruto - (taxaIRRF + taxaINSS))