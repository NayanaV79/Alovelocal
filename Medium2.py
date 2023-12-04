#Medium.2   Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
def majority_elements(nums):
    # Initialize candidates and their counters
    candidate1, count1 = None, 0
    candidate2, count2 = None, 0

    # Voting process
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

    # Count occurrences of the candidates to validate
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    # Check if candidates appear more than ⌊ n/3 ⌋ times
    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result

# Take input from the user
user_input = input()
nums = list(map(int, user_input.split(',')))

# Call the function with user input
result = majority_elements(nums)

# Display the result
print("Input: nums =", nums)
print("Output:", result)