import matplotlib

import matplotlib.pyplot as plt

from matplotlib import collections  as mc

import sys

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="input file")
parser.add_argument("output_file", nargs="?", help="output_file")
args = parser.parse_args()

lines = []
min_x = sys.maxsize
min_y = sys.maxsize
max_x = -min_x
max_y = -min_y

with open(args.input_file) as input_file:
    for line in input_file:
        points = line.strip().split(') (')
        point_1 = [ float(x) for x in points[0][1:].split(',') ]
        point_2 = [ float (x) for x in points[1][:-1].split(',') ]
        min_x = min(min_x, min(point_1[0], point_2[0]))
        min_y = min(min_y, min(point_1[1], point_2[1]))        
        max_x = max(max_x, max(point_1[0], point_2[0]))
        max_y = max(max_y, max(point_1[1], point_2[1]))                
        lines.append([point_1, point_2])

fig, ax = plt.subplots()
ax.set_xlim(min_x - 1, max_x + 1)
ax.set_ylim(min_y - 1, max_y + 1)
lc = mc.LineCollection(lines, colors='black', linewidths=1)
lc.set_capstyle('round')
ax.add_collection(lc)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
if args.output_file:
    plt.savefig(args.output_file, dpi=300)
plt.show()