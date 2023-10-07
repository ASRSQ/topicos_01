from algorithms.fractional_knapsack import median_of_medians_fractional_knapsack, mean_partition_fractional_knapsack

class Item:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.ratio = valor / peso
