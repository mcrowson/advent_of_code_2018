from aocd import data
import pandas as pd
import numpy as np
import numba





def part_a(d):
  df = pd.DataFrame.from_records([{'x': x, 'y': y} for x in np.arange(300) for y in np.arange(300)])
  df['cell_power'] = (((10 + df['x']) * df['y'] + d) * (10 + df['x'])).astype(str).str[-3:-2].replace(r'^\s*$', '0', regex=True).astype(np.integer) - 5  # Add serial and multiply by rackid
  df['3x3_power'] = df.loc[df['x'].between(df['x'], df['x'] + 2) & df['y'].between(df['y'], df['y'] + 2)]['cell_power']
  tr = df.iloc[df['3x3_power'].idxmax()] # Get top 3x3
  return '{},{}'.format(tr['x'], tr['y'])

assert part_a(18) == '33,45'
assert part_a(42) == '21,61'
print("A: {}".format(part_a(int(data))))


#print("B: {}".format(part_b(data.split('\n'))))