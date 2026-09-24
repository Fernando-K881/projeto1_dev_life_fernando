from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura, largura):
    # Você pode usar esta função como base para a sua função desenha_tela do arquivo tela_jogo.py
    # Esta tela é mostrada quando o jogador aperta a tecla 'i' (você provavelmente vai querer 
    # alterar este arquivo no nível avançado)
    motor.preenche_fundo(janela, CINZA)

    motor.desenha_string(janela, 1, 2, 'Bem vindo(a) ao jogo, aperte a tecla "n" para jogar', PRETO, BRANCO)
    motor.desenha_string(janela, 1, 4, 'Para sair aperte a tecla "q"', PRETO, BRANCO)
    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada == 'n':
        estado['tela_atual'] = TELA_INSTRUCAO
    elif tecla_apertada in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR