from formatacao_arquivos import funcao_formatacao

arquivo1 = funcao_formatacao("questao_01/formatacao_dados/pph_11_01.dat")

quant_num = arquivo1['quant_num']
array_a = [int(a) for a in arquivo1['array_a']]
array_b = [int(b) for b in arquivo1['array_b']]

S = [(array_a[0], array_b[0]), (array_a[1], array_b[1])]
R = array_a[0]/array_b[0]


def somaR(array):
    soma_A = 0.0
    soma_B = 0.0

    for par in array:
        A, B = par
        soma_A += A
        soma_B += B

    if soma_B != 0:
        R = soma_A / soma_B

    # print(R)
    return R


for k in range(quant_num):
    if array_a[k]/array_b[k] > R:
        if (array_a[k], array_b[k]) not in S:
            S.append((array_a[k], array_b[k]))
        R = somaR(S)


print(S)
print(R)
