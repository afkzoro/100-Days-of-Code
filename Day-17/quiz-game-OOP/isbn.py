def character(text):
    text.split()
    num = 0
    s = '[ABCDEFGHIJKLMNOPQRSTUVWYZ]'
    for i in range(len(text)):
        if text[i] in s:
            num += 1
    if num >= 1:
        return True
    return False

def is_valid(isbn):
    if '-' in isbn:
        isbn = isbn.replace('-', '')
    if len(isbn) == 10 and character(isbn) is False:
        if "X" in isbn[:8]:
            return False
        if isbn[9] != "X":
            new_list = list(isbn)

        res = [int(x) for x in new_list]

        if isbn[9] == "X":
            res.append(10)

        mod = len(res)

        add = 0
        for i in range(len(res)):
            add += res[i] * mod
            mod -= 1
        if add % 11 == 0:
            return True
    return False