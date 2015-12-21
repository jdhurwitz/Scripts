import glob
import os


CWD = os.getcwd()
PATH = os.path.dirname(CWD)

os.chdir(CWD+"/SP500")

filenames = []
num_read = 0;
num_selected = 0;
num_entered = 0;
for file in glob.glob("*.csv"):
    f = open(file, 'r')
    firstline = f.readline()
    secondline = f.readline()
   # print(secondline[0:15])
    if(secondline[0:15] == "12/30/2002,0930"):
      print(secondline + '\n')
      filenames.append(os.path.splitext(file)[0])
      num_selected += 1
    f.close()

    num_read += 1

f = open('sorted.txt', 'w')
for name in filenames:
    f.write(name+'\n')
#    print(name)
    num_entered += 1
f.close()
    

print("number read: ", num_read,"\n")
print("number qualify: " , num_selected, "\n")
print("total # written to file: ", num_entered, "\n")
