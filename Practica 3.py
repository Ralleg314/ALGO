import string
def acro(frase):
    acronim=''
    for l in string.split(frase): #Splits the string
        acronim+=l[0] #Picks the first letter and writes it in the new variable
    return acronim.upper() #Capitalizes all the letters

def paraules(frase):
    recompte=len(string.split(frase)) #Splits the string in order to count every component
    return recompte
    
def cesar(clau,text):
    textxifrat=""
    for c in text:
        if((ord(c)>64 and ord(c)<91)or(ord(c)>96 and ord(c)<123)): #Tests if the character is a letter
            flag=0 #Flag to see if it is capital or not
            if(ord(c)>96 and ord(c)<123): #In case the letter is lowercase, sets flag to "True" and turns it into capital
                flag=1
                c=c.upper() #This will make the program shorter
            if(clau>0): #Depending of the value of "clau", the algorythm will be different
                if(ord(c)+clau>90): #In this case, the letter starts being a character (like *,+,~, etc.)
                    ovfl=ord(c)+clau-90 #Calculates how much the sum "overflows" from letters
                    if(flag==0): #Tests if the letter was capital or not
                        textxifrat+=chr(64+ovfl) #Makes "cesar" from the beginning using the value that "overflowed" before
                    else:
                        textxifrat+=chr(64+ovfl+32) #Will be equivalent the cas 96+ovfl
                else:
                    if(flag==0):
                        textxifrat+=chr(ord(c)+clau) #If we sum "clau" and the letter remains as a letter, we sum values
                    else:
                        textxifrat+=chr(ord(c)+clau+32)
            if(clau<0): #If "clau" is negative, the algorythm remains almost the same, but changing values
                if(ord(c)+clau<65):
                    ovfl=65-ord(c)+clau
                    if(flag==0):
                        textxifrat+=chr(91+ovfl)
                    else:
                        textxifrat+=chr(91+ovfl+32)
                else:
                    if(flag==0):
                        textxifrat+=chr(ord(c)+clau)
                    else:
                        textxifrat+=chr(ord(c)+clau+32)
                #If clau=0, text will be the same, so we don't consider this case
        else: #If the character is not a letter, it remains the same
            textxifrat+=c
    return textxifrat #Returns the ciphered text
    
    
def lyrics(fitxer):
    f = open(fitxer,"r")
    text = f.readlines() #Opens the file and copies it into text variable
    f.close() #File will no longer be used, so we close it
    for line in text:
        print line, #Prints line per line
    print
    
    
def lyrics2(fitxerin):
    fin=open(fitxerin, "r")
    fout=open("lletra_cesar.txt","w")
    for l in fin.readlines(): #Picks a line per cicle
        fout.write(cesar(5,l)) #Transforms the file line per line
    fout=open("lletra_cesar.txt","r")
    print fout.read()
    fin.close()
    fout.close() #Closes the files
    
def sequencia(file):
    f=open("lletra.txt", "r")
    fr=f.read()
    vegadesmin=fr.count('th')
    vegadesmay=fr.count('Th') #We look for both cases
    vegades=vegadesmin+vegadesmay #Sum both cases
    return vegades
    
def paraula(file, paraulabuscar):
    f=open(file, 'r')
    fr=f.read()
    l=len(paraulabuscar) #Mesures the length of the word 
    flag=0
    i=1
    for c in fr:
        if (paraulabuscar[0]==c): #Test if the first letter is the same
            if (fr[i:i+l-1]==paraulabuscar[1:]and (ord(text[i+l])>96 and ord(text[i+l])<123)): #Test if the following characters are the same
                #If the next character is a letter, they're not the same word
                flag+=1 #Word is the same, then we add one
        i+=1 #Next character
    return flag
