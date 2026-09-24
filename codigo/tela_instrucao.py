from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura, largura):
    # Você pode usar esta função como base para a sua função desenha_tela do arquivo tela_jogo.py
    # Esta tela é mostrada quando o jogador aperta a tecla 'i' (você provavelmente vai querer 
    # alterar este arquivo no nível avançado)
    motor.preenche_fundo(janela, CINZA)

    motor.desenha_string(janela,  1,  2, 'INSTRUCOES', PRETO, BRANCO)
    motor.desenha_string(janela, 1, 4,'Use as setas para movimentar o jogador',PRETO, BRANCO)
    motor.desenha_string(janela, 1, 5, 'Pegue os coracoes e evite os espinhos.', PRETO, BRANCO)
    motor.desenha_string(janela, 1, 6, 'Lute contra os monstros, ataque eles', PRETO, BRANCO)
    motor.desenha_string(janela, 1, 7, 'Caso você morra, terá instruções na tela de gameover', PRETO, BRANCO)
    motor.desenha_string(janela, 1, 9, "Aperte a tecla 'q' a qualuqer momento para sair do jogo", PRETO, BRANCO)
    motor.desenha_string(janela, 1, 11,'Aperte "n" para comecar.', PRETO, BRANCO)

    motor.mostra_janela(janela)




def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada == 'n':
        estado['tela_atual'] = TELA_JOGO

    elif tecla_apertada in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR