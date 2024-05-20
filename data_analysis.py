import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

df = pd.read_csv('sorting_execution_times_experiment.csv')
# Convert Execution Time to microseconds
df['Execution Time'] = df['Execution Time'] * 1000000

# Box plot grouped by Algorithm and Length
plt.figure(figsize=(12, 8))
sns.boxplot(x='Length', y='Execution Time', hue='Algorithm', data=df)
plt.title('Box Plot of Execution Time Grouped by Algorithm and Length')
plt.xlabel('Length')
plt.ylabel('Execution Time (µs)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Algorithm')
plt.tight_layout()
plt.savefig('figures/boxplot_lenght.png')

# Box plot grouped by Algorithm and Dataset Type
plt.figure(figsize=(12, 8))
sns.boxplot(x='Dataset Type', y='Execution Time', hue='Algorithm', data=df)
plt.title('Box Plot of Execution Time Grouped by Algorithm and Dataset Type')
plt.xlabel('Dataset Type')
plt.ylabel('Execution Time (µs)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Algorithm')
plt.tight_layout()
plt.savefig('figures/boxplot_dataset.png')


# Line plots for each dataset type
fig, axs = plt.subplots(2, 2, figsize=(18, 12))
axs = axs.flatten()
x_values = [10, 100, 1000, 10000, 100000, 1000000]
min_execution_time = df['Execution Time'].min()
max_execution_time = df['Execution Time'].max()

algorithms = [
    ('BubbleSort', 'red', 'o'),
    ('HeapSort', 'blue', 's'),
    ('InsertionSort', 'deeppink', '^'),
    ('MergeSort', 'orange', 'd'),
    ('QuickSort', 'yellow', 'o'),
    ('SelectionSort', 'green', 'x')
]

i = 0
dataset_types = ['Ordered', 'OrderedInverse', 'AlmostOrdered', 'Random']

for dataset_type, ax in zip(dataset_types, axs):
    df_subset = df[df['Dataset Type'] == dataset_type]
    
    for algorithm_name, color, marker in algorithms:
        df_algorithm = df_subset[df_subset['Algorithm'] == algorithm_name]
        ax.plot(df_algorithm['Length'], df_algorithm['Execution Time'], label=algorithm_name,
                c=color, marker=marker, linestyle='-', alpha=0.85)
        ax.grid(True, linestyle='--', alpha=0.7)
        
    
    ax.set_title(f'{dataset_type}')
    ax.set_xlabel('Length')
    ax.set_ylabel('Execution Time (µs)') 
    ax.set_xscale('log') 
    ax.set_xticks(x_values)
    
    ax.get_xaxis().set_major_formatter(ticker.LogFormatter()) 
    

    if i == 0:
        ax.legend()
    i += 1
    
# Set the same y-axis limits for all subplots
for ax in axs:
    ax.set_ylim(min_execution_time, max_execution_time)

plt.tight_layout()
plt.savefig('figures/lineplot_alldata.png')
