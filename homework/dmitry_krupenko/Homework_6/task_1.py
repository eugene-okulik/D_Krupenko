text_orgin = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
               + 'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text_orgin.split(' ')
fin_text = []
for word in words:
    if '.' in word[-1]:
        final_word = word[:-1] + 'ing' + word[-1]
    elif ',' in word[-1]:
        final_word = word[:-1] + 'ing' + word[-1]
    elif ',' or '.' not in word:
        final_word = word + 'ing'
    fin_text.append(final_word)
print(' '.join(fin_text))
