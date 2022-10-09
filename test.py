def is_isogram(word):
    result = word
    if "-" in word:
        result = word.replace("-", " ")
    result = "".join(result.split())
    return len(result) == len(set(result.lower()))