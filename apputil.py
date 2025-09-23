def parentheses(s: str) -> bool:
    """
    Check if the parentheses in the string are balanced.
    Only '(' and ')' are considered.
    Returns True if balanced, False otherwise.
    """
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # No matching '('
                return False
            stack.pop()
    return len(stack) == 0  # True if all '(' matched