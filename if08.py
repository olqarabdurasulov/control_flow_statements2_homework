def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    ans = ""
    if number == 1:
        ans = "Monday"

    elif number == 2:
        ans = "Tuesday"

    elif number == 3:
        ans = "Wednesday"

    elif number == 4:
        ans = "Thursday"

    elif number == 5:
        ans = "Friday"

    elif number == 6:
        ans = "Saturday"
        
    elif number == 7:
        ans = "Sunday"
    return ans 