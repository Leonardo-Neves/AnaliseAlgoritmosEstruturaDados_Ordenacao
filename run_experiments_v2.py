import time
import pandas as pd
import concurrent.futures as futures

from DatasetGenerator import DatasetGenerator
from sorting import (
    QuickSort,
    BubbleSort,
    InsertionSort,
    SelectionSort,
    HeapSort,
    MergeSort
)

OUTPUT_FILE = 'sorting_execution_times_experiment.csv'

# Initialize the dataset generator with the known lengths and the folder to load the datasets
length_lists = [10, 100, 1000, 10000, 100000, 1000000]
generate_dataset = DatasetGenerator(length_lists, save_dir='datasets')

# List of algorithms
algorithms = [
    ('BubbleSort', BubbleSort),
    ('HeapSort', HeapSort),
    ('InsertionSort', InsertionSort),
    ('QuickSort', QuickSort),
    ('SelectionSort', SelectionSort),
    ('MergeSort', MergeSort),
]

results_df = []

def runAlgorithm(length, dataset_type, algorithm_name, sort_func):
    
    global results_df

    arr_copy = arr.copy()
    start_time = time.time()
    try:
        sort_func(arr_copy).sort()
    except Exception as e:
        pass

    execution_time = time.time() - start_time

    results_df.append({'Length': length, 'Dataset Type': dataset_type, 'Algorithm': algorithm_name, 'Execution Time': execution_time})

for length in length_lists:
    for dataset_type in ['Ordered', 'OrderedInverse', 'AlmostOrdered', 'Random']:
        arr = generate_dataset.get_dataset(dataset_type, length)
        
        MAX_WORKERS = 1000

        workers = min(MAX_WORKERS, len(algorithms))

        with futures.ThreadPoolExecutor(workers) as executor:
            future_to_get_bv = {executor.submit(runAlgorithm, length, dataset_type, algorithm_name, sort_func): dataset_type for algorithm_name, sort_func in algorithms}    
            for future in futures.as_completed(future_to_get_bv):
                future.result()

                    
results_df = pd.DataFrame(results_df, columns=['Length', 'Dataset Type', 'Algorithm', 'Execution Time'])

results_df.to_csv(OUTPUT_FILE, index=False, sep=";")        

print(f"Execution times saved to {OUTPUT_FILE}")
