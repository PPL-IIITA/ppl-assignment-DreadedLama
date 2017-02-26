from csv import writer
import random


def create(file_name , gender):

    f = open(file_name,"w")    		#Open a csv file to write data in it
    write = writer(f,delimiter = ',')   #seperate wrt ,

    for i in gender:
        write.writerow(i)
    f.close()				#Close the file


def utility():

    Girl = [('Girl_'+str(g),random.randint(1,200),random.randint(1,1100),random.randint(250,2500)) for g in range(1,60)]       			#Attractive,Intelligence,Maintainance
    Boy = [('Boy_'+str(b),random.randint(1,200),random.randint(1,1150),random.randint(150,3000),random.randint(1,160))for b in range(1,101)]    #Attrictive, Intelligence,Maintainance ,Min attractivness req

    create('Boys.csv',Boy)
    create('Girls.csv',Girl)




    
