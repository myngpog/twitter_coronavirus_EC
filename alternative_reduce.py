#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--keys',nargs='+',required=True)
args = parser.parse_args()


# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

total = defaultdict(lambda: Counter())
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)

        date = path[-14:-8]

        for k in tmp:
            if k in args.keys:
                total[k][date] += sum(tmp[k].values())


plt.figure()
for hashtag in list(total.keys()):
    plt.plot(total[hashtag].keys(), total[hashtag].values(), label=hashtag)

# Plot the thing
plt.xlabel('Days of Year')
plt.ylabel('Hashtag Count')
plt.title('Hashtag Count over the Year')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

output_filename = 'genshin_hashtag_count.png'
plt.savefig(output_filename)
