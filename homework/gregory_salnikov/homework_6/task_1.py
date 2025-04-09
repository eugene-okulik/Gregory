text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero.'
)

words = text.split()
fin_words = []

for word in words:
    if word.endswith('.') or word.endswith(','):
        punctuation = word[-1]
        word_without_punctuation = word[:-1] + 'ing'
        fin_words.append(word_without_punctuation + punctuation)
    else:
        fin_words.append(word + 'ing')

print(' '.join(fin_words))

