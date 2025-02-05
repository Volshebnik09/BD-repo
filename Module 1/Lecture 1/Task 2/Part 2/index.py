def find_text_in_array(arr, search_text):
    search_text = search_text.lower()

    count = 0
    indices = []

    for index, element in enumerate(arr):
        if search_text in element.lower():
            count += 1
            indices.append(index)

    return count, indices


arr = [
    'Питон язык программирования',
    'Питон входит в 3 популярных языков программирования',
    'Питон использует динамическую типизацию',
    'Питон обладает интуитивно понятным синтаксисом'
]
search_text = input("Введите текст для поиска: ")

count, indices = find_text_in_array(arr, search_text)

print(f"n={count} {indices}")