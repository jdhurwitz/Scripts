import glob
import os
import time
import multiprocessing as mp

multithread = 1
num_processes = 0
CWD = os.getcwd()
WRITEDIR = os.getcwd()+"/Gap Calculations/"
if not os.path.exists(WRITEDIR):
	os.makedirs(WRITEDIR)

os.chdir(CWD+"/SP500")

output = mp.Queue()


sorted_names = open("sorted.txt" ,'r')
counter = 0;

#30 days: September, Novemebr, April, June
#31 days: January, March, May, July, August, October, December
#28 days: February
#29 days: February in leap years
#Leap years since 2002: 2004, 2008, 2012

#String to int to avoid issue with octal leading zeroes
month_to_day = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}


def calculateGaps(ticker):
   file = open(ticker.rstrip()+'.csv', 'r')
   file.readline() #junk first line

   day_prev = 0
   month_prev = 0
   gaplength = 0

   complete_name = os.path.join(WRITEDIR, ticker.rstrip()+".txt")
   gfile = open(complete_name, 'w')
   for line in file:
        #Verification steps
	

        month = line[0:2]
        day = line[3:5]
        year = line[6:10]

	if(month_prev != 0):
		if(int(day) != int(day_prev)+1):
			gaplength = (int(day) - int(day_prev))-1
		else:
			gaplength = 0
	if(gaplength > 2):
		gap_output = (month,day,year, "gap length is: " + str(gaplength))
		print(gap_output)
		gfile.write(str(gap_output)+"\n")


	day_prev = day
	month_prev = month


   gfile.close()
   file.close()

if(multithread):
	processes = [mp.Process(target=calculateGaps, args=(ticker,)) for ticker in sorted_names]

	for p in processes:
		p.start()
		num_processes += 1

	for p in processes:
		p.join()
else:
	for ticker in sorted_names:
		calculateGaps(ticker)


sorted_names.close()
print("Multithreading: "+str(multithread), "Num processes: " +str(num_processes))

