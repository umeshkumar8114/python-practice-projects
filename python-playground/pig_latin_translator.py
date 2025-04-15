

def convertToPigLatin(text):
    word_list = text.lower().split()
    list_of_words = []
    for word in word_list:
        words = word[1:] + word[0] + 'ay '
        list_of_words.append(words)
    text2 = ''.join(list_of_words)
    return text2


filename = input("Enter the name of input file (with extension): ")
filename2 = input("Enter the name of output file (with extension): ")
file2 = open(filename, 'r')
file3 = file2.read()
file2.close()
file4 = open(filename2, 'w')
file4.write(convertToPigLatin(file3))
file4.close()
