# quick select solution

# return the kth element in the array
import sys
import pdb
def partition(nums):
	pivot = nums[0]
	a = 0
	b = len(nums)-1
	while a < b:
		while a<b and nums[b] > pivot:
			b -= 1
		nums[b],nums[a] = nums[a],nums[b]
		while a<b and nums[a] < pivot:
			a += 1
		nums[b],nums[a] = nums[a],nums[b]
	nums[a] = pivot
	return a

def quickselect(nums,k):
	#pdb.set_trace()
	pos = partition(nums)
	if pos == k:
		return nums[pos]
	else:
		if pos < k:
			return quickselect(nums[pos+1:],k-pos-1)
		else:
			return quickselect(nums[:pos],k)

import random
x = range(10)
random.shuffle(x)
print x
k = int(sys.argv[1])
print "%dth number in array is %d" %(k, quickselect(x,k))



