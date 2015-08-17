# city map
# given an array as the map
# T[x] = y means x is connect with y
# T[x] = x means x is the capital

import collections
import pdb

nums = [1,1,1,2,1,6,4,1,7,8,3]
print nums
print range(len(nums))

def findCapital(nums):
	for i in range(len(nums)):
		if nums[i] == i:
			return i

cap = findCapital(nums)

check = dict()
check[cap] = []
for i in range(len(nums)):
	if i == cap:
		continue
	if nums[i] in check:
		check[nums[i]].append(i)
	else:
		check[nums[i]] = [i]

print check
parent = collections.deque()
parent.append(cap)
child = collections.deque()
res = []
#count = 0
while parent:
	#pdb.set_trace()
	curr = parent.popleft()
	if curr in check:
		child.extend(check[curr])
	#count += len(check[curr])
	if not parent:
		if child:
			res.append(len(child))
		while child:
			parent.append(child.popleft())
		#count = 0
print res


