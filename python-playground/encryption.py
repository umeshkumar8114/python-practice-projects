

encrypt_code = {'A':')', 'a':'0', 'B':'(', 'b':'9', 'C':'*', 'c':'8',
                'D':'&', 'd':'7', 'E':'^', 'e':'6', 'F':'%', 'f':'5',
                'G':'$', 'g':'4', 'H':'#', 'h':'3', 'I':'@', 'i':'2',
                'J':'!', 'j':'1', 'K':'Z', 'k':'z', 'L':'Y', 'l':'y',
                'M':'X', 'm':'x', 'N':'W', 'n':'w', 'O':'V', 'o':'v',
                'P':'U', 'p':'u', 'Q':'T', 'q':'t', 'R':'S', 'r':'s',
                'S':'R', 's':'r', 'T':'Q', 't':'q', 'U':'P', 'u':'p',
                'V':'O', 'v':'o', 'W':'N', 'w':'n', 'X':'M', 'x':'m',
                'Y':'L', 'y':'l', 'Z':'K', 'z':'k', '!':'J', '1':'j',
                '@':'I', '2':'i', '#':'H', '3':'h', '$':'G', '4':'g',
                '%':'F', '5':'f', '^':'E', '6':'e', '&':'D', '7':'d',
                '*':'C', '8':'c', '(':'B', '9':'b', ')':'A', '0':'a',
                ':':',', ',':':', '?':'.', '.':'?', '<':'>', '>':'<',
                "'":'"', '"':"'", '+':'-', '-':'+', '=':';', ';':'=',
                '{':'[', '[':'{', '}':']', ']':'}', ' ': ' '}


def encrypt(string):
    qw = string.split()
    encoded = []
    for elt in qw:
        for char in elt:
            symbols = encrypt_code.get(char)
            encoded.append(symbols)
        encoded.append(' ')
    combination = ''.join(encoded)
    return combination


filename = input("Enter the name of the input file (with extension): ")
filename2 = input("Enter the name of the output file (with extension): ")
file1 = open(filename, "r")
file2 = file1.read()
file1.close()
file3 = open(filename2, "w")
file3.write(encrypt(file2))
file3.close()

