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

    objetos += gera_objetos(8, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(6, ESPINHO, VERDE_CLARO, largura_mapa, altura_mapa, posicoes_ocupadas)

    monstro = gera_objetos(3, MONSTRO, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)

    for mons in monstro:
        mons['vidas'] = 5
        mons['probablidade_de_ataque'] = 0.3

    objetos += monstro

    posicoes_paredes = [

    [0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7], [0,8], [0,9], [0,10], [0,11], [0,12], [0,13], [0,14], [0,15], [0,16], [0,17], [0,18], [0,19], [0,20], [0,21], [0,22], [0,23], [0,24],

    [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0], [8,0], [9,0], [10,0], [11,0], [12,0], [13,0], [14,0], [15,0], [16,0], [17,0], [18,0], [19,0], [20,0], [21,0], [22,0], [23,0], [24,0], [25,0], [26,0], [27,0], [28,0], [29,0], [30,0], [31,0], [32,0], [33,0], [34,0], [35,0], [36,0], [37,0], [38,0], [39,0], [40,0], [41,0], [42,0], [43,0], [44,0], [45,0], [46,0], [47,0], [48,0], [49,0], [50,0], [51,0], [52,0], [53,0], [54,0], [55,0], [56,0], [57,0], [58,0], [59,0], [60,0], [61,0], [62,0], [63,0], [64,0],

    [64,1], [64,2], [64,3], [64,4], [64,5], [64,6], [64,7], [64,8], [64,9], [64,10], [64,11], [64,12], [64,13], [64,14], [64,15], [64,16], [64,17], [64,18], [64,19], [64,20], [64,21], [64,22], [64,23], [64,24],

    [1,24], [2,24], [3,24], [4,24], [5,24], [6,24], [7,24], [8,24], [9,24], [10,24], [11,24], [12,24], [13,24], [14,24], [15,24], [16,24], [17,24], [18,24], [19,24], [20,24], [21,24], [22,24], [23,24], [24,24], [25,24], [26,24], [27,24], [28,24], [29,24], [30,24], [31,24], [32,24], [33,24], [34,24], [35,24], [36,24], [37,24], [38,24], [39,24], [40,24], [41,24], [42,24], [43,24], [44,24], [45,24], [46,24], [47,24], [48,24], [49,24], [50,24], [51,24], [52,24], [53,24], [54,24], [55,24], [56,24], [57,24], [58,24], [59,24], [60,24], [61,24], [62,24], [63,24],
    
    [18,3], [19,3], [20,3], [21,3], [22,3], [23,3], [24,3], [25,3], [26,3], [27,3], [28,3], [29,3], [30,3], [30,4], [30,5], [30,6], [30,7],

    [7,5], [8,5], [9,5], [10,5], [11,5], [12,5], [13,5], [14,5], [15,5], [16,5], [17,5], [18,5], [19,5], [20,5], [7,6], [7,7], [7,8], [7,9], [7,10], [7,11], [7,12], [8,12], [9,12], [10,12], [11,12], [12,12], [13,12], [14,12], [15,12], [16,12], [17,12],

    [18,8], [19,8], [20,8], [21,8], [22,8], [23,8], [24,8], [25,8], [26,8], [27,8], [28,8], [29,8], [30,8],

    [24,5], [25,5], [26,5], [27,5], [28,5], [29,5], [31,5], [32,5], [33,5], [34,5], [34,6], [34,7], [34,8], [34,9],

    [42,3], [43,3], [44,3], [45,3], [46,3], [47,3], [48,3], [49,3], [50,3], [51,3], [52,3], [53,3], [54,3], [55,3], [42,4], [42,5], [42,6], [43,6], [44,6], [45,6], [46,6], [47,6], [48,6], [49,6], [50,6], [51,6], [52,6], [53,6], [54,6], [55,6], [56,6], [56,7], [56,8], [56,9],

    [39,10], [40,10], [41,10], [42,10], [43,10], [44,10], [45,10], [46,10], [47,10], [48,10], [49,10], [50,10], [39,11], [39,12], [39,13], [40,13], [41,13], [42,13], [43,13], [44,13], [45,13], [46,13], [47,13], [47,14], [47,15], [47,16], [47,17], [47,18],

    [51,10], [52,10], [53,10], [54,10], [55,10], [56,10], [57,10], [58,10], [59,10], [60,10], [61,10], [62,10], [63,10],

    [1,16], [2,16], [3,16], [4,16], [5,16], [6,16], [7,16], [8,16], [9,16], [10,16], [10,17], [10,18], [10,19], [10,20], [7,20], [8,20], [9,20], [11,20], [12,20], [13,20], [14,20], [15,20], [16,20],

    [20,15], [21,15], [22,15], [23,15], [24,15], [25,15], [26,15], [27,15], [28,15], [29,15], [30,15], [31,15], [31,16], [31,17], [31,18], [20,18], [21,18], [22,18], [23,18], [24,18], [25,18], [26,18], [27,18], [28,18], [29,18], [30,18],

    [35,16], [36,16], [37,16], [38,16], [39,16], [40,16], [41,16], [42,16], [43,16], [44,16], [45,16], [46,16], [43,17], [43,18], [43,19], [43,20], [35,20], [36,20], [37,20], [38,20], [39,20], [40,20], [41,20], [42,20],

    [55,15], [55,16], [55,17], [55,18], [55,19], [55,20], [55,21], [55,22], [56,22], [57,22], [58,22], [59,22], [60,22], [61,22], [62,22], [63,22],

    [18,19], [18,20], [18,21], [18,22], [19,22], [20,22], [21,22], [22,22], [23,22], [24,22], [25,22], [26,22], [27,22], [28,22],
    
]

    for posicoes in posicoes_paredes:
        objetos.append({
            'tipo': PAREDE,
            'posicao': posicoes,
            'cor': MARROM_ESCURO,
        })
        posicoes_ocupadas.append(posicoes)
    
    return {
        'tela_atual': TELA_JOGO,
        'pos_jogador': pos_jogador,
        'vidas': 5,  
        'max_vidas': 5,  
        'objetos': objetos,
        'mapa': mapa,
        'mensagem': '',  
    }
