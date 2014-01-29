import random, sys

score = 0

while True:


    som = random.randint(10, 20)
    deel = random.randint(1, 10)
    if ((som-deel) > 10):
#        print('Moeilijke som overgeslagen!')
        continue
    
    answer = str(som - deel)


    q1 = "\nNienke: %d is %d + ...?" % (som, deel)
    print(q1)

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
