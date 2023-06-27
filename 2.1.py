""""В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку."""

with open('txt.txt', encoding='utf-8') as f:
    text = f.read()

text = "".join([i.lower() for i in text if i.isalpha() or i == " "])
words = text.split()

n = 10
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Сортировка по количеству и по алфавиту
sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))[:n]
for word, count in sorted_words:
    print(f"Слово {word} встречается {count} раз")
