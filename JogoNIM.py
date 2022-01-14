def computador_escolhe_jogada(n,m):
    for i in range(m):
        if (n-i)%(m+1) == 0:
            jogada = i
            break
        else:
            jogada = m 
            
    return jogada
    #retorna a quantidade de peças que o computador retira pra ganhar

def usuario_escolhe_jogada(n,m):
    jogada = int(input(('Quantas peças você vai tirar? ')).split()[0])
    
    while jogada > m or jogada > n or jogada <= 0:
        jogada = int(input(('\nOops! Jogada inválida! Tente de novo.\n\nQuantas peças você vai tirar? ')).split()[0])
    
    return jogada
    #pede a jogada do jogador, verifica se é válida; se for, devolve o valor; c.c., solicita outra jogada
    
def partida():
    num_pecas = int(input('Quantas peças? ').split()[0]) 
    
    lim_pecas = int(input('Limite de peças por jogada? ').split()[0])
    
    ult_jogada = inicio = cont = None
    
    while num_pecas != 0:
        if num_pecas < lim_pecas:
            lim_pecas = num_pecas
        while cont != 1: 
            if num_pecas%(lim_pecas+1) == 0:
                print('\nVocê começa!\n')
                inicio = 0
            else:
                print('\nComputador começa!\n')
                inicio = 1
            cont = 1
            ult_jogada = inicio
        
        if ult_jogada == 0:
            pecas_ret = usuario_escolhe_jogada(num_pecas,lim_pecas)
                
            if pecas_ret == 1:
                print('Você tirou uma peça.')
            else:
                print('Você tirou', pecas_ret, 'peças.')
                
            ult_jogada = 1

        else:
            pecas_ret = computador_escolhe_jogada(num_pecas,lim_pecas)
                
            if pecas_ret == 1:
                print('O computador tirou uma peça.')
            else:
                print('O computador tirou', pecas_ret, 'peças.')
                
            ult_jogada = 0
        
        num_pecas -= pecas_ret
        
        if num_pecas == 1:
            print('Agora resta apenas uma peça no tabuleiro.\n')
        elif num_pecas != 0:
            print('Agora restam', num_pecas, 'peças no tabuleiro.\n')
        else:
            continue
    
    if ult_jogada == 1:
        print('Fim do jogo! Você ganhou!')
    else:
        print('Fim do jogo! O computador ganhou!')
        
    return ult_jogada
    #pede n e m ao jogador e começa o jogo; imprime na tela, a cada jogada, a quantidade de peças removidas na rodada anterior e a quantidade de peças restantes
    
def campeonato():
    comp = jog = 0
    
    for i in range(3):
        print('\n**** Rodada', i+1, '****\n')
        
        if partida() == 1:
            jog += 1
        else:
            comp += 1
    
    print('\n**** Final do campeonato! ****\n\nPlacar: Você', jog, 'X', comp, 'Computador')
    
    return None
    #faz três partidas e retorna o placar como Placar: Você ??? X ??? Computador
    
opcao = int(input(('Bem vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato ')).split()[0])
    
if opcao == 1:
    print('\nVocê escolheu uma partida isolada!')
    partida()
else:
    print('\nVocê escolheu um campeonato!')
    campeonato()