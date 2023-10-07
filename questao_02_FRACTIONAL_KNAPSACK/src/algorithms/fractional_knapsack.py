from functools import reduce
from select_bfprt import select_bfprt_factory

select_bfprt = select_bfprt_factory(5)

# def sorted_fractional_knapsack(items, capacidade):

def median_of_medians_fractional_knapsack(items, capacidade):
    if capacidade == 0 or len(items)==0:
        return 0

    if len(items) == 1 and items[0].peso > capacidade:
        return capacidade * items[0].ratio

    k = len(items) // 2
    mid = select_bfprt(items, k)
    items_right = items[mid:]

    w1 = 0
    v1 = 0

    for item in items_right:
        w1 += item.peso
        v1 += item.valor
    
    # Não cabe na mochila
    if(w1 > capacidade):
        return median_of_medians_fractional_knapsack(items_right, capacidade)

    # Cabe na mochila
    items_left = items[:mid]
    return v1 + median_of_medians_fractional_knapsack(items_left, capacidade - w1)

def partition_by_mean(items, inicio, fim):
    k = len(items)
    # print('sum ratios', sum([item.ratio for item in items]))
    pivot = 1 / k * sum([item.ratio for item in items])
    # pivot = items[fim].ratio
    # print('pivot', pivot)

    i = inicio - 1
    for j in range(inicio, fim):
        if items[j].ratio >= pivot:
            i += 1

            items[i], items[j] = items[j], items[i]

    items[i + 1], items[fim] = items[fim], items[i + 1]
    # return len(items) // 2 => If len(items) = 5, return 2
    return i + 1

def mean_partition_fractional_knapsack(items, capacidade):
    if capacidade == 0 or len(items) == 0:
        return 0

    if len(items) == 1 and items[0].peso > capacidade:
        return capacidade * items[0].ratio


    mid = partition_by_mean(items, 0, len(items) - 1)
    items_right = items[: mid]

    w1 = 0
    v1 = 0

    for item in items_right:
        w1 += item.peso
        v1 += item.valor

    # Não cabe na mochila
    if(w1 > capacidade):
        return mean_partition_fractional_knapsack(items_right, capacidade)

    # Cabe na mochila
    items_left = items[mid : ]
    return v1 + mean_partition_fractional_knapsack(items_left, capacidade - w1)

# if __name__ == "__main__":
#     VAL = 10

#     w = [random.randint(1, VAL) for _ in range(VAL)]
#     v = [random.randint(1, VAL) for _ in range(VAL)]
#     itens = [Item(w[i], v[i]) for i in range(len(w))]
#     itens_v1 = itens.copy()
#     itens_v2 = itens.copy()

#     # itens = [Item(40, 840), Item(30, 600), Item(20, 400), Item(10, 100), Item(20, 300)]
#     # itens = [Item(2, 40), Item(5, 30), Item(10, 50), Item(5, 10)]
#     # Give another example for the kn
#     # {{60, 10}, {100, 20}, {120, 30}}, W = 50
#     # {profit, weigth}

#     # itens = [Item(10, 60), Item(20, 100), Item(30, 120)]
#     # itens = [Item(2, 40), Item(5, 30), Item(10, 50), Item(5, 10), Item(8, 70)]
#     capacidade_mochila = 10

#     import time

#     start = time.time()
#     valor_total = median_of_medians_fractional_knapsack(itens_v1, capacidade_mochila)
#     end = time.time()

#     print(f"Tempo de execução - v1: {end - start}")

#     start = time.time()
#     valor_total_v2 = mean_partition_fractional_knapsack(itens_v2, capacidade_mochila)
#     end = time.time()

#     print(f"Tempo de execução - v2: {end - start}") 
#     # print("Itens na mochila:")
#     # for item in `mochila`:
#     #     print(f"Peso: {item.peso}, Valor: {item.valor}")
#     print(f"Valor total na mochila: {valor_total}")
#     print(f"Valor total na mochila: {valor_total_v2}")
