# Modules | Class | Functions for RH System

class SistemaRH:
    def __init__(self, salarioBruto, taxaINSS, taxaIRRF):
        self.salarioBruto = salarioBruto
        self.taxaINSS = taxaINSS
        self.taxaIRRF = taxaIRRF

    def set_salarioBruto(self, salarioBruto):
        self.salarioBruto = salarioBruto

    def get_salarioBruto(self):
        return self.salarioBruto

    def calc_inss(self, salarioBruto):

        salINSS = [1100, 2203.48, 3305.22, 6433.57]  # Lista de divisão de salários - INSS
        aliINSS = [7.50, 9, 12, 14]  # Lista de divisão de aliquotas em relação aos salários - INSS
        parINSS = [82.5, 99.31, 132.20]

        taxaINSS = 0
        salarioBrutoB = salarioBruto

        if (self.salarioBruto <= salINSS[0]):  # Salário igual ou menor a 1100
            taxaINSS = salarioBruto * (aliINSS[0] / 100)
        elif (self.salarioBruto <= salINSS[1]):  # Salário igual ou menor a 2203,48
            salarioBrutoB = self.salarioBruto - salINSS[0]
            taxaINSS = salarioBrutoB * (aliINSS[1] / 100) + parINSS[0]
        elif (self.salarioBruto <= salINSS[2]):  # Salário igual ou menor a 3305,22
            salarioBrutoB = self.salarioBruto - salINSS[1]
            taxaINSS = salarioBrutoB * (aliINSS[2] / 100) + (parINSS[0] + parINSS[1])
        elif (self.salarioBruto <= salINSS[3]):  # Salário igual ou menor a 6433,57
            salarioBrutoB = self.salarioBruto - salINSS[2]
            taxaINSS = salarioBrutoB * (aliINSS[3] / 100) + (parINSS[0] + parINSS[1] + parINSS[2])
        else:  # Salário acima do teto do INSS
            taxaINSS = (salINSS[0] * (aliINSS[0] / 100)) + ((salINSS[1] - salINSS[0]) * (aliINSS[1] / 100)) + (
                        (salINSS[2] - salINSS[1]) * (aliINSS[2] / 100)) + (
                                   (salINSS[3] - salINSS[2]) * (aliINSS[3] / 100))

        self.taxaINSS = taxaINSS

        return self.taxaINSS

    def get_taxaINSS(self):
        return self.taxaINSS

    def calc_irrf(self, salarioBruto, taxaINSS):

        salIRRF = [1903.98, 2826.65, 3751.05, 4664.68]  # Lista de divisão de salários - IRRF
        aliIRRF = [0, 7.5, 15, 22.5, 27.5]  # Lista de divisão de aliquotas em relação aos salários - IRRF
        parIRRF = [0, 142.80, 354.8, 636.13, 869.36]  # Lista de divisão de dedução do IRRF referente aos salários

        taxaIRRF = 0

        if ((salarioBruto - taxaINSS) <= salIRRF[0]):  # Salário igual ou menor a 1903,98.
            taxaIRRF = (salarioBruto * 0)
        elif ((salarioBruto - taxaINSS) <= salIRRF[1]):  # Salário igual ou menor a 2826,65.
            taxaIRRF = (salarioBruto * (aliIRRF[1] / 100)) - parIRRF[1]
        elif ((salarioBruto - taxaINSS) <= salIRRF[2]):  # Salário igual ou menor a 3751,05.
            taxaIRRF = (salarioBruto * (aliIRRF[2] / 100)) - parIRRF[2]
        elif ((salarioBruto - taxaINSS) <= salIRRF[3]):  # Salário igual ou menor a 4664,68.
            taxaIRRF = (salarioBruto * (aliIRRF[3] / 100)) - parIRRF[3]
        else:  # Salário maior que 4664,68.
            taxaIRRF = (salarioBruto * (aliIRRF[4] / 100)) - parIRRF[4]

        self.taxaIRRF = taxaIRRF

        return self.taxaIRRF

    def get_taxaIRRF(self):
        return self.taxaIRRF

    def calc_liquidsal(self, salarioBruto, taxaINSS, taxaIRRF):

        salarioLiquido = self.salarioBruto - (self.taxaINSS + self.taxaIRRF)

        self.salarioLiquido = salarioLiquido

        return self.salarioLiquido

    def get_salarioLiquido(self):
        return self.salarioLiquido

    def calc_ferias(self, salarioBruto, taxaINSS, taxaIRRF):

        try:
            diasFerias = int(input("\nDigite quantos dias de férias você deseja tirar: "))

            if diasFerias <= 0:
                print('\n\033[91m' + "ERRO: " + '\033[0m' + f"Você não pode tirar {diasFerias} dias de férias.")
            else:
                primeiroValor = (self.salarioBruto / 30) * diasFerias

                segundoValor = primeiroValor / 3

                valorBruto = primeiroValor + segundoValor

                valorTotal = valorBruto - (self.taxaINSS + self.taxaIRRF)

                print(f"\nPrimeiro pagamento: R$ {primeiroValor:.2f}")
                print(f"Pagamento referente a 1/3 das Férias Liquidas (Abono Pecuniário): R$ {segundoValor:.2f}")
                print(f"Total bruto com o 1/3: R$ {valorBruto:.2f}")
                print(f"Total líquido: R$ {valorTotal:.2f}")

        except ValueError:
            return "O valor deve ser númerico."

    def calc_decterceiro(self, salarioBruto, taxaINSS, taxaIRRF):

        while True:
            try:
                nmt = float(input('Tempo total de trabalho desde outubro do ano passado (em meses): '))
                if nmt <= 0:
                    raise
                else:
                    break

                valorPrimario = (self.salarioBruto / 12) * nmt
                primeiraParcela = valorPrimario / 2
                segundaParcela = primeiraParcela - (self.taxaINSS + self.taxaIRRF)

                print(f'O funcionário vai receber: ')
                print(f'Primeira Parcela: R$ {primeiraParcela:.2f}')
                print(f'Segunda Parcela: R$ {segundaParcela:.2f}')
                print(f'Total: R${primeiraParcela + segundaParcela}')
                return (primeiraParcela + segundaParcela)

            except ValueError:
                print("Erro no valor")
            break
