indice = 0
indice2 = 0
controle = 0
while indice <= 100 :
    controle = 0
    indice2 =  indice
    
    
    while indice2 > 0 :
        if(indice % indice2 == 0):
            controle += 1
        indice2 -= 1
    
    if (controle == 2):
    
        print (indice)
    
    indice += 1
