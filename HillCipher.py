import random
alfabeto = {'z':0,'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'0':26,'1':27,'2':28,'3':29,'4':30,'5':31,'6':32,'7':33,'8':34,'9':35}
#alfabeto e digitos de 0 a 9, a criptografia sera feita usando calculos de 0 a 9
#getkey
def get_key(val):                       #recupera a chave de um valor dentro do dicionario acima
    for key, value in alfabeto.items():
      if val == value:
            return key
def gerar_chave():
    inversos_modulares = {1:1,5:29,7:31,11:23,13:25,17:17,19:19,23:11,25:13,29:5,31:7,35:35}#todos os inversos modulares mod36
    chave = [[],[]]
    while True:                               #gera uma chave aleatória com elementos inteiros de
        for i in range(2):                    #1 a 1000 invertível mod36
            x = random.randint(1, 1000)
            chave[0].append(x)
        for i in range(2):
            x = random.randint(1, 1000)
            chave[1].append(x)

        determinante_chave1 = (chave[0][0] * chave[1][1] - chave[0][1] * chave[1][0])
        if determinante_chave1 < 0:                                 #calcula o determinante da matriz para saber se é invertível,
            determinante_chave1 = determinante_chave1*(-1)          #caso seja, retorna a chave, caso não, faz o processo novamente.
        if determinante_chave1%36 not in inversos_modulares:
            chave.clear()
            chave = [[],[]]
        else:break
    return chave
def encriptação(senha):   #faz a encriptação da mensagem segundo a cifra de hill,
    chave = gerar_chave()
# matrizes                                      #guardando num banco de dados a senha codificada e a chave
    matriz_senha = []
    matriz_linha = []
    coluna = []
    senha_linha = ''
    for char in senha:
        coluna.append(alfabeto[char])
        if len(coluna) == 2:
            matriz_senha.append(coluna.copy())
            coluna.clear()
    while len(matriz_linha) < len(matriz_senha):
        for n_coluna in chave:
            for n_linha in matriz_senha:
                coluna.append(n_coluna[0]*n_linha[0]+n_coluna[1]*n_linha[1])
                if len(coluna) == 2:
                    matriz_linha.append(coluna.copy())
                    coluna.clear()
#correção da matriz codificada
    for index in range(len(matriz_linha)):
        if len(matriz_linha[index])%2 != 0:
            matriz_linha[index].append(0)
#matriz codificada mod26
    for j in matriz_linha:
        for i in range(len(j)):
            j[i] = j[i]%36
#senha_linha
    for coluna in matriz_linha:
        senha_linha += get_key(coluna[0])
    for coluna in matriz_linha:
        senha_linha += get_key(coluna[1])

    return (chave,senha_linha)

def permitir_acesso(senha,chave,senha_linha): #utiliza os parametros chave e senha para fazer a mesma multiplicação matricial
    tupla = encriptação(senha,chave)          #feita na encriptação, então compara a senha digitada encriptada e a senha armazenada encriptada
    if tupla[1] == senha_linha:
        return True

