
def palindrome(word: str) -> bool:
    """
    Check if the input string is a palindrome.
    Ignores spaces, punctuation, and is case-insensitive.
    """
    # Remove spaces and punctuation, convert to lowercase
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    # Check if cleaned string equals its reverse
    return cleaned == cleaned[::-1]