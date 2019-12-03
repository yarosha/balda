def vocabulary():
    string = ''
    voc = []
    correct_vocabulary = {}
    f = open('vocabulary.txt', encoding='utf-8')
    for line in f:
        for i in range(len(line)-1):
            string += line[i]
        voc.append(string)
        string = ''
    for elem in voc:
        correct_vocabulary[elem] = len(elem)
    return correct_vocabulary


def check_function(word, vocabulary):
    if word in vocabulary.keys():
        return vocabulary[word]
    else:
        return 0


v = vocabulary()
print(check_function('абажур', v))