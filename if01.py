def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    maximum = 0
    if a > b and a > c:
        maximum = a
    elif b>a and b>c:
        maximum = b
    else:
        maximum = c
    return maximum