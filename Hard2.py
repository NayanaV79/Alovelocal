#You are given a string s. You can convert s to a palindrome by adding characters in front of it.
def shortest_palindrome(s):
    def find_longest_palindrome_prefix(s):
        rev_s = s[::-1]
        for i in range(len(s)):
            if s.startswith(rev_s[i:]):
                return rev_s[:i] + s

    if not s:
        return ""

    return find_longest_palindrome_prefix(s)

user_input = input("s=")

result = shortest_palindrome(user_input)
print(result)

#Algorithm
'''
The algorithm uses a helper function to find the longest palindrome prefix of a given string.
The main function handles the case when the input string is empty.
If the input string is not empty, it calls the helper function to find the longest palindrome prefix.
The result is the shortest palindrome obtained by adding characters in front of the original string.
'''
#logic
'''
It reverses the string s to create rev_s.
It iterates through the characters of the original string and checks if the reversed string  is a prefix of the original string.
If the input string is empty (not s), it returns an empty string as the result.
It then calls the shortest_palindrome function with the user input and prints the input and the resulting palindrome.
'''