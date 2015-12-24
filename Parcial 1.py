
#Exercise 1
import math
def fib(n):
    a=0 #Set initial values
    b=1
    for i in range(n): #Calculates the following with the old numbers
        a,b=b+a,a
    return a

#We could also use a list to save the old numbers and avoid calculating every time we need one
def pi_fib(n):
    pi=0 #Initializes pi to 0
    for i in range(1,n+1): #From 1 to 10 (If we write n, "for" would only use numbers from 1 to 9)
        pi+=math.atan(1./fib(2*i+1)) #1. transforms 1 to float to avoid division problems
    return 4*pi #Multiplies the value from the for by 4




#Exercise 2

def my_string_split(text,c):
    sol=[] #Initialices both lists. sol will have the locations where c is; textspt will have the splited text 
    textspt=[]
    for i,l in enumerate(text):
        if(l==c):
            sol.append(i) #Finds where c is in the text and saves its position
    sol.append(len(text)) #Adds the last character + 1 as position
    j=0 #Starts at the begining of the text
    for i in sol:
        textspt.append(text[j:i]) #Takes the text between c anc c (or start and c, and c and end)
        j=i+1 #Picks the next starting position
    return textspt #Returns the splited text




#Exercise 3
def to_binary_rec(n):
    if(n==1): #If n is already 1, we go back
        return n 
    r=n%2 #Calculates the residum
    n/=2  #Divides n by 2
    lastnum=to_binary_rec(n) #Gets the binary expresion of n/2
    lastnum=lastnum*10+r #Adds the residum at the end of the expresion of n/2
    return lastnum #Returns the binary expresion of n





