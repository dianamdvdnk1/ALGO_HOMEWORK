"""Сложность O(n) + O(n)"""
#мы эт в классе решали, только первый уровень:)

def f_rob(nums):
    if len(nums) == 1:
        return nums[0]
    s = [0] * len(nums)
    s[0] = nums[0]
    s[1] = nums[1]
    for i in range(2, len(nums)):
        s[i] = nums [i] + max(s[:i-1])
    return max(s[-1], s[-2])



def rob(nums):
    if len(nums) == 1:
        return nums[0] 
    result1 = f_rob(nums[:len(nums) - 1]) #не учитываем первый элемент
    result2 = f_rob(nums[1:])
    return max(result1, result2) #вернуть максимум

