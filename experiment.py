import pandas as pd
import numpy as np

file = 'experiment.csv'
edf = pd.read_csv('experiment.csv', dtype=str)
ans = np.full(1000, -1) 

try: 
    for i, row in edf.iterrows():
        info = ('\n----------------------------------------------------------------------------------\n\n'
        f'TWEET #{i+1}\n\n'
        'Possible responses:\n\n'
        'Unpolitical/Undecided (0)\n'
        'Positive to Democrats (1)\n'
        'Negative to Democrats (2)\n'
        'Negative to Conservatives (3)\n'
        'Positive to Conservatives (4)\n')

        
        print(info)
        val = input(f'Tweet:\n\n{row.text}\n\nPolitical Opinion (0-4): ')
        ans[i] = val
finally:
    col = f'test{len(edf.columns) - 2}'
    edf[col] = ans
    edf.to_csv('experiment.csv', index=False)