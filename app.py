# apputil.py

def palindrome(word: str) -> bool:
    """
    Check if the input string is a palindrome.
    Ignores spaces, punctuation, and is case-insensitive.
    """
    # Keep only alphanumeric characters, lowercase
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    return cleaned == cleaned[::-1]