import os
import filecmp

sorted = open("sorted.txt", 'r')
filenames = []
for line in sorted:
    if(line == "A"):
        pass
    filenames.append(line)

os.chdir(os.getcwd()+'/Gap Calculations')


compare = open('compare.txt', 'w')
for file in os.listdir(os.getcwd()):
    if(file == "sorted.txt" or file == "compare.txt" or file == "concatenated.txt"):
        pass
    else:
        if(filecmp.cmp('A.txt', file) == False):
            compare.write(file+'\n')

sorted.close()
compare.close()
