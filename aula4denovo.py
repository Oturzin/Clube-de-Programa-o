import random 


num = random.randint(1,  100)



while 1:
    
    palpite = input('Digite um numero')
    palpite = int (palpite)
    if palpite  ==  num:
        print ('ganhou')
    elif palpite < num:
        print('numero maior')
    elif palpite > num:
        print ('numero menor')
      
