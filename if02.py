def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    min = a
    if min > b and b < c:
        min = b
    elif c < min and c < b:
        min = c 
    return min

