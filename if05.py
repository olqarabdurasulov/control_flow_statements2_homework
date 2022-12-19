def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    maximum = 0
    
    n1 = n % 10
    n = n//10
    n2 = n % 10
    n = n//10
    n3 = n % 10
    n = n//10
    n4 = n % 10
    n = n//10
    n5 = n % 10
    n = n//10

    if n1 > n2:
        maximum = n1
    elif n3 > maximum:
        maximum = n3
    elif n4 > maximum:
        maximum = n4
    elif n5 > maximum:
        maximum = n5
    return maximum
print(main(23546))