from constantes import *
import motor_grafico as motor

def desenha_tela(janela, estado, altura, largura):
    # Você pode usar esta função como base para a sua função desenha_tela do arquivo tela_jogo.py
    # Esta tela é mostrada quando o jogador aperta a tecla 'i' (você provavelmente vai querer 
    # alterar este arquivo no nível avançado)
    motor.preenche_fundo(janela, CINZA)

    motor.desenha_string(janela, 1, 1, 'Sair aperte "q"', PRETO, BRANCO)
    motor.desenha_string(janela, 1, 2, 'Jogar novamente "p"', PRETO, BRANCO)
    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR