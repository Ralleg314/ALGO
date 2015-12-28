def mult(a,b):
    if(a>b):#a has to be the lowest always (It'll only work the first time if b is bigger. After that, a will be the lowest allways)
        a,b=b,a
    if a==1: #If the lowest number is 1, returns b
        return b
    if a==2: #If it's 2, sums 2 times the biggest
        return b+b
    return mult(a-1,b)+b #Decreases the a by one and sums b, as a multiplication would be if made by sums
"""
Cost of the function
a=1\
b=2|-->1>log(1)/log(2)=0-->O(n^d)=O(n)
d=1/
"""

print mult(3,15)
print mult(2,17)

#Exercici 2
def mergesort(llista): #Implement sorting function (mergesort)
    if len(llista)==1:
        return llista
    mid=len(llista)/2
    right=mergesort(llista[mid:])
    left=mergesort(llista[:mid])
    return merge(left,right)

def merge(left,right):
    ll=len(left)
    lr=len(right)
    il=0
    ir=0
    sol=[]
    while il<ll and ir<lr:
        if left[il]<right[ir]:
            sol.append(left[il])
            il+=1
        else:
            sol.append(right[ir])
            ir+=1
    if il==ll:
        sol+=right[ir:]
    else:
        sol+=left[il:]
    return sol


def paresimpares(llista):
    par=[]
    impar=[]
    llistaord=mergesort(llista[:])#Sort list: O(nlogn)
    for i in llistaord:#O(n)
        if i%2==0:
            par.append(i) #Adds even numbers
        else:
            impar.append(i) #Adds odd numbers      
    return par+impar #Returns a list with both

#Cost de la funcio: O(n+nlogn)=O(nlogn)
"""
a=[-54,-36,-4,20,30,40,56,78,3]
print paresimpares(a)

a=[-54,-37,-4,10,21,30,40,56,78,1123]
print paresimpares(a)
"""

#Exercici 3
def lev_distance(first,second): #Implement Leveshtein algorithm as in theory
    if len(first)>len(second):
        first,second=second,first
    if len(second)==0:
        return len(first)
    lf=len(first)+1
    ls=len(second)+1
    distance_matrix=[[0]*ls for x in range(lf)]
    for i in range(lf):distance_matrix[i][0]=i
    for j in range(ls):distance_matrix[0][j]=j
    for i in range(1,lf):
        for j in range(1,ls):
            deletion=distance_matrix[i-1][j]+1
            insertion=distance_matrix[i][j-1]+1
            substitution=distance_matrix[i-1][j-1]
            if first[i-1]!=second[j-1]:
                substitution+=1
            distance_matrix[i][j]=min(deletion,insertion,substitution)
    return distance_matrix
       
def distancianuevo(lista,listb):
    dm=lev_distance(lista,listb) #Returns a matrix with all distances
    for i in range(len(lista)):
        dmin=dm[i+1][i+1]
        if dm[i+1][i]==dmin: #The only one with the same distance can only be the one in the left, as the top one and top-left will be dettected
			     #in the iteration before
            print lista[:i+1],"->",listb[:i],"(",dmin,")" #If it's the case, prints it
        print lista[:i+1],"->",listb[:i+1],"(",dmin,")" #The distance in the diagonal will always be the minimal, so we print it.
        print "-------------"

"""
distancianuevo("kitten","sitting")    
"""
