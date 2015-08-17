# longest subsequence

# give a array find the longest subsequence



nums = [1,3,2,2,5,2,3,7]
print nums

# sort
# time O(NlogN)
# space O(1)
nums.sort()
print nums
a = 0
b = 0
size = len(nums)
res = 0
while b < size:
	while b < size and nums[b]<=nums[a]+1:
		b += 1
	res = max(res,b-a)
	tmp = nums[a]
	while a < size and nums[a]==tmp:
		a += 1

print res


# hashtable
# time: O(N)
# space: O(N)
check = dict()
for i in nums:
	if i in check:
		check[i] += 1
	else:
		check[i] = 1

print check
first_key = None
res = 0
for key in check:
	if not first_key:
		first_key = key
		continue
	else:
		second_key = first_key
		first_key = key
		res = max(res,check[first_key]+check[second_key])
print res
