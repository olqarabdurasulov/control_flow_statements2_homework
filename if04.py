def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    ans = 0
    if a > b:
        ans = a
    elif a < b:
        ans = b
    return ans

