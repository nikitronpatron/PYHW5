## Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "ваб бав авб абв вабв вабвб абвбв"
text = " ".join(list(filter(lambda word: "абв" not in word, text.split())))
print(text)