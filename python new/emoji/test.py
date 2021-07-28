def emojify(words):
    main = words.split(' ')
    my_emojis = {
        ":)": "🙂",
        ":(": "🙁",
    }
    output = ""
    for x in main:
        output += my_emojis.get(x, x)
    return output

sentence = input('> ')
print(emojify(sentence))
