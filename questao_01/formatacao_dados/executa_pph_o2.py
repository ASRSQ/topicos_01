from formatacao_arquivos import funcao_formatacao
from pph_o2 import pph
import time


def executa_pph_o2(instancia):
    # Defina o número de segundos que deseja executar o código
    tempo_desejado = 5  # Por exemplo, 5 segundos

    # Registra o tempo inicial
    tempo_inicial = time.time()
    num_iteracao = 0

    # Executa o código que deseja por X segundos
    while True:
        for i in range(1, 100):
            num_arquivo = str(i).zfill(2)
            path = f"questao_01/data/{instancia}/pph_{instancia}_{num_arquivo}.dat"
            arquivo = funcao_formatacao(path)

            # Problema de Programação Hiperbólica
            R, S = pph(arquivo)

            num_iteracao += 1
            print(f"iteracao {num_iteracao}")
            print(f"R = {R}")
            print(f"S = {S}")

        # Verifica o tempo atual
        tempo_atual = time.time()

        # Verifica se o tempo decorrido é maior ou igual ao tempo desejado
        if tempo_atual - tempo_inicial >= tempo_desejado:
            break

    return num_iteracao
