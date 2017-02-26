from cmath import exp, log10
from math import floor
from random import randint
from gifts import Gift
from couples import Couple
from boys import Boy
from girls import Girl
from utility import Utili
from csv import *
from logging import *


basicConfig(format='%(asctime)s %(name)s - %(levelname)s %(message)s:',datefmt='%d/%m/%Y %I:%M:%S %p',level=DEBUG,filename='logs.txt',filemode='w')


def calculate_happiness(C):
    with open('Gifts.csv','r') as csvfile:
        reader = reader(csvfile,delimiter = ',')
        GFT = [Gift(row[0],int(row[1]),int(row[2]),row[3])for row in reader]
        csvfile.close()

    GFT = sorted(GFT,key=lambda k:k.price)
    info('Gifting')
    for c in C:
        if (c.boy.type == 'Miser'):
            happy_miser(GFT,c)

        if (c.boy.type == 'Generous'):
            happy_generous(GFT,c)

        if (c.boy.type == 'Geek'):
            happy_geek(GFT,c)

    print_gifts(C)



def allocate():

    f = open('Boys.csv','r')
    read = reader(f, delimiter = ',')
    Boys = [Boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5])for row in read]
    f.close()


    f = open('Girls.csv','r')
    read = reader(f, delimiter = ',')
    Girls = [Girl(row[0],int(row[1]),int(row[2]),int(row[3]),row[4])for row in read]
    f.close()


    CP = []
    info('Profile Matching start:\n')
    for girl in Girls:
        for boy in Boys:
            info('Commitment: Girl ' + girl.name +' is checking profile of Boy '+boy.name)
            if (boy.is_elligible(girl.budget,girl.attribute)) and (girl.is_elligible(boy.budget)) and girl.status == 'single' and boy.status == 'single':
                girl.status = 'commited'
                boy.status = 'commited'
                girl.bname = boy.name
                boy.gname = girl.name
                info('Commitment Girl: '+girl.name+' got commited with boy: '+boy.name)
                CP += [(boy,girl)]
                break


    print("Couples formed \n")
    for girl in Girls:
        if girl.status == 'single':
            print('Girl: ' + girl.name + '  single')
        else:
            print('Girl: ' + girl.name + '  is commited with  Boy: ' + girl.bname)
    print("-"*100)
    C = [Couple(c[0],c[1]) for c in CP]
    calculate_happiness(C)



def print_gifts(C):
	for c in C:
		print('Gifts given from Boy:  ' + c.boy.name + '  to Girl:  ' + c.girl.name + ':')
		for girl in c.GFT:
			print('Gift named:  ' + girl.name + '  of type:  ' + girl.type)
		print ('\n')
		k = randint(1, len(C))
	print_hc(C, k)


def print_hc(C, k):
	A = sorted(C, key=lambda item: item.happiness)
	Boys = sorted(C, key=lambda item: item.compatibility)
	print(str(k) + ' most Happy couples:')
	for i in range(k):
		print (A[i].boy.name + ' and ' + A[i].girl.name)

	print ('\n' + str(k) + ' most Compatible couples:')
	for i in range(k):
		print(Boys[i].boy.name + ' and ' + Boys[i].girl.name)


def happy_miser(GFT, c):
	v1 = 0
	v2 = 0
	for girl in GFT:
		if (girl.price == c.girl.budget) or (girl.price - c.girl.budget <= 100) and (c.boy.budget >= 0) and (c.boy.budget - girl.price > 0):
			if (girl.type == 'Luxury'):
				v2 = v2 + 2*girl.price
			else:
				v2 = v2 + girl.price
			v1 = v1 + girl.price
			c.GFT = c.GFT + [girl]
			c.boy.budget = c.boy.budget - girl.price
			info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + girl.name + ' of price = ' + str(girl.price) + ' rupees')

	if (c.girl.type == 'Choosy'):
		c.girl.happiness = log10(v2 if v2 > 0 else 1).real
	elif (c.girl.type == 'Normal'):
		c.girl.happiness = v1
	else:
		c.girl.happiness = exp(v1).real
	c.boy.happiness = c.boy.budget
	c.set_happiness()
	c.set_compatibility()


def happy_generous(GFT, c):
	v1 = 0
	v2 = 0
	for girl in GFT:
		if ((girl.price == c.boy.budget) or (c.boy.budget-girl.price <= 300)) and (c.boy.budget >= 0) and (c.boy.budget - girl.price > 0):
			if (girl.type == 'Luxury'):
				v2 = v2 + 2*girl.price
			else:
				v2 = v2 + girl.price
			v1 = v1 + girl.price
			c.GFT = c.GFT + [girl]
			c.boy.budget = c.boy.budget - girl.price
			info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + girl.name + ' of price = ' + str(girl.price) + ' rupees')
	if (c.girl.type == 'Choosy'):
		c.girl.happiness = log10(v2 if v2 > 0 else 1).real
	elif (c.girl.type == 'Normal'):
		c.girl.happiness = v1
	else:
		c.girl.happiness = exp(v1).real
	c.boy.happiness = c.girl.happiness
	c.set_happiness()
	c.set_compatibility()


def happy_geek(GFT, c):
	v1 = 0
	v2 = 0
	for girl in GFT:
		if (girl.price == c.girl.budget) or (girl.price-c.girl.budget <= 100) and (c.boy.budget >= 0) and (c.boy.budget - girl.price > 0):
			if (girl.type == 'Luxury'):
				v2 = v2 + 2*girl.price
			else:
				v2 = v2 + girl.price
			v1 = v1 + girl.price
			c.GFT = c.GFT + [girl]
			c.boy.budget = c.boy.budget - girl.price
			info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + girl.name + ' of price = ' + str(girl.price) + ' rupees')

	for i in GFT:
		if (i not in c.GFT) and (i.type == 'luxury') and (i.price <= c.boy.budget):
			v2 = v2 + 2*i.price
			v1 = v1 + i.price
			c.GFT = c.GFT + [i]
			c.boy.budget = c.boy.budget - i.price
			info('Gifting:  Boy: ' + c.boy.name + '  gave his Girlfriend: ' + c.girl.name + '  Gift: ' + i.name + ' of price = ' + str(i.price) + ' rupees')
			break


	if (c.girl.type == 'Choosy'):
		c.girl.happiness = log10(v2 if v2 > 0 else 1).real
	elif (c.girl.type == 'Normal'):
		c.girl.happiness = v1
	else:
		c.girl.happiness =exp(v1).real
	c.boy.happiness = c.girl.intelligence
	c.set_happiness()
	c.set_compatibility()


Utili()
allocate()
