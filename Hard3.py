#Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n
def count_one(n):
    count = 0

    for i in range(1, n + 1):
        count += str(i).count('1')

    return count
n = int(input("n="))
result = count_one(n)
print(result)
#Algorithm
'''
First step is to Initialize count=0.
Next,Loop through digits from right to left in each number from 1 to n that is provided by user.
Calculate the number of one's in each digit.
Return the final count as a result.
'''