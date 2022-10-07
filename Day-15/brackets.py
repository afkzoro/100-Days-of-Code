from turtle import position


open_brackets = ["[","{","("]
close_brackets = ["]","}",")"]
def is_paired(myStr: str):
    """
    Loop through a string and match open and close brackets
    Pops it if they match.
    if lenght of new list is greater than or equal to 1 there's an unbalanced bracket
    """
    record = []
    for i in myStr:
        if i in open_brackets:
            record.append(i)
        elif i in close_brackets:
            pos_index = close_brackets.index(i)
            if ((len(record) > 0) and (open_brackets[pos_index] == record[len(record)-1])):
                record.pop()
            return False
    if len(record) == 0:
        return True
    return False