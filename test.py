def pangram(sentence):
    return not set('abcdefghijklmnopqrstuvwxyz') - set(sentence.lower())
