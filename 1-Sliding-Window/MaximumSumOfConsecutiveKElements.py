"""
Problem:
 Given an array of integers of size ‘n’, Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array.
"""

"""
# Naive Approach or Brute Force Approach:

import sys

# O (n * k) solution for finding 
# maximum sum of a subarray of size k
INT_MIN = -sys.maxsize - 1

# Returns maximum sum in a
# subarray of size k.

def maxSum(arr, n, k):

	# Initialize result
	max_sum = INT_MIN

	# Consider all blocks
	# starting with i.
	for i in range(n - k + 1):
		current_sum = 0
		for j in range(k):
			current_sum = current_sum + arr[i + j]

		# Update result if required.
		max_sum = max(current_sum, max_sum)

	return max_sum

# Driver Code
arr = [1, 4, 2, 10, 2,
		3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
"""

"""
Sliding Window Approach:
Applying the sliding window technique : 

1. We compute the sum of the first k elements out of n terms using a linear loop 
	 and store the sum in variable window_sum.
2. Then we will graze linearly over the array till it reaches the end 
	 and simultaneously keep track of the maximum sum.
3. To get the current sum of a block of k elements just subtract the first element from the previous block 
	 and add the last element of the current block.
"""

# O(n) solution for finding
# maximum sum of subarray of size k

def maxSum(arr, k):
	# length of array
	n = len(arr)

	# n must be greater than k
	if n < k:
		return "INVALID"

	# Compute the sum of first window of size k
	window_sum = sum(arr[:k])

	# First Sum Available
	max_sum = window_sum

	for i in range(n - k):
		window_sum = window_sum - arr[i] + arr[i + k]
		max_sum = max(window_sum, max_sum)

	return max_sum


# Driver Code
if __name__ == '__main__':
	arr = [1, 4, 2, 10, 2,
			3, 1, 0, 20]
	k = 4
	print(maxSum(arr, k))
