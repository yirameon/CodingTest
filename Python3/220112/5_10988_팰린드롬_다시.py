word=list(str(input()))
if list(reversed(word))==word:
    print('1')
elif list(reversed(word))!=word:
    print('0')