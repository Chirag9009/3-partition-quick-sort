# 3-partition-quick-sort
In simple QuickSort algorithm, we select an element as pivot, partition the array around pivot and recur for subarrays on left and right of pivot.
Consider an array which has many redundant elements. For example, {1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4}. If 4 is picked as pivot in Simple QuickSort, we fix only one 4 and recursively process remaining occurrences.

The idea of 3 way QuickSort is to process all occurrences of pivot and is based on Dutch National Flag algorithm.

In 3 Way QuickSort, an array arr[l..r] is divided in 3 parts:
1. arr[l..i] elements less than pivot.
2. arr[i+1..j-1] elements equal to pivot.
3. arr[j..r] elements greater than pivot.
