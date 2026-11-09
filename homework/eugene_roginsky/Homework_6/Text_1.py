text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
addon = 'ing'
words = text.split()
fin_words = []
for word in words:
    if ',' in word:
        word = word[:-1]
        fin_words.append(f'{word}{addon},')
    elif '.' in word:
        word = word[:-1]
        fin_words.append(f'{word}{addon}.')
    else:
        fin_words.append(f'{word}{addon}')
print(' '.join(fin_words))
