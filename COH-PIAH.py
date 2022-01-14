import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

#! vou definir funções pra calcular cada um dos aspectos linguísticos

#*-------------------------------
def calcula_wal(texto):
    soma = total_palavras = 0
    
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            total_palavras += len(separa_palavras(frase))
            for palavra in separa_palavras(frase):
                soma += len(palavra)
    
    wal = soma/total_palavras
    
    return wal
    #calcula o tamanho médio por palavra: soma dos tamanhos/total de palavras

#*-------------------------------
def calcula_ttr(texto):
    total_palavras = total_palavras_dif = 0
    
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            total_palavras += len(separa_palavras(frase))
            total_palavras_dif += n_palavras_diferentes(separa_palavras(frase)) 
            
    ttr = total_palavras_dif/total_palavras
    
    return ttr   
    #calcula a relação Type-Token: número de palavras dif/total de palavras

#*-------------------------------
def calcula_hlr(texto):
    total_palavras = total_palavras_uni = 0
    
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            total_palavras += len(separa_palavras(frase))
            total_palavras_uni += n_palavras_unicas(separa_palavras(frase))
            
    hlr = total_palavras_uni/total_palavras
    
    return hlr 
    #calcula a razão Hapax Legomana: número de palavras únicas/total de palavras

#*-------------------------------
def calcula_sal(texto):
    total_carac = 0
    
    for sentenca in separa_sentencas(texto):       
        total_carac += len(sentenca) - 1
    
    sal = total_carac/len(separa_sentencas(texto))
    
    return sal
    #calcula o tamanho médio de sentença: soma dos números de caracteres/total de sentenças
    
#*-------------------------------
def calcula_sac(texto):
    total_frases = 0
    
    for sentenca in separa_sentencas(texto):
        total_frases += len(separa_frases(sentenca)) #acrescenta o total de frases em cada sentença
    
    sac = total_frases/len(separa_sentencas(texto))
    
    return sac
    #calcula a complexidade de sentença: total de frases/total de sentenças

#*-------------------------------
def calcula_pal(texto):
    total_carac = total_frases = 0
    
    for sentenca in separa_sentencas(texto):
        
        total_frases += len(separa_frases(sentenca))
        
        for frase in separa_frases(sentenca):
            total_carac += len(frase) - 1
    
    pal = total_carac/total_frases
    
    return pal    
    #calcula o tamanho médio de frase: soma dos núm. de caracteres em cada frase/total de frases

#*-------------------------------
def compara_assinatura(as_a, as_b):
    soma = 0
    
    for i in range(6):
        soma += abs(as_a[i] - as_b[i])
    
    sim = soma/6
    
    return sim 
    
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    # grau de similaridade = soma(abs(TLa - TLb))/6
    #assinatura é uma lista [wal, ttr, hlr, sal, sac, pal]

#*-------------------------------
def calcula_assinatura(texto):
    assinatura = [calcula_wal(texto), 
                  calcula_ttr(texto), 
                  calcula_hlr(texto), 
                  calcula_sal(texto), 
                  calcula_sac(texto), 
                  calcula_pal(texto)]
    
    return assinatura
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

#*-------------------------------
def avalia_textos(textos, ass_cp):
    assinaturas = []
    
    for texto in textos:
        assinaturas.append(compara_assinatura(ass_cp, calcula_assinatura(texto)))
    
    num = assinaturas.index(min(assinaturas)) 
    
    return num + 1
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero 
    (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
ass_cp = le_assinatura()
textos = le_textos()
    
print('O autor do texto', avalia_textos(textos, ass_cp), 'está infectado com COH-PIAH')