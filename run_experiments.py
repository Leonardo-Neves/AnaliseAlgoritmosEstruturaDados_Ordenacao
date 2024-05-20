import time
import pandas as pd

from DatasetGenerator import DatasetGenerator
from sorting import (
    QuickSort,
    BubbleSort,
    InsertionSort,
    SelectionSort,
    HeapSort,
    MergeSort
)

# Initialize the dataset generator with the known lengths and the folder to load the datasets
length_lists = [10, 100, 1000, 10000, 100000, 1000000]
generate_dataset = DatasetGenerator(length_lists, save_dir='datasets')

# List of algorithms
algorithms = [
    ('BubbleSort', BubbleSort),
    ('HeapSort', HeapSort),
    ('InsertionSort', InsertionSort),
    ('MergeSort', MergeSort),
    ('QuickSort', QuickSort),
    ('SelectionSort', SelectionSort)
]

# Measure execution time for each algorithm and dataset type
execution_times = []
for length in length_lists:
    for dataset_type in ['Ordered', 'OrderedInverse', 'AlmostOrdered', 'Random']:
        arr = generate_dataset.get_dataset(dataset_type, length)
        
        for algorithm_name, sort_func in algorithms:
            arr_copy = arr.copy()
            start_time = time.time()
            sort_func(arr_copy)
            execution_time = time.time() - start_time
            
            execution_times.append([length, dataset_type, algorithm_name, execution_time])

df = pd.DataFrame(execution_times, columns=['Length', 'Dataset Type', 'Algorithm', 'Execution Time'])

# Save the DataFrame as a CSV file
df.to_csv('sorting_execution_times_experiment.csv', index=False)

print("Execution times saved to sorting_execution_times_experiment.csv")



