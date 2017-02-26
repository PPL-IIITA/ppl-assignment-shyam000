from Q2boy import boy
from Q2girl import girl
from Q2randomInput import randomInputGenerate
from Q2couple import couple
from Q2gift import gift
import csv
import logging
from math import log10,exp
from random import randint


logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',			level=logging.DEBUG,filename='log.txt',filemode='w')

def pairing():
	randomInputGenerate()
	BoyCsv = open('./boys.csv')
	GirlCsv = open('./girls.csv')
	Boys = csv.reader(BoyCsv,delimiter = ",")
	Girls = csv.reader(GirlCsv,delimiter = ",")
	Blist = []
	Glist = []
	coupleList = []
	for row in Boys:
		Blist += [boy(row[0],int(row[1]),int(row[2]),row[3],int(row[4]),int(row[5]))]
	BoyCsv.close()
	
	for row in Girls:
		Glist += [girl(row[0],int(row[1]),int(row[2]),row[3],int(row[4]))]
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
				coupleList += [couple(b,g)] 
				break
	
	calculateHappiness(coupleList)
	k = randint(3,len(coupleList))
	printHappyCouples(coupleList,k)
	
def printHappyCouples(coupleList,k):
	CH = sorted(coupleList, key=lambda item: item.happiness, reverse=True)
	CC = sorted(coupleList, key=lambda item: item.happiness, reverse=True)
	print('printing '+str(k)+' happy couples ')
	
	for i in range (0,k):
		print(CH[i].boy.name+' and '+CH[i].girl.name)
	print('printing '+str(k)+' compatible couples ')
	for i in range (0,k):
		print(CC[i].boy.name+' and '+CC[i].girl.name)

def calculateHappiness(C):
	giftCsv = open("./gifts.csv")
	Gifts = csv.reader(giftCsv,delimiter = ",")
	GiftList = []
	gP1 = 0
	gP2 = 0
	gV = 0
	bH = 0
	gH = 0
	for row in Gifts:
		GiftList += [gift(row[0],int(row[1]),int(row[2]),row[3])]	
	giftCsv.close()
	for c in C:
		if(c.boy.Type == 'Miser'):
			for g in GiftList :
				if (g.available == True) and (g.price <= c.boy.budget) and (g.price - c.girl.maintainanceBudget <= 100):
					logging.info(g.name+' is gifted by '+c.boy.name+' to '+c.girl.name)
					print(g.name+' is gifted by '+c.boy.name+' to '+c.girl.name)					
					g.available = False
					c.boy.budget -= c.boy.budget
					if(g.Type == 'Luxury'):
						gP1 += 2*(g.price)
						gP2 += g.price
						gV += g.value
					else:
						gP2 += g.price
						gV += g.value
			bH = c.boy.budget
			if(c.girl.Type == 'Choosy'):
				gH = log10(gP1)
			if(c.girl.Type == 'Normal'):
				gH = gP2 + gV
			if(c.girl.Type == 'Desperate'):
				gH = exp(min(500,gP2))
			c.happiness = bH + gH
			c.boy.happiness = bH
			c.girl.happiness = gH
			c.set_happiness()
			c.set_compatability()

		if(c.boy.Type == 'Generous'):
			AGifts = sorted(GiftList, key=lambda item: item.price, reverse=True)
			for g in AGifts :
				if (g.available == True) and (g.price <= c.boy.budget) :
					logging.info(g.name+' is gifted by '+c.boy.name+' to '+c.girl.name)
					print(g.name+' is gifted by '+c.boy.name+' to '+c.girl.name)					
					g.available = False
					c.boy.budget -= c.boy.budget
					if(g.Type == 'Luxury'):
						gP1 += 2*(g.value)
						gP2 += g.price
						gV += g.value
					else:
						gP2 += g.price
						gV += g.value
		
			if(c.girl.Type == 'Choosy'):
				gH = log10(gP2)
				gH = gH + gP1
			if(c.girl.Type == 'Normal'):
				gH = gP2 + gV
			if(c.girl.Type == 'Desperate'):
				gH = exp(min(500,gP2))
			bH = gH
			c.happiness = bH + gH
			c.boy.happiness = gH
			c.girl.happiness = gH
			c.set_happiness()
			c.set_compatability()
	
		if(c.boy.Type == 'Geek'):
			for g in GiftList :
					if (g.available == True) and (g.price <= c.boy.budget) and (g.price - c.girl.maintainanceBudget <= 100):
						logging.info(g.name+' is gifted by '+c.boy.name+' to '+c.girl.name)
						print(g.name+' is gifted by '+c.boy.name+' to '+c.girl.name)					
						g.available = False
						c.boy.budget -= c.boy.budget
						if(g.Type == 'Luxury'):
							gP1 += 2*(g.value)
							gP2 += g.price
							gV += g.value
						else:
							gP2 += g.price
							gV += g.value
			for g in GiftList :
				if (g.available == True) and (g.Type == 'Luxury') and (g.price <= c.boy.budget):
					logging.info(g.name+' is gifted by '+c.boy.name+' to '+c.girl.name)
					print(g.name+' is gifted by '+c.boy.name+' to '+c.girl.name)
					g.available = False
					c.boy.budget -= c.boy.budget
					gP1 += 2*(g.value)
					gP2 += g.price
					gV += g.value
	
			if(c.girl.Type == 'Choosy'):
				gH = log10(gP2)
				gH = gH + gP1
			if(c.girl.Type == 'Normal'):
				gH = gP2 + gV
			if(c.girl.Type == 'Desperate'):
				gH = exp(min(500,gP2))
			bH = c.girl.intelligence
			c.happiness = bH + gH
			c.boy.happiness = bH
			c.girl.happiness = gH
			c.set_happiness()
			c.set_compatability()

pairing()	
