from random import randint
import csv

def randomInputGenerate():

	boy_types = ['Miser','Generous','Geek']
	girl_types = ['Choosy','Normal','Desperate']
	
	Boy = []
	Girl = []
	for i in range (0,20) :
		Boy += [('Boy'+str(i),randint(1,10),randint(1,5),boy_types[randint(0,2)],randint(1,10),100*randint(1,10))]
	for i in range (0,10):
		Girl += [('Girl'+str(i),randint(3,10),100*randint(1,6),girl_types[randint(0,2)],randint(1,10))]

	create('boys.csv',Boy)
	create('girls.csv',Girl)
def create(file,list):
	f = open(file,'wr')
	writer = csv.writer(f,delimiter = ",")

	for i in list:
		writer.writerow(i)
randomInputGenerate()
