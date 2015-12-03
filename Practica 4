def mentre(n,llista):
    divperdos=0
    while(n!=1):
        n/=2 #Divides the number by 2
        divperdos+=1 #Adds 1 to counter
    sumallista=0
    i=1
    n=llista[0]
    while(n!=999): #While the number we get is different of 999, we keep the sum
        sumallista+=n #Sums the number to the others
        n=llista[i] #Picks the next number of the list
        i+=1
    return (divperdos,sumallista)
    
    
def per(n):
    suma=0
    sumasenars=0
    for i in range(1,n+1): #Picks every number from 1 to n (both incuded)
        suma+=i
    for i in range(1,2*n+2,2): #We ony want odd numbers, so we start at an odd number (1) and sum 2 every iteration
        sumasenars+=i
    return (suma,sumasenars)

def inversio(interes_fix_anual):
    inv=100. #We consider initial inversion equal to 100 (float)
    anys=0 #Starts at year 0
    while(inv<=200.): #2*100=200, then we will iterate as long as the inversion is not, at least, double the initial
        inv=inv+((interes_fix_anual*inv)/100.) #Applies the inversion formula
        anys+=1 #Adds 1 to year counter
    return anys

def nota(num):
    notes={0:'Suspens',1:'Suspens',2:'Suspens',3:'Suspens',4:'Suspens',5:'Aprovat',
           6:'Aprovat',7:'Notable',8:'Notable',9:'Excel∙lent ',10:'Matricula'}
    #We make a dictionary with all the marks and the respective qualification
    num=int(num) #The decimal part is meaningless, so we wipe it away
    qualificacio=notes[num] #We take the qualification of the mark
    return qualificacio
    
def dni(numero):
    if(numero>9999999 and numero<=99999999): #Tests if the DNI has the correct length
        l={0:'T',1:'R',2:'W',3:'A',4:'G',5:'M',6:'Y',7:'F',8:'P',9:'D',10:'X',11:'B',
           12:'N',13:'J',14:'Z',15:'S',16:'Q',17:'V',18:'H',19:'L',20:'C',21:'K',22:'E'}
        #We make a dictionary number-letter
        numero%=23 #We take the remainder
        lletra=l[numero%23] #Picks the letter of the dictionary according to the number
    else:
        lletra='Wrong DNI' #If the DNI is not a valid number, returns "Wrong DNI" string
    return lletra
    
import random #Imports random library
def shuffle(llista):
    for i in range(len(llista)):
        r=int((random.random()*10)%len(llista)) 
        #Calculates a random number between 0 and 1
        #Mutiplies the number by 10 to make it between 0 and 10
        #Picks the remainder to avoid an overflow, so r will be between 0 and len(llista)-1
        llista[i], llista[r]=llista[r],llista[i] #Interchanges the i element with r element
    return llista
    
def otan(text):
    OTKey={'A':'Alpha','B':'Bravo','C':'Charlie','D':'Delta','E':'Epsilon','F':'Foxtrot','G':'Golf','H':'Hotel',
           'I':'India','J':'Juliet',"K":'Kilo', 'L':'Lima','M':'Mike','N':'November','O':'Oscar','P':'Papa',
           'Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango','U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray',
           'Y':'Yankee','Z':'Zulu'}
    #Creates a dictionary letter-name
    textOTAN=''
    for c in text:
        textOTAN+=OTKey[c.upper()]+' ' #Makes the conversion letter to name
    return textOTAN
    
