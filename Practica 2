def provaentrada():
    grup1=raw_input("Digues-me un grup musical(1) ")
    grup2=raw_input("Digues-me un grup musical(2) ")
    punt1=input("Diguem una puntuació entre 0 i 1 del grup 1: ")
    punt2=input("Diguem una puntuació entre 0 i 1 del grup 2: ")
    edat1=input("Digues-me l'edat del/de la cantant principal del grup 1: ")
    edat2=input("Digues-me l'edat del/de la cantant principal del grup 2: ")
    espanyol1=bool(input("Indica si canten en espanyol (1) (respon True o False)"))
    espanyol2=bool(input("Indica si canten en espanyol (2) (respon True o False)"))
    print "El teu grup 1 és: %s, el cantant principal té %i anys," %(grup1, edat1),
    if(espanyol1==True):
        print  "parlen espanyol,", 
    print "i tenen una puntuació de %2.1f" %(punt1) 
    print "El teu grup 2 és: %s, el cantant principal té %i anys," %(grup2, edat2),
    if(espanyol2==True):
        print  "parlen espanyol,",
    print "i tenen una puntuació de %2.1f" %(punt2)     
    
def futval2(anys):
    print "Càlcul del valor futur d’una inversio a 12 anys."
    principal = input("Entra la inversio inicial: ")
    apr = input("Entra l'interes anual: ")
    for i in range(anys):
        principal = principal * (1 + apr)
    print "La quantitat al cap de",anys,"anys es:", principal

def convert(temp):
    fahrenheit = 9.0 / 5.0 * temp + 32
    print "{:3}".format(temp),"ºC =", "{:3.2f}".format(fahrenheit), "ºF" #Creates a table of values and testing output method
    
def convert2():
    for temp in range(0, 110, 10):
        convert(temp)
        
def exp():
    import math
    print 4.0 / 10.0 + 3.5 * 2
    print 10 % 4 + 6 / 2
    print abs(4 - 20 / 3) ** 3 #20/3!=20.3. then answer will be int
    print math.sqrt(5.5 - 5.0) + 7 * 3 #Sqrt not defined. We need to import function sqrt
    #print 5/(4.2 + 0.3 - 4.5) #4.2+0.3-4.5 = 0 cannot divide by 0
    print 3 * 10 / 3 + 10 % 3
    print 3L ** 3
    
def pendent(x1,y1,x2,y2):
    if(x2-x1==0):
        m="inf" #Avoid divide by 0
    else:
        m=(float(y2)-float(y1))/(float(x2)-float(x1))
    print "Pendent =", m
    
def euclid(x1,y1,x2,y2):
    import math #Import math library to use sqrt function
    d=math.sqrt((x2-x1)**(2)+(y2-y1)**2)
    print "Distance =", d
    
def euclid2(x1,y1,x2,y2):
    import math #Import math library to use sqrt function
    d=math.sqrt((x2-x1)**(2)+(y2-y1)**2)
    print "Distance =", int(round(d))
    
def factmenor():
    fact=1
    i=2
    while(fact<620448401733239439360000): #I use while and not for or if to make just the number of operations I need
        print fact
        #Factorial:
        fact*=i #Multiply per i
        i+=1 #Add 1 
        
def suma():
    sum=0
    for i in range(1000):
        if(i%3==0 or i%5==0): #If remainder is 0 in either case, that means the number is multiple of 3 or 5
            sum+=i
    print sum

def divisible():
    #If a number is multiple of 8, it is of 2 and 4 too
    #If a number is multiple of 9, it is of 3 too
    #If a number is multiple of 10, it is of 2 and 5 too
    #We are looking for a number that is multiple of 6,7,8,9 and 10
    i=10 #We start at the maximum
    while(i%6!=0 or i%7!=0 or i%8!=0 or i%9!=0 or i%10!=0):
          i+=1  
    print i
    
