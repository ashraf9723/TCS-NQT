from math import *
def printDivisor(n):
    
     i=1
     while(i*1<n):
         if(n%i == 0):
             print(i,end=" ")
             
         i +=1
     for i in range(int(sqrt(n)),0,-1):
         if(n%i == 0):
             print(n//i , end=" ")
             
print("The divisors of 33 are: ")
 
printDivisor(33)