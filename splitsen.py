import random, sys

score = 0

while True:

    som = random.randint(1, 10)
    deel = random.randint(1, som-1)
    if ((som-deel) > 10):
#        print('Moeilijke som overgeslagen!')
        continue
    
    answer = str(som - deel)


    print("\nNienke: %d is %d + ...?" % (som, deel))

    userIn = input("--> ")

    while (userIn.isdigit()==False):
        print("Tiep een getal!")
        userIn = input("Probeer het nog een keer : ")
        
    if userIn == answer:
        print ("\n********* SUPER NIENKE *********** ")
        score+=1
    else:
        print ("\nJammer, Nienke.")
        print ("Het goed antwoord was: %d is %d + %d" % (som, deel, som-deel))
    
    scoretekst = "Je score is %d" % (score)
    print (scoretekst)
     
#    print ("Play again? y/n")
#    again = input("--> ")
    
#    if again != "y":
#        break
