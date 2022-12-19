def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    ans = ""
    if temp < 0:
        ans = "Freezing"
    elif temp >= 1 and temp <= 10:
        ans = "Very Cold"
    elif temp >= 11 and temp <= 20:
        ans = "Cold"
    elif temp >= 21 and temp <= 30:
        ans = "Normal"
    elif temp >= 31 and temp <= 40:
        ans = "Hot"
    elif temp > 40:
        ans = "Very Hot"
    return ans 