
import time
from typing import Callable, List, Tuple
import matplotlib.pyplot as plt
import timeit

import sorting
import ListF
import numpy as np
import json

def TestSelectionSort(array, trials=10):
    sums = []
    for i in range(trials):
        array_copy = array.copy()
        sums.append(timeit.timeit(lambda: sorting.insertion(array_copy), number=1))
    return sums

def SaveResults(output_file, gen_list: Callable[[int], list]):
    RUNS = 50
    RUN_SPACE = 100
    TRIALS = 10

    results = []
    data_x = [ RUN_SPACE * (i + 1) for i in range(RUNS) ]
    for x in data_x:
        print(f"Analysis for {x}/{RUN_SPACE * (RUNS + 1)} entries")
        results.append(TestSelectionSort(gen_list(x), TRIALS))

    x_vals = [d for d in data_x for _ in range(TRIALS)]
    y_vals = [ item for res in results for item in res ]

    obj = {
        'x': x_vals,
        'y': y_vals,
    }

    with open(output_file, 'w') as f:
        f.write(json.dumps(obj))

# Display a scatterplot
def DisplayResults(read_from, color, type):
    with open(read_from) as f:
        o = json.loads(f.read())
        plt.plot(o['x'], o['y'], type, color=color)

# Display a much more readable average line or boxplot
def DisplayAvgResults(read_from, color, type, bp=False):
    with open(read_from) as f:
        o = json.loads(f.read())
        
        averages: List[Tuple[float, List[float]]] = []

        prev_x = None
        for i in range(len(o['x'])):
            if prev_x != o['x'][i]:
                prev_x = o['x'][i]
                averages.append((prev_x, []))
            averages[len(averages)-1][1].append(o['y'][i])

        if bp:
            x = [ avg[0] for avg in averages ]
            y = [ avg[1] for avg in averages ]
            plt.boxplot(y, positions=x, widths=[90 for i in range(len(averages))], flierprops={'markersize': 3})
        
        else:
            x = [ avg[0] for avg in averages ]
            y = [ sum(avg[1]) / len(avg[1]) for avg in averages ]
            plt.plot(x, y, type, color=color)

        vals = np.arange(0, 5001, 1000.0)
        # Arrange the xticks
        plt.xticks(vals, [f"{v:.0f}" for v in vals])

if __name__ == '__main__':
    if input('Would you like to generate data?').lower() == 'y':
        run_start = time.time()
        SaveResults('average.json', lambda x: ListF.randomIntList(x))
        SaveResults('best.json', lambda x: [i for i in range(x)])
        SaveResults('worst.json', lambda x: [(x - i) for i in range(x)])
        print(f"Run complete after {time.time() - run_start:.2f} seconds")


    flags = input("Which cases should be shown? ")
    BOXPLOT = flags.lower().count('d') > 0

    CONSTANT_A = 0.000000051
    CONSTANT_B = 0.000000085
    CONSTANT_C = 0.000000103
    start = time.time()

    ### Expected result ###
    n = [100 * (i + 1) for i in range(50)]

    ### AVERAGE CASE ###
    if flags.lower().count('a') > 0:
        DisplayAvgResults('average.json', 'blue', '-', bp=BOXPLOT)
        if flags.count('A') > 0:
            plt.plot(n, [ (i * i) * CONSTANT_A for i in n ], '-', color='orange')

    ### BEST CASE ###
    if flags.lower().count('b') > 0:
        DisplayAvgResults('best.json', 'yellow', '-', bp=BOXPLOT)
        if flags.count('B') > 0:
            plt.plot(n, [ i * CONSTANT_B for i in n ], '-', color='purple')

    ### WORSE CASE ###
    if flags.lower().count('w') > 0:
        DisplayAvgResults('worst.json', 'red', '-', bp=BOXPLOT)
        if flags.count('W') > 0:
            plt.plot(n, [ (i * i) * CONSTANT_C for i in n ], '-', color='cyan')

    plt.xlabel('Number of items')
    plt.ylabel('Sort time (seconds)')

    print(f"Display results after {time.time() - start:.2f} seconds")
    plt.show()

