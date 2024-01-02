import os

comprimido = []                            #lista que vai armazenar o texto comprimido
descomprimido = []                         #lista que vai armazenar o texto descomprimido

# COMPRESSÃO
with open("espacos_branco.txt", "r") as arquivo: #abre o arquivo original
    texto = arquivo.read()                          #le o arquivo, armazena na var texto e fecha arq

caracteres = list(texto)                   #var caracteres armazena o texto em lista, assim podemos manipular cada caractere individualmente
qnt_brancos = 0                            #variável que vai guardar a qntd de espaços em branco em cada sequência

for caractere in caracteres:  #loop pelos caracteres
    if caractere == " ":  #se o caractere atual for espaço em branco
        qnt_brancos += 1  #incrementa a qntd de espaços em branco
    else:
        if qnt_brancos >= 1:  #se ñ for espaço em branco e houver uma sequência de espaços
            comprimido.append("#" + str(qnt_brancos))  #add a sequência à lista comprimido
        if caractere.isdigit():     #se o caractere atual for um número
            comprimido.append("|" + caractere)     #add um | antes do caractere
        else:
            comprimido.append(caractere)  #se ñ for um num, add o caractere atual a comprimido
        qnt_brancos = 0               #zera a sequência

comprimido = "".join(comprimido)           #junta os itens da lista (cada caractere) numa string

with open("comprimido.txt", "w") as arquivo_comprimido:  #cria o novo arquivo comprimido.txt
    texto_comprimido = arquivo_comprimido.write(comprimido) #escreve a lista comprimido no arquivo comprimido.txt e fecha arq



# DESCOMPRESSÃO
with open("comprimido.txt", "r") as arquivo_c:    #abre o arquivo comprimido
    texto_c = arquivo_c.read()                 #le o arquivo comprimido, armazena na var texto_c e fecha arq

caracteres = list(texto_c)                 #var caracteres armazena o texto_c em lista, assim podemos manipular cada caractere individualmente

for i, caractere in enumerate(caracteres):      #loop vai percorrer a lista (caracteres), acompanhando o índice (i) e o valor do item (caractere)
    if caractere == "#":
        qnt_brancos = ""                        #se o caractere atual for uma #, limpa a var qnt_brancos, podemos estar numa nova seq
        while caracteres[i+1].isdigit():        #loop ocorre enquanto o próximo caractere for um dígito. isso serve para garantir que o multiplicador da flag será reconhecido, msm q seja maior q 9
            qnt_brancos += caracteres[i+1]          #o caractere numérico é add à var qnt_brancos e vai pro próx. índice
            i += 1
        if qnt_brancos:                         #checa se a var qnt_brancos guarda um valor diferente de 0, converte a var para int 
            qnt_brancos = int(qnt_brancos)         
            descomprimido.append(" " * qnt_brancos)     #e multiplica esse número por espaços em branco, add à lista descomprimido
        else:
           descomprimido.append("#")            #se a var qnt_brancos estiver vazia, a # encontrada é um caractere e ñ uma flag. ela é add à lista descomprimido                                  
    elif caractere == "|" and caracteres[i+1].isdigit():  #se o caractere atual for uma |, sabemos que era um número do texto original, ñ um multiplicador de flag
        descomprimido.append(caracteres[i+1])               #o número que procede a | é add à lista descomprimido
    elif not caractere.isdigit():
        descomprimido.append(caractere)         #se o caractere atual ñ for um dígito (já foram incluídos), ele é add à lista descomprimido

descomprimido = "".join(descomprimido)     #junta os itens da lista (cada caractere) numa string

with open("descomprimido.txt", "w") as arquivo_descomprimido: #cria o novo arquivo descomprimido.txt
    texto_descomprimido = arquivo_descomprimido.write(descomprimido) #escreve a lista descomprimido no arquivo descomprimido.txt e fecha arq