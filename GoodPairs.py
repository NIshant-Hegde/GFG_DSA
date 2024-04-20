def numIdenticalPairs(nums):
    FT = [0] * 100
    gpc = 0

    for i in range(len(nums)):
        FT[nums[i]] += 1

    for ele in FT:
        if ele != 0:
            if ele > 2:
                gpc += (((ele - 2)/2) * (3 + ele))
            elif ele == 2:
                gpc += 1
    
    return gpc

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))