'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case, if the current word cannot physically contain 'th', return 0
    if len(word) < 2:
      return 0
    # if the current two chars are th, increment a count, and skip a character
    # a character can be skipped since the previous last character is H, it's pointless to check the next character
    elif word[0] == "t" and word[1] == "h":
      return 1 + count_th(word[2:])
    # if there are n > 2 chars left in the word, and the current two indices are not 'th', progress the recursion
    else:
      return count_th(word[1:])
