#!/usr/bin/python3
"""stats metrics"""
import sys

status_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

file_sizes = [0]

def display_statistics():
    total_size = sum(file_sizes)
    print('File size: {}'.format(total_size))
    for code, quantity in sorted(status_counts.items()):
        if quantity > 0:
            print('{}: {}'.format(code, quantity))

try:
    for line_number, entry in enumerate(sys.stdin, start=1):
        data = entry.strip().split()
        try:
            status = data[-2]
            size = data[-1]
            if status in status_counts:
                status_counts[status] += 1
            file_sizes.append(int(size))
        except (IndexError, ValueError):
            continue
        if line_number % 10 == 0:
            display_statistics()
    display_statistics()
except KeyboardInterrupt:
    display_statistics()
    raise
