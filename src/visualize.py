#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

for k,v in items[:10]:
    print(k,':',v)
    plt.bar(k, v)

# Plot the thing
label_suffix = 'Country' if args.input_path.endswith('.country') else 'Language'
key_base_name = args.key.lstrip('#')

plt.xlabel(f'{label_suffix}')
plt.ylabel('Counts')
plt.title(f'Data Visualization for {args.key} - {label_suffix}')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

output_filename = f'output_plot_{key_base_name.lower()}_{label_suffix.lower()}.png'
plt.savefig(output_filename)
