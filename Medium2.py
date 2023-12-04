#Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
def major_elements(nums):
    candidate1, count1 = None, 0
    candidate2, count2 = None, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result
user_input = input("Nums=")
nums =list(map(int, user_input.split(',')))
result = major_elements(nums)
print("nums =", nums)
print( result)
#algorithm
'''
The algorithm uses two candidates and their counts to keep track of potential majority elements.
During the voting process, it updates the counts based on the current element.
After the voting process, it validates the counts of the candidates and adds them to the result list if they appear more than ⌊ n/3 ⌋ times.
'''
#logic
'''
candidate1 and candidate2 represent the two potential majority elements.
count1 and count2 represent their respective counts.
Iterate through the array nums.
If the current number is one of the candidates, increment its count.
If the counts are 0, update the candidate and set its count to 1.
If the counts are not 0, decrement the counts for both candidates.
If the counts of the candidates exceed ⌊ n/3 ⌋, add them to the result list.
'''