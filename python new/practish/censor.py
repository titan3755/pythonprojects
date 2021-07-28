def censor_string(txt, lst, char):
    main = str(txt).split(' ')
    for word in main:
        if word in lst:
            index = main.index(word)
            length = ''
            for x in range(len(word)):
                length += char
            main[index] = length
        else:
            pass
    censored_sentence = ' '.join(main)
    return censored_sentence


censor_string('aho vatija aho', ['vatija'], '-')