import time

def levenshtein_distance(text,line): #We implement levenshtein algorithm as in the theory
    len_text=len(text)
    len_line=len(line)
    if len_text>len_line:
        text,line=line,text
    if len_line==0:
        return len(text)
    distance_matrix=[[0]*len_line for x in range(len_text)]
    for i in range(len_text): distance_matrix[i][0]=2*i
    for i in range(len_line): #Initialices the first line with 0 if the letter is the same and as 1 if they are different
        if text[0]!=line[i]:
            distance_matrix[0][i]=1
    for i in range(1,len_text):
        for j in range(1,len_line):
            deletion=distance_matrix[i-1][j]+2
            insertion=distance_matrix[i][j-1]+2
            substitution=distance_matrix[i-1][j-1]
            if text[i]!=line[j]:
                substitution+=1
            distance_matrix[i][j]=min(insertion,deletion,substitution)
    return min(distance_matrix[-1]) #Returns the minimal distance

def dna():
    with open('HUMAN-DNA.txt','r') as f:
        t0=time.clock() #Sets initial time
        d_min1=float('inf') #Consider the minimal distance as "infinite"
        d_min2=float('inf')
        d_min3=float('inf')
        for l,line in enumerate(f.readlines()): #Enumerate gives us the line we are in and the line itself
            d1=levenshtein_distance('AGATACATTAGACAATAGAGATGTGGTC',line)
            if(d1<d_min1): #If distance is smaller than the minimal distance, we pick the line and the its value
                d_min1=d1
                linia1=l
            d2=levenshtein_distance('GTCAGTCTGGCCTTGCCATTGGTGCCACCA',line)
            if(d2<d_min2):
                d_min2=d2
                linia2=l
            d3=levenshtein_distance('TACCGAGAAGCTGGATTACAGCATGTACCATCAT',line)
            if(d3<d_min3):
                d_min3=d3
                linia3=l
        temps=time.clock()-t0 #Calculates the time in seconds    
        return ([['AGATACATTAGACAATAGAGATGTGGTC',linia1,d_min1],
                ['GTCAGTCTGGCCTTGCCATTGGTGCCACCA',linia2,d_min2],
                ['TACCGAGAAGCTGGATTACAGCATGTACCATCAT',linia3,d_min3]],
                temps)
                


def mod_levenshtein_distance(text,line): #Same algorithm as before, but now it will give us the substring and distance
    len_text=len(text)
    len_line=len(line)
    if len_text>len_line:
        text,line=line,text
    if len_line==0:
        return len(text)
    distance_matrix=[[0]*len_line for x in range(len_text)]
    for i in range(len_text): distance_matrix[i][0]=2*i
    for i in range(len_line):
        if text[0]!=line[i]:
            distance_matrix[0][i]=1
    for i in range(1,len_text):
        for j in range(1,len_line):
            deletion=distance_matrix[i-1][j]+2
            insertion=distance_matrix[i][j-1]+2
            substitution=distance_matrix[i-1][j-1]
            if text[i]!=line[j]:
                substitution+=1
            distance_matrix[i][j]=min(insertion,deletion,substitution)
    dmin=float('inf') #Looks for the first minimal distance and the position
    for i in range(1,len_line):
        if(distance_matrix[-1][i]<dmin):
            l=i
            dmin=distance_matrix[-1][i]
    i=len_text-1 #Starts at the last line of the matrix
    j=l #Starts at the location of the minimal distance
    while(i!=0): #We will go up until we get to the first line
        deletion=distance_matrix[i-1][j]
        insertion=distance_matrix[i][j-1]
        substitution=distance_matrix[i-1][j-1]
        mov_min=min(deletion,insertion,substitution) #Picks the smallest of all 3 cases
        if(mov_min==deletion): #Depending on which one is the smallest, we will go up, left or up-left
            i-=1
        elif(mov_min==insertion):
            j-=1
        elif(mov_min==substitution):
            i-=1
            j-=1
    return (dmin,line[j-1:l+1])#Returns the substring and distance
            

def dna2():
    with open('HUMAN-DNA.txt','r') as f:
        text='GGCCTTGCCATTGG'
        t0=time.clock()
        line=f.readlines() #Opens the file as lines and stores them in a list
        (distancia1,substring1)=mod_levenshtein_distance(text,line[0]) #We can't use a for because variables are different
        (distancia2,substring2)=mod_levenshtein_distance(text,line[1])    
        (distancia3,substring3)=mod_levenshtein_distance(text,line[2])
        (distancia4,substring4)=mod_levenshtein_distance(text,line[3])
        (distancia5,substring5)=mod_levenshtein_distance(text,line[4])
        (distancia6,substring6)=mod_levenshtein_distance(text,line[5])
        (distancia7,substring7)=mod_levenshtein_distance(text,line[6])
        (distancia8,substring8)=mod_levenshtein_distance(text,line[7])
        (distancia9,substring9)=mod_levenshtein_distance(text,line[8])
        (distancia10,substring10)=mod_levenshtein_distance(text,line[9])
        temps=time.clock()-t0    
    return ([[ 1,distancia1,substring1],
              [ 2,distancia2,substring2],
              [ 3,distancia3,substring3],
              [ 4,distancia4,substring4],
              [ 5,distancia5,substring5],
              [ 6,distancia6,substring6],
              [ 7,distancia7,substring7],
              [ 8,distancia8,substring8],
              [ 9,distancia9,substring9],
              [10,distancia10,substring10]],
                temps)
