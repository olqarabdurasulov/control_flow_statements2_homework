def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    ans = 0
    if (a>b and a<c) or (a > c and a < b):
        ans = a
    elif (b>a and b<c) or (b > c and b < a):
        ans = b
    else:
        ans = c 
    
    return ans
