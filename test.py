#import os
#files = []
#for i in os.listdir('/home/khan/Desktop/Projetos/meterologia/'):
#    if i.endswith('.txt'):
#        files.append(open(i))
import glob
files = glob.glob('*.txt')
#print(files)
for i in files:
	with open(i, 'r+') as file:
		f_a = file.readlines()
		f_a = '.'.join(f_a)
		print(f_a)

with open('temps/todaysTemMax.txt') as file:
	f = file.readlines()
	f = ''.join(f)
	#f = file.append()
	print(f)