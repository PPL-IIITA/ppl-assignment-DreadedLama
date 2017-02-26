from boys import Boy
from girls import Girl
from utility import utility
from logging import *
from csv import reader


basicConfig(format='%(asctime)s %(name)s - %(levelname)s %(message)s:',datefmt='%d/%m/%Y %I:%M:%S %p',level=DEBUG,filename='logs.txt',filemode='w')


def allocate():

    f = open('Girls.csv','r')											#read girls data
    read = reader(f, delimiter = ',')
    Girls = [Girl(str(row[0]),int(row[1]),int(row[2]),int(row[3]))for row in read]
    f.close()

    f = open('Boys.csv','r')											#read boys data
    read = reader(f, delimiter = ',')
    Boys = [Boy(str(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4]))for row in read]
    f.close()

    info('Profile Matching started: ')

#matching boys and  girls

    for girl in Girls:
        for boy in Boys:
            info('Commitment: Girl ' + girl.name +' is checking profile of Boy '+boy.name)
            if (boy.is_elligible(girl.budget,girl.attribute)) and (girl.is_elligible(boy.budget)) and girl.status == 'single' and boy.status == 'single':
                girl.status = 'commited'
                boy.status = 'commited'
                girl.bf_name = boy.name
                boy.gf_name = girl.name
                info('Commitment Girl: '+girl.name+' got commited with boy: '+boy.name)
                break

#print the couples formed

    print("Couples formed")
    for girl in Girls:
        if girl.status == 'single':
            print(girl.name + '  is not commited to anyone')
        else:
            print(girl.name + '  is commited with ' + girl.bf_name)



utility()
allocate()
