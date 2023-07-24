codes ={'A':"~ ",
        'a':"!",  
        'B':"@", 
        'b':"\." ,
        'C':'#' ,
        'c':'/' ,
        'D':'$' ,
        'd':'-' ,
        'E':'*' ,
        'e':'%' ,
        "F":'^' ,
        'f':'.' ,
        'G':',',
        'H':'>',
        'h': '?',
        'I':'!',
        'i':'@',
        'J':'#' ,
        'j':'$',
        'K':'%',
        'k':'^',
        'L':'&',
        'l':'*',
        'M':'/',
        'm':"." ,
        'N':"|" ,
        'n':"|",
        'O':"/" ,
        'o': '.',
        'P': '-',
        'p': '_',
        'Q': '+',
        'q': '=',
        'R': '!',
        'r': '!!',
        'S': '@@',
        's': '#',
        'T': '%',
        't': '^^',
        'U': '&',
        'u': '**',
        'V': '*&',
        'v': '%@',
        'W': '!@',
        'w': '&*',
        'X': '/<',
        'x': '><',
        'Y': '<>',
        'y': '!>',
        'Z':' @',
        'z':'!'
        
        }
print(codes)

infile= open('info_security-1.txt','r')
new_file=infile.read()
infile.close()

encrypted_file= open('encrypted.txt','w')

for ch in new_file:
    if ch in codes:
        encrypted_file.write(codes[ch])

encrypted_file.close()
    