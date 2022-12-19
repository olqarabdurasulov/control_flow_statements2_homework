def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    
    n1 = n % 10
    n = n//10
    index1 = 1

    n2 = n % 10
    n = n//10
    index2 = 2

    n3 = n % 10
    n = n//10
    index3 = 3

    n4 = n % 10
    n = n//10
    index4 = 4

    n5 = n % 10
    n = n//10
    index5 = 5

    m = n1
    index = index1
    if n2 > m:
        m = n2
        index = index2
    if m < n3:
        m = n3
        index = index3 
    if m < n4:
        m = n4 
        index = index4 
    if m < n5:
        m = n5
        index = index5
    return index 
print(main(76514))
print(main(54694))
