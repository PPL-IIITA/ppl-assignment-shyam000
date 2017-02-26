from boy import Boy
from girl import Girl
from randomInput import randomInputGenerate
import csv
import logging

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',			level=logging.DEBUG,filename='log.txt',filemode='w')

def main():
	randomInputGenerate()
	BoyCsv = open('./boys.csv')
	GirlCsv = open('./girls.csv')
	Boys = csv.reader(BoyCsv,delimiter = ",")
	Girls = csv.reader(GirlCsv,delimiter = ",")
	Blist = []
	Glist = []
	for row in Boys:
		Blist += [Boy(row[0],int(row[1]),int(row[2]),row[3],int(row[4]),int(row[5]))]
	BoyCsv.close()
	
	for row in Girls:
		Glist += [Girl(row[0],int(row[1]),int(row[2]),row[3],int(row[4]))]
	GirlCsv.close()


	logging.info('Started pairing up')
	for g in Glist:
		for b in Blist:
			logging.info('Girl '+g.name+' is checking on '+b.name)
			if (b.isEligible(g.maintainanceBudget,g.attractiveness)) and (g.isEligible(b.budget)) and (b.status == 'single') and (g.status == 'single'):
				b.status = 'commited'
				g.status = 'commited'
				b.gf = g.name
				g.bf = b.name
				logging.info(g.name+' is commited to '+b.name)
				break
	
	for g in Glist:
		if(g.status == 'single'):
			print(g.name+' is single')
		else:
			print(g.name+' is commited to '+g.bf)
main()
			
