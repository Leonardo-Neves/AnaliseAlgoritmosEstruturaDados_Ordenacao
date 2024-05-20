import random
import numpy as np
import time
import json 

from heapSort import HeapSort

class GenerateDataset:

    def __init__(self, length_lists):
        self.length_lists = length_lists

    def ordered(self):
        ordered_lists = []
        for length in self.length_lists:
            ordered_lists.append([i for i in range(1, length + 1)])
        return ordered_lists
    
    def orderedInverse(self):
        ordered_inverse_lists = []
        for length in self.length_lists:
            ordered_inverse_lists.append(list(reversed([i for i in range(1, length + 1)])))
        return ordered_inverse_lists
    
    def almostOrdered(self):
        almost_ordered_lists = []
        for length in self.length_lists:
            almost_ordered_lists.append([i for i in range(1, int(np.floor(length / 2)) + 1)])
        for i, almost_ordered_list in enumerate(almost_ordered_lists):
            length = self.length_lists[i]
            while len(almost_ordered_list) != length:
                random_value = random.randint(int(np.floor(length / 2)) + 1, length * 2)
                if random_value not in almost_ordered_list:
                    almost_ordered_list.append(random_value)
        return almost_ordered_lists
    
    def random(self):
        random_lists = []
        for length in self.length_lists:
            random_list = []
            while len(random_list) != length:
                random_value = random.randint(1, length * 2)
                if random_value not in random_list:
                    random_list.append(random_value)
            random_lists.append(random_list)
        return random_lists
    
length_lists = [10, 100, 1000, 10000, 100000, 1000000]
# length_lists = [10, 100]

generate_dataset = GenerateDataset(length_lists)

datasets = []

datasets.append({
    'name': 'Ordered',
    'dataset': generate_dataset.ordered()
})
datasets.append({
    'name': 'Ordered Inverse',
    'dataset': generate_dataset.orderedInverse()
})
datasets.append({
    'name': 'Almost Ordered',
    'dataset': generate_dataset.almostOrdered()
})
datasets.append({
    'name': 'Random',
    'dataset': generate_dataset.random()
})

print(datasets)

algorithm_classes = [
    {   
        'name': 'HeapSort',
        'class': HeapSort
    }
]

algorithm_results = []

for algorithms_class in algorithm_classes:
    for dataset in datasets:
        for itens in dataset['dataset']:

            algorithm = algorithms_class['class'](itens)

            start_time = time.time()

            ordered_itens = algorithm.sort()

            end_time = time.time()

            algorithm_results.append({
                'algorithm': algorithms_class['name'],
                'time': end_time - start_time,
                'dataset_name': dataset['name'],
                'dataset_length': len(itens),
                'ordered_itens': ordered_itens
            })

with open("results.json", "w") as file: 
    json.dump(algorithm_results, file)
