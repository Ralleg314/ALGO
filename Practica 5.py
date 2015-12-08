def fib1(n):
    if(n==1 or n==2):
        return 1
    return fib1(n-1)+fib1(n-2)
    
def mcd(x,y):
    t0=time.clock() #Sets intial time
    while(y!=0): #The loop will run for as long as y isn't 0
        x,y=y,x%y #Applies Euclides' algorithm
    maxcomdiv=x #GCD is x
    temps=(time.clock()-t0)*1000 #Calculates the time the algorithm took
    return (maxcomdiv,temps)
    
import math
def era1(n):
    A=[i for i in range(2,n+1)] #Creates a list of numbers between 2 and n (both included)
    llistaprimers=[] #Initialices the list
    while(A[0]<math.sqrt(n)): #The loop will only work while the first element in A is smaller than SQRT of the given n
                              #The greatest number a given n can be divided by is its square root
                              #If it can be divided by a greater number, it will give us a smaller prime, that we have already use
        llistaprimers.append(A[0]) #Adds the smaller number of the list (it will always be the smaller prime of A)
        A=[i for i in A[::-1] if i%A[0]!=0] #Removes the numbers that can be divided by A[0] from the end to the beggining
        A=A[::-1] #Reorders the list
    llistaprimers+=A #Adds the remainder prime numbers greater than sqrt(n)
    return llistaprimers

def era2(n):
    t0=time.clock()
    tantsprimers=len(era1(n)) #Uses the era1 function to make a list of prime numbers. 
                              #Then, we count how many items/prime numbers are in the list
    temps=(time.clock()-t0) #Calculates the time era1 took
    return (temps,tantsprimers)
    
def factorp(n):
    t0=time.clock()
    lim=math.sqrt(n) #Greatest prime number n can be divided by is sqrt of n, because, if it can be divided by one greater,
                     #it will be divided by a smaller prime too.
    lowprimes=[2,3,5,7,11,13] #This will work for numbers smaller than 13² (=169)
    for i in lowprimes:
        if(i<lim): #We will only use the smaller numbers according to sqrt
            if(n%i==0): #If it can be divided by the number, n is not prime
                return (False,(time.clock()-t0)*1000)
        else:
            break #If i es greater than sqrt, we don't need to test the numbers greater than this, so the number is prime
    return (True,(time.clock()-t0)*1000)

def modexp(x,y,n): #It's really "expensive" to calculate a^(n-1) (mod n) if n is big, so we implement modexp function 
                   #to make it "cheaper" and to avoid errors (if we don't use modexp, the funtion starts to fail with
                   # numbers greater than 29)
    if y==0:
        return 1
    z=modexp(x,y/2,n)
    if(y%2==0):
        return (math.pow(z,2))%n
    else:
        return (x*math.pow(z,2))%n

def fermatp(n):
    if(n<=5):
        return ("Too small number",0)
    t0=time.clock()
    alist=[2,3,5] #Values that we will use
    for a in alist:
        if(modexp(a,n-1,n)!=1): #Calculates if a^(n-1)=1 (mod n). If it isn't, n is not prime, so it returns false
            return (False,(time.clock()-t0)*1000) #Time in ms
    temps=(time.clock()-t0)*1000 #We don't need to write "else" because if the funcction gets here, any of the cases is "=1" 
    return (True,temps)
 
 
  
#RSA agorithm works because it's really difficult for a computer to calculate the given numbers
#without knowing the private key.
#There aren't any algorithms to factorise a number, so you can't know p and q in an easy way
#Using 127 byte keys you can calculate the keys in a reasonable ammount of time and make it 
#difficult to break to unknow people.
#If it was a smaller key, it would be easy to break
#If it was bigger, it would take too much time to calculate
import random
def mcdmod(x,y):
    while(y!=0): #The loop will run for as long as y isn't 0
        x,y=y,x%y #Applies Euclides' algorithm
    return x #GCD is x

def mcdext(a,b):
    if(a==0):
        return(b,0,1)
    else:
        g,y,x=mcdext(b%a,a)
        return (g, x-(b//a)*y, y)

def RSA():
    #I will work with p and q of 16 bits 
    primelist=[i for i in  era1(100000) if (i>32768 and i<65536)] #Picks all prime numbers of 16 bit
    l=len(primelist)-1
    p=primelist[random.randint(0,l)] #Pick 2 random numbers from the list
    q=primelist[random.randint(0,l)]
    n=p*q
    m=(p-1)*(q-1)
    e=random.randint(0,m-1) #Calculates a random number smaller than m and positive
    while (mcdmod(e,m)!=1): #We want a coprime number so we can have it's inverse, then, gdc must be 1
        e=random.randint(0,m-1)
    d=mcdext(m,e)[2] #Calculates d using extended eucides algorithm
    print "Public key:",n,e,"\nPrivate key:",n,d
    
