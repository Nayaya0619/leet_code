
ans=[]
nums= [3,2,4]
target = 6
k = 0
for i in nums:
    k += 1
    if target - i in nums[k:]:
        ans.append(k - 1)
        ans.append(nums[k:].index(target - i) + k)
print (ans)
