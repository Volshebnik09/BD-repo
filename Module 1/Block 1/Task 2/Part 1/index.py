import string


def find_words_starting_with_letter(text, letter):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    target_letter = letter.lower()
    filtered_words = [word for word in words if word.startswith(target_letter)]

    word_count = {}
    for word in filtered_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    result = []
    for word, count in word_count.items():
        result.append((word, count))

    return result


text = input("Введите текст: ")
letter = input("Введите букву: ")

output = find_words_starting_with_letter(text, letter)

print(f"n={len(output)} {output}")