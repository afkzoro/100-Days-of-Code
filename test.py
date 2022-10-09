def steps(number):
    count = 0
    div = number
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number > 0:
        while div != 1:
            if div % 2 == 0:
                div = div / 2
                count += 1
            div = 3 * div + 1
            count += 1
    return count
