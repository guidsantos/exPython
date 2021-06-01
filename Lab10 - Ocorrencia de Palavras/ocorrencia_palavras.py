from unidecode import unidecode


def filter_phase(phase: list):
    phase_list = []
    for line in phase:
        filter = [".", ",", ":", ";", "!", "?"]
        for i in filter:
            line = unidecode(line).replace(i, '')
        phase_list.append(line.lower().split())
    return phase_list


def find_words(words: list, phase: list):
    found_words = []
    for searched_word in words:
        quant_word = 0
        quant_similiar_word = 0
        searched_word_lower = searched_word.lower()
        for line in phase:
            for word in line:
                if word == searched_word_lower:
                    quant_word += 1
                if searched_word_lower in word:
                    quant_similiar_word += 1
        count_word = [searched_word, quant_word,
                      quant_similiar_word-quant_word]
        found_words.append(count_word)
    return found_words


l = int(input('Quantas linhas tem seu texto: '))

phase = []
for line_index in range(0, l):
    line = str(input(f"Insira a {line_index+1}º linha: "))
    phase.append(line)

n = int(input('Quantas palavras serão buscadas: '))

words = []
for word_index in range(0, n):
    word = str(
        input(f'Digite a {word_index+1}º palavra que deseja encontrar: '))
    words.append(word)


phase_list = filter_phase(phase)

word_count = find_words(words, phase_list)

for word in word_count:
    print(
        f'\nPalavra buscada: {word[0]}\n'
        f'Ocorrencia: {word[1]}\n'
        f'Palavras similares: {word[2]}')
print()
