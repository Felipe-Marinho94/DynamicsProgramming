import random
from OrdenationAlgorithms import selection_sort, bubble_sort, insertion_sort

any_numbers = random.sample(range(1, 1000), 42)
already_sorted = [1, 2, 3, 4, 5, 6, 9]
inversed = [9, 6, 5, 4, 3, 2, 1]
repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9]

print(any_numbers)
print("\n Ordenado")
print(insertion_sort(any_numbers))