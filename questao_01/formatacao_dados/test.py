# from formatacao_arquivos import funcao_formatacao

# data = funcao_formatacao("questao_01/formatacao_dados/pph_11_01.dat")

# quant_num = data['quant_num']
# array_a = [int(a) for a in data['array_a']]
# array_b = [int(b) for b in data['array_b']]

# synced_pairs = list(zip(array_a, array_b))

# print(synced_pairs)

# R = array_a[0] / array_b[0]
# S = set()

# for k in range(1, quant_num):
#     for j in range(quant_num):
#         if array_a[j] / array_b[j] < R:
#             S.add((array_a[j], array_b[j]))
#             R = array_a[j] / array_b[j]

# # S = {(a, b) for a, b in S if a / b < R}

# print(S)
# print(R)


# def encontrar_R_S(coef_a, coef_b):
#     n = len(coef_a) - 1
#     R = coef_a[0] / coef_b[0]
#     S = set()

#     for k in range(1, n + 1):
#         for j in range(n + 1):
#             if coef_a[j] / coef_b[j] < R:
#                 S.add((coef_a[j], coef_b[j]))
#                 R = coef_a[j] / coef_b[j]

#     # Remover elementos de S que não satisfazem às condições do lema
#     S = {(a, b) for a, b in S if a / b < R}

#     return R, S


# # Exemplo de uso com a entrada diretamente
# coef_a, coef_b = ([400,
#                    421,
#                    68,
#                    28,
#                    48,
#                    271,
#                    431,
#                    1,
#                    460,
#                    326,
#                    165,
#                    53,
#                    87,
#                    295,
#                    321,
#                    53,
#                    124,
#                    226,
#                    298,
#                    34],
#                   [397,
#                    76,
#                    422,
#                    526,
#                    649,
#                    344,
#                    935,
#                    119,
#                    224,
#                    192,
#                    176,
#                    223,
#                    422,
#                    151,
#                    649,
#                    63,
#                    39,
#                    475,
#                    306,
#                    459])

# # R, S = encontrar_R_S(coef_a, coef_b)

# print(encontrar_R_S(coef_a, coef_b))
