import random
response=input("Do you want to roll the dice? ")

while response==y:
    no= random.randint(1,6)
    if(no==1):
        print('[------]')
        print('[      ]')
        print('[   0  ]')
        print('[      ]')
        print('[------]')   
    elif(n0==2):
        print('[------]')
        print('[      ]')
        print('[0    0]')
        print('[      ]')
        print('[------]')   
    elif(n0==3):
        print('[-------]')
        print('[       ]')
        print('[0  0  0]')
        print('[       ]')
        print('[-------]') 
    elif(no==4):
         print('[------]')
         print('[0    0]')
         print('[      ]')
         print('[0    0]')
         print('[------]')  
    elif(no==5):
        print('[------]')
        print('[0    0]')
        print('[   0  ]')
        print('[0    0]')
        print('[------]')
    else:
        print('[------]')
        print('[0    0]')
        print('[0    0]')
        print('[0    0]')
        print('[------]')

    response=input("Press y to roll again and n to exit: ")


