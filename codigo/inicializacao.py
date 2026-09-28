from random import randint

from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código


def gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa):
    x = randint(1, largura_mapa-2)
    y = randint(1, altura_mapa-2)
    posicao = [x, y]

    while posicao in posicoes_ocupadas:
        x = randint(1, largura_mapa-2)
        y = randint(1, altura_mapa-2)
        posicao = [x, y]
        
    posicoes_ocupadas.append(posicao)

    return posicao


def gera_objetos(quantidade, tipo, cor, largura_mapa, altura_mapa, posicoes_ocupadas):
    """
    Esta função já está pronta, você não precisa modificá-la.

    Gera uma lista de objetos do tipo especificado, com a quantidade especificada.
    Cada objeto é um dicionário com as chaves 'tipo', 'posicao' e 'cor'.

    Parâmetros:
    quantidade: quantidade de objetos a serem gerados
    tipo: tipo do objeto a ser gerado. É uma string como '❤'
    cor: cor do objeto a ser gerado. É uma lista com três elementos, como [255, 0, 0]
    largura_mapa: largura do mapa do jogo em caracteres
    altura_mapa: altura do mapa do jogo em caracteres
    posicoes_ocupadas: lista de posições ocupadas no mapa. Cada posição é uma lista com exatamente dois elementos: a posição x e a posição y.
    """
    objetos = []

    for i in range(quantidade):
        posicao = gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa)
        objetos.append({
            'tipo': tipo,
            'posicao': posicao,
            'cor': cor,
        })

    return objetos


def inicializa_estado():

    mapa = [
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
        [' '] * 65,
    ]
    
    largura_mapa = len(mapa[0])
    altura_mapa = len(mapa)
    
    pos_jogador = [largura_mapa//2, altura_mapa//2]  

    posicoes_ocupadas = [pos_jogador]
    objetos = []
    
    with open('mapa.txt', 'r') as arquivo:

        mapa_temp = arquivo.readlines()

    for i in range(len(mapa_temp)):
        for j in range(len(mapa_temp[i])):
            if mapa_temp[i][j] == 'X':
                objetos.append({
                    'tipo': PAREDE,
                    'posicao': [j,i],
                    'cor': MARROM_ESCURO,
                })
                posicoes_ocupadas.append([j,i])

    objetos += gera_objetos(8, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(6, ESPINHO, VERDE_CLARO, largura_mapa, altura_mapa, posicoes_ocupadas)

    monstro = gera_objetos(3, MONSTRO, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)

    for mons in monstro:
        mons['vidas'] = 5
        mons['probabilidade_de_ataque'] = 0.3

    objetos += monstro

    monstro_1 = gera_objetos(2, MONSTRO_1, AZUL, largura_mapa, altura_mapa, posicoes_ocupadas)

    for mons in monstro_1:
        mons['vidas'] = 3
        mons['probabilidade_de_ataque'] = 0.5

    objetos += monstro_1

    monstro_2 = gera_objetos(2, MONSTRO_2, AMARELO, largura_mapa, altura_mapa, posicoes_ocupadas)

    for mons in monstro_2:
        mons['vidas'] = 7
        mons['probabilidade_de_ataque'] = 0.2

    objetos += monstro_2



    return {
        'tela_atual': TELA_INICIAL,
        'pos_jogador': pos_jogador,
        'vidas': 5,  
        'max_vidas': 5,
        'experiencia': 0,
        'nivel': 1,  
        'objetos': objetos,
        'mapa': mapa,
        'mensagem': '',  
    }
