def minion_game(string):
    vowels = 'AEIOU'
    the_word = string
    Stuart_score, Kevin_score = 0, 0
    length = len(the_word)
    for index in range(0, length):
        score = length - index
        if the_word[index] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    if Stuart_score < Kevin_score:
        print('Kevin {}'.format(Kevin_score))


if __name__ == '__main__':
    s = input()
    minion_game(s)
