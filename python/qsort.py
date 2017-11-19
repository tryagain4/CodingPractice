def qsort(nums,s,e):   
    x, y = s, e
    pivot = nums[s]
    while (x < y):
        while ( x < y and nums[y] >= pivot): y-= 1
        nums[x]=nums[y]
        while ( x < y and nums[x] <= pivot): x+= 1
        nums[y]=nums[x]
    nums[x]=pivot       
    print nums
    if (x - 1 > s): qsort(nums, s, x)
    if (e > x + 1): qsort(nums, x + 1, e)

nums = [100, 1,3,5,7,9,2,4,6,8,10,-1]
qsort(nums, 0 ,len(nums) - 1)
print nums    