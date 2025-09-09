
def palindrome(word):
    length = len(word)
    if length == 0:
        return 0
            #reverse of the word is [word[::-1]]
    return word == word[::-1]

print(palindrome("python"))
print(palindrome("racecar"))
print(palindrome("Nurses Run"))
print(palindrome("Sit on a potato pan Otis"))
print("running the balanced parenthesis assignment ____________________")
# add code below ...
def is_balanced(sequence):
    """Checks if a string has balanced parentheses."""
    count = 0  # count how many times '(' is currently open
    for char in sequence:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:  # count is -ve, we have a ")" before - imbalanced
                return False  # imbalanced - False
    return count == 0  # Balanced if the final count is 0

print(is_balanced("(((())"))
print(is_balanced("((blah)()()())"))