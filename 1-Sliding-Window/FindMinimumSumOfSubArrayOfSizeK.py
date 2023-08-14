"""
Problem:
 Given an array of integers of size ‘n’, Our aim is to calculate the minimum sum of ‘k’ consecutive elements in the array.
"""

import sys 

def findMinimumSum(arr, k):
	min_sum = sum(arr[:k])

	window_sum = min_sum

	for i in range(len(arr) - k):
		window_sum = window_sum - arr[i] + arr[i + k]
		min_sum = min(window_sum, min_sum)

	return min_sum


if __name__ == '__main__':
	arr = list(map(int, input().split()))
	k = int(input())

	print(findMinimumSum(arr, k))