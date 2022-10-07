open_brackets = ["[","{","("]
close_brackets = ["]","}",")"]
def is_paired(myStr: str):
    record = []
    for i in myStr:
        if i in open_brackets:
            record.append(i)
        elif i in close_brackets:
            pos_index = close_brackets.index(i)
            if len(record) > 0 and open_brackets[pos_index] == record[-1]:
                record.pop()
            return False
    if not record:
        return True
    return False