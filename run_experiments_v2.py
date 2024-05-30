import time
import pandas as pd
import concurrent.futures as futures
import warnings

from DatasetGenerator import DatasetGenerator

from sorting.bubbleSort import bubbleSort
from sorting.heapSort import heapSort
from sorting.insertionSort import insertionSort
from sorting.mergeSort import mergeSort
from sorting.quickSort import quickSort
from sorting.selectionSort import selectionSort

warnings.filterwarnings(action='ignore')

OUTPUT_FILE = 'sorting_execution_times_experiment.csv'
RUN_TIMES = 1

# Initialize the dataset generator with the known lengths and the folder to load the datasets
length_lists = [10, 100, 1000, 10000, 100000, 1000000]
generate_dataset = DatasetGenerator(length_lists, save_dir='datasets')

# List of algorithms
algorithms = [
    'bubbleSort',
    'heapSort',
    'insertionSort',
    'mergeSort',
    'quickSort',
    'selectionSort'
]

results_df = []

def runAlgorithm(length, dataset_type, algorithm_name, arr, run_time_index):

    global results_df

    arr_copy = arr.copy()
    start_time = time.process_time()

    result, counter_comparisons, counter_moviments = globals()[algorithm_name](arr_copy)

    execution_time = time.process_time() - start_time

    results_df.append({ 'Interation': run_time_index + 1, 'Length': length, 'Dataset Type': dataset_type, 'Algorithm': algorithm_name, 'Execution Time': execution_time, 'Counter Comparisons': counter_comparisons, 'Counter Moviments': counter_moviments})

for i in range(0, RUN_TIMES):
    for length in length_lists:
        for dataset_type in ['Ordered', 'OrderedInverse', 'AlmostOrdered', 'Random']:
            arr = generate_dataset.get_dataset(dataset_type, length)
            
            MAX_WORKERS = 1000

            workers = min(MAX_WORKERS, len(algorithms))

            with futures.ThreadPoolExecutor(workers) as executor:
                future_to_get_bv = {executor.submit(runAlgorithm, length, dataset_type, algorithm_name, arr, i): dataset_type for algorithm_name in algorithms}    
                for future in futures.as_completed(future_to_get_bv):
                    future.result()

                    
results_df = pd.DataFrame(results_df, columns=['Interation', 'Length', 'Dataset Type', 'Algorithm', 'Execution Time', 'Counter Comparisons', 'Counter Moviments'])

results_df.to_csv(OUTPUT_FILE, index=False, sep=";")        

print(f"Execution times saved to {OUTPUT_FILE}")
