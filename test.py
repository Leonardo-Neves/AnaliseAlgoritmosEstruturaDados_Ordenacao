import warnings
warnings.filterwarnings(action='ignore')

from DatasetGenerator import DatasetGenerator

from sorting.bubbleSort import bubbleSort
from sorting.heapSort import heapSort
from sorting.insertionSort import insertionSort
from sorting.mergeSort import mergeSort
from sorting.quickSort import quickSort
from sorting.selectionSort import selectionSort

length_lists = [10, 100, 1000, 10000, 100000, 1000000]
generate_dataset = DatasetGenerator(length_lists, save_dir='datasets')

datasets = generate_dataset.generate_ordered_inverse()
print(datasets[0])

A, counter_comparisons, counter_moviments = bubbleSort(datasets[0])
print(A)
print(counter_comparisons)
print(counter_moviments)