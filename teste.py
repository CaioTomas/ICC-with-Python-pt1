import string

fname = input('Enter a file name: ')

try:
    fhandle = open(fname)
except:
    print('Cannot open', fname)
    exit()
    
count = dict()
    
for line in fhandle:
    line.rstrip()
    line.translate(line.maketrans('', '', string.punctuation))
    line.lower()
    words = line.split()
    for word in words:
        letters = list(word)
        for letter in letters:
            if letter.isdigit() == False:
                count[letter] = count.get(letter, 0) + 1

lst = list()

for key, val in count.items():
    lst.append((val, key))
    
lst.sort(reverse=True)

for key, val in lst:
    print(key, val)
