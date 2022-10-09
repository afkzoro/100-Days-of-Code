def square(user):
    if user > 0 and user <= 64:
        return (f"The number of grains on square {user} is {user}")
    else:
        raise ValueError("Square must be between 1 and 64")

def total():
    sum = 0
    for i in range(1, 65):
        sum += i
    return sum