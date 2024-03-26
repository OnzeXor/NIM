
def usuario_escolhe_jogada(n,m):
    jogado = 0
    while jogado!=1:
        a = int(input('quantas pessas deseja retirar?'))
        if a <= 0 or a>m or a>n:
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            jogado=1
       
    if jogado ==1:
        print('voce tirou',a,'peças')
        return a
    


def computador_escolhe_jogada(n,m):
    p=1
    a=0
    while m>=p:
        
        if ((n-p)%(m+1)) == 0:
            a=p
        p=p+1
    if a ==0:
        if p>n:
            return n
        if p<n: 
            return p   
        print('o pc tirou',p,'pessas do tabuleiro')
        print(a)
    else:
        print('o pc tirou',a,'pessas do tabuleiro')
        return a 

    


def partida():
    def jogada(k,n,m):
        
        while n >=0:
            if k == 0 and n>0:
                a = usuario_escolhe_jogada(n,m)
                n = n - a
                print('sobrou',n,'pessas no tabuleiro') 
                if n>0:
                    k =1
                else:
                    print('voce venceu')
                    return
            if k ==1 and n>0:
                j = computador_escolhe_jogada(n,m)
                n = n-j
                print('sobrou',n,'pessas no tabuleiro') 
                if n>0:
                    k =0
                else:
                    print('O computador venceu')
                    return
    
        if n==0:
            print('o Jogo acabou')
    inicio = False
    if inicio == False:
        n = int(input('Quantas peças? '))
        m = int(input('Limite de peças por jogada? '))
        inicio = True
    
    if (n%(m+1)) == 0 and inicio == True:
        print('Você começa')
        jogada(0,n,m)
     
    if (n%(m+1)) != 0 and inicio == True:
        print('O PC começa')
        jogada(1,n,m)
    return

def start():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar uma partida isolada')
    a = input('2 - para jogar um campeonato ')
    if a == "1":
        print('Voce escolheu uma partida única!')
        partida()
    if a == "2":
        print('Voce escolheu um campeonato!')
        partida()
        partida()
        partida()
start()
