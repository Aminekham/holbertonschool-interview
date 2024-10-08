#ifndef SORT_H
#define SORT_H

#include <stdlib.h>
#include <stdio.h>

void swap(int *a, int *b);
void sift_down(int *array, int start, int end, size_t size);
void heapify(int *array, size_t size);
void heap_sort(int *array, size_t size);
void print_array(const int *array, size_t size);

#endif
