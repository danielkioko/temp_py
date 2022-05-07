fname = input('Enter the file name: ')
fh = open(fname)
word_list = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in word_list:
            word_list.append(word)
print(sorted(word_list))