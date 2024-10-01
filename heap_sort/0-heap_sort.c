#include "sort.h"
#include <stdio.h>

/**
 * swap - Swaps two elements in an array
 * @a: First element
 * @b: Second element
 */
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

/**
 * sift_down - Repairs the heap whose root element is at index 'start'
 * @array: The array to be sorted
 * @start: The index of the root element of the heap
 * @end: The last index of the heap
 * @size: Total size of the array for printing
 */
void sift_down(int *array, int start, int end, size_t size)
{
    int root = start;

    while (root * 2 + 1 <= end)
    {
        int child = root * 2 + 1;
        int swap_idx = root;

        if (array[swap_idx] < array[child])
            swap_idx = child;

        if (child + 1 <= end && array[swap_idx] < array[child + 1])
            swap_idx = child + 1;

        if (swap_idx == root)
        {
            return;
        }
        else
        {
            swap(&array[root], &array[swap_idx]);
            print_array(array, size);  // Print the array after every swap
            root = swap_idx;
        }
    }
}

/**
 * heapify - Builds the heap in array
 * @array: The array to be heapified
 * @size: The size of the array
 */
void heapify(int *array, size_t size)
{
    int start = (size - 2) / 2; // Last parent node

    while (start >= 0)
    {
        sift_down(array, start, size - 1, size);
        start--;
    }
}

/**
 * heap_sort - Sorts an array of integers in ascending order using Heap sort
 * @array: The array to be sorted
 * @size: The size of the array
 */
void heap_sort(int *array, size_t size)
{
    if (size < 2)
        return;

    heapify(array, size);

    for (size_t end = size - 1; end > 0; end--)
    {
        swap(&array[end], &array[0]);
        print_array(array, size);
        sift_down(array, 0, end - 1, size);
    }
}
