#!/usr/bin/env python3

# Extract, transform and write CSV data from a CSV file.

import sys
import csv

if len(sys.argv) != 3:
    print('exactly 2 arguments are expected')
    sys.exit(1)

with open(sys.argv[1], 'r') as input_file:
    with open(sys.argv[2], 'w', newline='\n') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        next(reader) # skip header
        writer.writerow(['1st', '2nd']) # write header

        # transform and write
        for row in reader:
            writer.writerow([row[0], row[1]])
