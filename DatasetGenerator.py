import random
import numpy as np
import pickle
import os

class DatasetGenerator:
    
    def __init__(self, length_lists=[], save_dir='datasets'):
        self.length_lists = length_lists
        self.datasets = {}
        self.save_dir = save_dir
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def _save_dataset(self, name, length, dataset):
        self.datasets[(name, length)] = dataset
        filename = f"{name}_{length}.pkl"
        filepath = os.path.join(self.save_dir, filename)
        with open(filepath, 'wb') as f:
            pickle.dump(dataset, f)

    def _load_dataset(self, name, length):
        filename = f"{name}_{length}.pkl"
        filepath = os.path.join(self.save_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                return pickle.load(f)
        else:
            return None

    def generate_ordered(self):
        for length in self.length_lists:
            ordered_list = list(range(1, length + 1))
            self._save_dataset('Ordered', length, ordered_list)
    
    def generate_ordered_inverse(self):
        for length in self.length_lists:
            ordered_inverse_list = list(range(length, 0, -1))
            self._save_dataset('OrderedInverse', length, ordered_inverse_list)
    
    def generate_almost_ordered(self):
        for length in self.length_lists:
            half = list(range(1, int(np.floor(length / 2)) + 1))
            remaining = list(range(int(np.floor(length / 2)) + 1, length + 1))
            random.shuffle(remaining)
            almost_ordered_list = half + remaining
            self._save_dataset('AlmostOrdered', length, almost_ordered_list)
    
    def generate_random(self):
        for length in self.length_lists:
            random_list = random.sample(range(1, length * 2 + 1), length)
            self._save_dataset('Random', length, random_list)
    
    def generate_all(self):
        self.generate_ordered()
        self.generate_ordered_inverse()
        self.generate_almost_ordered()
        self.generate_random()
    
    def get_dataset(self, name, length):
        # First, we try to get the dataset from memory
        dataset = self.datasets.get((name, length), None)
        if dataset is None:
            # If not in memory, we try to load it from disk
            dataset = self._load_dataset(name, length)
        return dataset
            
if __name__ == "__main__":
    # Example usage
    length_lists = [10, 100, 1000, 10000, 100000, 1000000]
    generate_dataset = DatasetGenerator(length_lists, save_dir='datasets')

    # Generate all datasets
    generate_dataset.generate_all()

    # Retrieve a specific dataset
    dataset = generate_dataset.get_dataset('AlmostOrdered', 10)
    print(dataset)
