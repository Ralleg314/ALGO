import math
def negatius(a):
    sol=[]
    neg=0
    f=0
    for i in a:
        if i<0: 
            sol.insert(neg,i)
            neg+=1 #Number of negatives
        elif i>0:
            sol.append(i) #Adds it at the end of the list
        else: #If there's a 0, sets flag to True
            f=1
    if f==0: #If there isn't a 0, returns the list with negative and positive numbers 
        return sol
    #If function gets here, there's a 0 in "a"
    sol.insert(neg,0)
    return sol
    
def exponent(a,b):
    if(b==1): #Stops when the exponent is 1
        return a
    if(b%2==0): #If the exponent is even, we use the formula above
        return exponent(a,b/2)*exponent(a,b/2)
    return exponent(a,b/2)*exponent(a,b/2)*a #If it's odd, multiplies it by a
    
def reverse(a):
    l=len(a) #Saves the list length
    if(l==2): #If length is 2, switches the letters
        return a[1]+a[0]
    elif(l==1):
        return a[0] #If l=1, returns the letter
    if(l%2==0):
        return reverse(a[(l/2):])+reverse(a[:(l/2)]) #If l is even, switches what the functions returns
    return reverse(a[((l/2)+1):])+a[l/2]+reverse(a[:(l/2)]) #If it's odd, the middle letter remais unchanged
    
