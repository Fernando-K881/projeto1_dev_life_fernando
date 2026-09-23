from constantes import *  
from random import randint,random                                  
import motor_grafico as motor  


def desenha_tela(janela, estado, altura_tela, largura_tela):
    mapa = estado['mapa']
    mensagem = estado['mensagem']
    vidas = estado['vidas']
    objetos = estado['objetos']
    pos_jogador = estado['pos_jogador']
    max_vidas = estado['max_vidas']

    motor.preenche_fundo(janela, PRETO)

    x_mapa = (largura_tela - len(mapa[0])) // 2
    y_mapa = (altura_tela - len(mapa)) // 2


    for linha in range(len(mapa)):
        for caractere in range(len(mapa[linha])): 
            motor.desenha_string(janela, x_mapa + caractere, y_mapa + linha, mapa[linha][caractere], VERDE_ESCURO, VERDE_ESCURO)

    for obj in objetos:
        x = obj['posicao'][0]
        y = obj['posicao'][1]

        if obj['tipo'] == PAREDE:
            motor.desenha_string(janela, x + x_mapa, y + y_mapa, obj['tipo'], MARROM_MAIS_ESCURO, obj['cor'])
        else:
            motor.desenha_string(janela, x + x_mapa, y + y_mapa, obj['tipo'], VERDE_ESCURO, obj['cor'])

    x_jogador = pos_jogador[0]
    y_jogador = pos_jogador[1]
    motor.desenha_string(janela, x_mapa + x_jogador, y_mapa + y_jogador, JOGADOR, VERDE_ESCURO, BRANCO)

    motor.desenha_string(janela, 0, 0, CORACAO * vidas, PRETO, VERMELHO)
    motor.desenha_string(janela, vidas, 0, CORACAO * (max_vidas - vidas), PRETO, BRANCO)

    motor.desenha_string(janela, 0 , altura_tela - 1, mensagem, PRETO, BRANCO)

    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla):
    estado['mensagem'] = ''

    nova_posicao = [
        estado['pos_jogador'][0],
        estado['pos_jogador'][1]
    ]

    if tecla == 'ESQUERDA':
        if nova_posicao[0] > 0:
            nova_posicao[0] -= 1

    elif tecla == 'DIREITA':
        if nova_posicao[0] < len(estado['mapa'][0]) - 1:
            nova_posicao[0] += 1

    elif tecla == 'CIMA':
        if nova_posicao[1] > 0:
            nova_posicao[1] -= 1

    elif tecla == 'BAIXO':
        if nova_posicao[1] < len(estado['mapa']) - 1:
            nova_posicao[1] += 1

    parede = False
    monstro = False
    monstro_ataca = False

    for obj in estado['objetos']:
        if obj['tipo'] == PAREDE:
            if nova_posicao == obj['posicao']:
                parede = True
    
        elif obj['tipo'] == MONSTRO:
            if nova_posicao == obj['posicao']:
                monstro = True
                sorteio = random()

                if sorteio < obj['probabilidade_de_ataque']:
                    estado['vidas'] -= 1
                    estado['mensagem'] = 'O monstro te atacou'

                    if estado['vidas'] <= 0:
                        estado['tela_atual'] = SAIR
                else:
                    obj['vidas'] -= 1
                    monstro_ataca = obj
                    estado['mensagem'] = 'Você atacou o monstro'

                    if obj['vidas'] <= 0:
                        estado['objetos'].remove(obj)
                        estado['pos_jogador'] = nova_posicao
                        estado['mensagem'] = 'O monstro morreu'

    if parede:
        estado['mensagem'] = 'Você não pode atravessar a parede'

    elif monstro == False:
        estado['pos_jogador'] = nova_posicao


    for objeto in estado['objetos']:
        if estado['pos_jogador'] == objeto['posicao']:
            if objeto['tipo'] == CORACAO:
                estado['objetos'].remove(objeto)

                if estado['vidas'] < estado['max_vidas']:
                    estado['vidas'] += 1
                    estado['mensagem'] = 'Você ganhou uma vida'
                else:
                    estado['mensagem'] = 'Sua vida já está no máximo'

            elif objeto['tipo'] == ESPINHO:
                estado['vidas'] -= 1
                estado['mensagem'] = 'Você perdeu uma vida'

            if estado['vidas'] <= 0:
                estado['tela_atual'] = SAIR

    teclas = ['ESQUERDA', 'DIREITA', 'CIMA', 'BAIXO']

    for ob in estado['objetos']:
        if ob['tipo'] == MONSTRO and ob != monstro_ataca:
            direcao = teclas[int(random() * 4)]
            nova_posicao_monstro = [
                    ob['posicao'][0],
                    ob['posicao'][1]
                ]
            
            if direcao == 'ESQUERDA':
                nova_posicao_monstro[0] -= 1

            elif direcao == 'DIREITA':
                nova_posicao_monstro[0] += 1

            elif direcao == 'CIMA':
                nova_posicao_monstro[1] -= 1

            elif direcao == 'BAIXO':
                nova_posicao_monstro[1] += 1

            if nova_posicao_monstro[0] >= 0 and nova_posicao_monstro[0] < len(estado['mapa'][0]):
                if nova_posicao_monstro[1] >= 0 and nova_posicao_monstro[1] < len(estado['mapa']):
                    if nova_posicao_monstro not in [obj['posicao'] for obj in estado['objetos']]:
                        ob['posicao'] = nova_posicao_monstro

    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR