"""
Day 89: Merge K Sorted Arrays
"""

import heapq

def merge_k_arrays(arrays):

    heap = []
    result = []

    # Step 1: Push first elements
    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))

    # Step 2: Process heap
    while heap:

        val, arr_idx, ele_idx = heapq.heappop(heap)
        result.append(val)

        # Push next element from same array
        if ele_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][ele_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, ele_idx + 1))

    return result


# Test
arrays = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

print("Merged Array:", merge_k_arrays(arrays))