def length_of_last_word(s):
    words = s.split()
    if not words:
        return 0
    return len(words[-1])
s = input()
result = length_of_last_word(s)
print(result)

#Algorithm
'''It first splits the input string into a list of words.
#It then checks if there are any words in the list. If not, it returns 0.
#If there are words, it returns the length of the last word in the list.'''

#Logic
'''s.split(): This method splits the input string  into a list of words using spaces.
if not words: This condition checks if the words list is empty.
return len(words[-1]): If there are words in the list, this line returns the length of the last word in the list.'''