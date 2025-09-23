# Exercise 1: Palindrome checker
def palindrome(word: str) -> bool:
    """
    Returns True if the input string is a palindrome, ignoring case,
    spaces, and punctuation. Otherwise returns False.
    """
    # Keep only alphanumeric characters and lowercase
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    return cleaned == cleaned[::-1]

# Exercise 2: Parentheses checker
def parentheses(s: str) -> bool:
    """
    Returns True if parentheses in the string are balanced, False otherwise.
    Ignores all characters except '(' and ')'.
    """
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:  # closing without opening
                return False
    return count == 0  # all opened parentheses must be closed