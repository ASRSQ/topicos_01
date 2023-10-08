from medir_tempo_memoria import medir_tempo_memoria
from executa_pph_o2 import executa_pph_o2

instacias = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000]

for instancia in instacias:
    medir_tempo_memoria(1, executa_pph_o2, instancia, f"pph_{instancia}_o2",
                        "questao_01/graficos/", "questao_01/relatorios/")
