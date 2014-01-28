import random, sys

score = 0

while True:


    som = random.randint(10, 20)
    deel = random.randint(1, 10)
    if ((som-deel) > 10):
#        print('Moeilijke som overgeslagen!')
        continue
    
    answer = str(som - deel)


    q1 = "\nNienke, %d is %d + ...?" % (som, deel)
    print(q1)

    userIn = input("--> ")

    if userIn.isdigit() == False:
        print("Tiep een getal!")  
        

        # Start again at the top of the loop.
        continue
    elif userIn == answer:
        print ("SUPER NIENKE")
        score+=1
    else:
        print ("Jammer, Nienke.")
    
    scoretekst = "Je score is %d" % (score)
    print (scoretekst)
     
#    print ("Play again? y/n")
#    again = input("--> ")
    
#    if again != "y":
#        break
