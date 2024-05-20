import time
import pandas as pd
from tqdm import tqdm
import os
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)
# exit(0)
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


csv_file = 'sorting_execution_times_experiment.csv'
if os.path.exists(csv_file):
    results_df = pd.read_csv(csv_file)
else:
    results_df = pd.DataFrame(columns=['Length', 'Dataset Type', 'Algorithm', 'Execution Time'])

for length in tqdm(length_lists, desc="Dataset Lengths"):
    for dataset_type in tqdm(['Ordered', 'OrderedInverse', 'AlmostOrdered', 'Random'], desc='Dataset Types'):
        arr = generate_dataset.get_dataset(dataset_type, length)
        
        for algorithm_name, sort_func in tqdm(algorithms, desc='Algorithms'):
            # Check if this combination has already been processed
            if not results_df[(results_df['Length'] == length) & 
                              (results_df['Dataset Type'] == dataset_type) & 
                              (results_df['Algorithm'] == algorithm_name)].empty:
                continue
            
            arr_copy = arr.copy()
            start_time = time.time()
            try:
                sort_func(arr_copy).sort()
            except Exception as e:
                print(f"Error sorting with {algorithm_name} on {dataset_type} dataset with length {length}: {e}")
                continue
            execution_time = time.time() - start_time
            
            new_row = pd.DataFrame({'Length': [length], 'Dataset Type': [dataset_type], 'Algorithm': [algorithm_name], 'Execution Time': [execution_time]})
            
            results_df = pd.concat([results_df, new_row], ignore_index=True)
            
            results_df.to_csv(csv_file, index=False)

print("Execution times saved to sorting_execution_times_experiment.csv")




