from constantes import *  
from random import random                                  
import motor_grafico as motor  


def desenha_tela(janela, estado, altura_tela, largura_tela): # desenha o mapa, objetos, jogador e informações na tela.
    mapa = estado['mapa']
    mensagem = estado['mensagem']
    vidas = estado['vidas']
    objetos = estado['objetos']
    pos_jogador = estado['pos_jogador']
    max_vidas = estado['max_vidas']

    motor.preenche_fundo(janela, CINZA)

    # centraliza o mapa na janela
    x_mapa = (largura_tela - len(mapa[0])) // 2
    y_mapa = (altura_tela - len(mapa)) // 2

    # desenha o terreno do mapa
    for linha in range(len(mapa)):
        for caractere in range(len(mapa[linha])): 
            motor.desenha_string(janela, x_mapa + caractere, y_mapa + linha, mapa[linha][caractere], VERDE_ESCURO, VERDE_ESCURO)

    # desenha paredes e itens/monstros nas posições corretas
    for obj in objetos:
        x = obj['posicao'][0]
        y = obj['posicao'][1]

        if obj['tipo'] == PAREDE:
            motor.desenha_string(janela, x + x_mapa, y + y_mapa, obj['tipo'], MARROM_MAIS_ESCURO, obj['cor'])
        else:
            motor.desenha_string(janela, x + x_mapa, y + y_mapa, obj['tipo'], VERDE_ESCURO, obj['cor'])

    x_jogador = pos_jogador[0]
    y_jogador = pos_jogador[1]

    # desenha o jogador sobre o mapa
    motor.desenha_string(janela, x_mapa + x_jogador, y_mapa + y_jogador, JOGADOR, VERDE_ESCURO, BRANCO)

    # exibe vidas, nível, experiência e mensagens do jogo
    motor.desenha_string(janela, 0, 0, CORACAO * vidas, CINZA, VERMELHO)
    motor.desenha_string(janela, vidas, 0, CORACAO * (max_vidas - vidas), CINZA, BRANCO)

    motor.desenha_string(janela, 0, 1, 'Nivel: ' + str(estado['nivel']), CINZA, BRANCO)
    motor.desenha_string(janela, 0, 2, 'XP: ' + str(estado['experiencia']), CINZA, BRANCO)

    motor.desenha_string(janela, 0 , altura_tela - 1, mensagem, PRETO, BRANCO)

    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla): # atualiza posição do jogador, combate, itens e movimento dos monstros
    estado['mensagem'] = ''

    # calcula a possível nova posição conforme a tecla pressionada
    nova_posicao = [
        estado['pos_jogador'][0],
        estado['pos_jogador'][1]
    ]

    # impede o jogador de sair dos limites do mapa
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

    # verifica colisão com parede ou início de combate com monstros
    for obj in estado['objetos']:
        if obj['tipo'] == PAREDE:
            if nova_posicao == obj['posicao']:
                parede = True
    
        elif obj['tipo'] == MONSTRO or obj['tipo'] == MONSTRO_1 or obj['tipo'] == MONSTRO_2:
            if nova_posicao == obj['posicao']:
                monstro = True
                monstro_ataca = obj
                sorteio = random() # sorteia se o monstro ataca ou se o jogador consegue atacá-lo

                if sorteio < obj['probabilidade_de_ataque']:
                    estado['vidas'] -= 1
                    estado['mensagem'] = 'O monstro te atacou'
                    
                    # verifica se a vida chegou a zero após coletar item ou pisar no espinho
                    if estado['vidas'] <= 0: 
                        estado['tela_atual'] = TELA_GAMEOVER
                else:
                    obj['vidas'] -= 1
                    monstro_ataca = obj
                    estado['mensagem'] = 'Você atacou o monstro'

                    # monstro derrotado: remove o monstro e concede experiência
                    if obj['vidas'] <= 0:
                        estado['objetos'].remove(obj)
                        estado['pos_jogador'] = nova_posicao
                        estado['experiencia'] += 1
                        # a cada 3 XP, o jogador sobe de nível e ganha vida máxima
                        if estado['experiencia'] >= 3:
                            estado['nivel'] += 1
                            estado['experiencia'] = 0
                            estado['max_vidas'] += 1
                            estado['vidas'] += 1
                            estado['mensagem'] = 'Você passou de nível'
                        
                        else:
                            estado['mensagem'] = 'O monstro morreu'

    # só move o jogador se não houver parede ou monstro na posição
    if parede:
        estado['mensagem'] = 'Você não pode atravessar a parede'

    elif monstro == False:
        estado['pos_jogador'] = nova_posicao

    # aplica o efeito dos itens quando o jogador passa sobre eles
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
                estado['tela_atual'] = TELA_GAMEOVER

    teclas = ['ESQUERDA', 'DIREITA', 'CIMA', 'BAIXO']

    for ob in estado['objetos']:
        if ob['tipo'] == MONSTRO or ob['tipo'] == MONSTRO_1 or ob['tipo'] == MONSTRO_2:
            if ob != monstro_ataca:
                # cada tipo de monstro possui um padrão de movimento
                if ob['tipo'] == MONSTRO: 
                    direcao = teclas[int(random() * 4)]
                
                elif ob['tipo'] == MONSTRO_1:
                    direcoes = ['CIMA', 'BAIXO']
                    direcao = direcoes[int(random() * 2)]
                
                elif ob['tipo'] == MONSTRO_2:
                    direcoes = ['ESQUERDA', 'DIREITA']
                    direcao = direcoes[int(random() * 2)]
                
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

                # só move se a posição estiver dentro do mapa e desocupada
                if nova_posicao_monstro[0] >= 0 and nova_posicao_monstro[0] < len(estado['mapa'][0]):
                    if nova_posicao_monstro[1] >= 0 and nova_posicao_monstro[1] < len(estado['mapa']):
                        ocupado = False

                        if nova_posicao_monstro == estado['pos_jogador']:
                            ocupado = True

                        for object in estado['objetos']:
                            if nova_posicao_monstro == object['posicao']:
                                ocupado = True

                        if ocupado == False:
                            ob['posicao'] = nova_posicao_monstro

    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR