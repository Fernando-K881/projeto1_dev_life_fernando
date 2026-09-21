from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código
import motor_grafico as motor  # Utilize as funções do arquivo motor_grafico.py para desenhar na tela
                               # Por exemplo: motor.preenche_fundo(janela, [0, 0, 0]) preenche o fundo de preto


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
        for car in range(len(mapa[linha])): 
            motor.desenha_string(janela, x_mapa + car, y_mapa + linha, mapa[linha][car], VERDE_ESCURO, VERDE_ESCURO)

    for obj in objetos:
        x = obj['posicao'][0]
        y = obj['posicao'][1]
        motor.desenha_string(janela, x + x_mapa, y + y_mapa, obj['tipo'], VERDE_ESCURO, obj['cor'])

    x_jogador = pos_jogador[0]
    y_jogador = pos_jogador[1]
    motor.desenha_string(janela, x_mapa + x_jogador, y_mapa + y_jogador, JOGADOR, VERDE_ESCURO, BRANCO)

    motor.desenha_string(janela, 0, 0, CORACAO * vidas, PRETO, VERMELHO)
    motor.desenha_string(janela, vidas, 0, CORACAO * (max_vidas - vidas), PRETO, BRANCO)

    motor.desenha_string(janela, 0 , altura_tela - 1, mensagem, PRETO, BRANCO)

    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla):
    # O seu código deve atualizar o dicionário "estado" com base na tecla apertada pelo jogador
    # Por exemplo, se o jogador apertar a seta para a esquerda (o valor da variável será "ESQUERDA"), 
    # o seu código deve atualizar o dicionário estado['pos_jogador'][0] -= 1

    # Mude o valor da chave 'tela_atual' para mudar de tela
    
    # Começamos apagando a mensagem anterior, pois ela já foi mostrada no frame anterior
    estado['mensagem'] = ''

    # Escreva seu código para atualizar o dicionário "estado" com base na tecla apertada pelo jogador aqui
    # APAGUE ESTA LINHA E ESCREVA SEU CÓDIGO AQUI

    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR