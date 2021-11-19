def is_palidrom(start_file):

    count = 0
    all_words = []
    while count != 15:
        letter = []
        sent = start_file.readline().split('\n')
        words = " ".join(sent)
        for i in words:
            if i.isalpha():
                letter.append(i.lower())
                ''.join(letter)
        if letter == letter[::-1]:
            all_words.append(words)
        count += 1
    start_file.close()

    output = open("task4_output.txt", "w", encoding="utf-8")
    for i in range(0, len(all_words)):
        output.write(all_words[i])
        output.write("\n")
    output.close()


st_file = open("task4.txt", "r", encoding="utf-8")
is_palidrom(st_file)

