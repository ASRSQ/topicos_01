def funcao_formatacao(arquivo):
    data = open(arquivo, "r")
    array_1 = data.read().strip()
    data.close()

    array1 = array_1.replace("\n", "")
    array2= array1.split(" ")
    numero_v = int(array2[0])
    a = array2[1:numero_v+1]
    b = array2[numero_v+2:]


    return {'quant_num': numero_v, 'array_a': a, 'array_b': b}