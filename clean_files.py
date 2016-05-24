#cleaning the data
import io
import glob

with io.open("stg1_file.txt","w") as finalfile:
	
	path = 'C:\\Users\\Hilary\\AppData\\Local\\Programs\\Python\\Python35-32\\turnstile_130[7-9]*.txt'
	files = glob.glob(path)
	
	for file in files:
	
		f = open(file,'r')
		for line in f:
			line = line.strip()
			cur = line.split(",")
			length=len(cur)
			i=3
			if ((length-3) % 5 == 0):
				while i<length:
					row=cur[0] + ','+cur[1]+','+cur[2]
					j=0
					while j<5:
						row=row+ ','+cur[i+j]
						j=j+1
					finalfile.write(row+'\n')		
					i = i+5
			else:
				print('error line')
