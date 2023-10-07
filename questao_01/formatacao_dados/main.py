from formatacao_arquivos import funcao_formatacao

arquivo1 = funcao_formatacao("questao_01/formatacao_dados/pph_11_01.dat")

print(arquivo1)

# print(open("questao_01/formatacao_dados/pph_5_01.dat", "r").read().strip().replace("\n", "").split(" "))


quant_num = arquivo1['quant_num']
array_a = [int(a) for a in arquivo1['array_a']]
array_b = [int(b) for b in arquivo1['array_b']]

synced_pairs = list(zip(array_a, array_b))
print(synced_pairs)

S = [(array_a[0], array_b[0])]
R = array_a[0]/array_b[0]

def somaR(array):
    for i in range(1, len(array)):
        a = (array[i-1][i-1]+array[i][i-1])
        b = (array[i-1][i]+array[i][i])
        R = a/b
    return R


for k in range(quant_num):
    for j in range(quant_num):
        if k==j:
            if array_a[k]/array_b[k] > R:
                S.append((array_a[k], array_b[k]))
                R = somaR(S)

print(S)
print(R)