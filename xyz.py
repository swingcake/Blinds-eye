import numpy as np 
t=int(input())

for i in range (t):
    apple,box = list(map(int,input().split()))
    
    if(apple == box):
        print("YES")
    elif(box == 1):
        print("NO")
    else:
        for n in range(1,1000):
            if(apple == np.power(box,n)):
                print("NO")
            else:
                print("YES")
            

            
