
ans=[]
nums= [3,2,4]
target = 6
dect ={}

for i in range(len(nums)):
    dect[nums[i]]=i
for i in range(len(nums)):
    if target - nums[i] in dect:
        if  dect [ target - nums[i] ] != i:
            ans.append(i)
            ans.append(dect[target - nums[i]])
            break

print (ans)