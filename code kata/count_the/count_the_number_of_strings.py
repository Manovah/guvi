str00 = input()
total = 1

for i in range(len(str00)):
    if(str00[i] == ' ' or str00 == '\n' or str00 == '\t'):
        total = total + 1

print( total)
