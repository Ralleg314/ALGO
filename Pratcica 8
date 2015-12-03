def length(llista):
    l=llista.pop() #Deletes the last item
    if not llista:
        return 1
    return length(llista)+1 #Every iteration, adds 1 to counter

def isMember(element,llista):
    if not llista: #If the list is empty, element in not in the list
        return False
    if element==llista.pop(): #Compares the last element with the one we want and removes it from the list
        return True
    return isMember(element,llista)
    
def mergesort(llista): #Implenet mergesort algorithm as in theory class
    if len(llista) < 2:
        return llista
    else:
        middle = len(llista) / 2
        left = mergesort(llista[:middle])
        right = mergesort(llista[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i ,j = 0, 0
    while(i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result += left[i:]
    result += right[j:]
    return result
    
def aprop(a):
    aord=mergesort(a)
    dmin=float('inf') #Sets distance to "infinite"
    for i in range(len(aord)-1):
        d=aord[i+1]-aord[i] #Calculates the distance between elements
        if d<dmin: #If the distance is smaller than the minimal, we get both the distance and the elements
            dmin=d
            mina=aord[i]
            minb=aord[i+1]
    return (mina,minb)
    
def elimina(a):
    #Ordenar
    orda=mergesort(a) #O(nlog(n))
    temp=orda[0]
    sol=[orda[0]]
    for i in orda[1:]: #O(n)--> O(nlogn+n)=O(nlogn)
        if temp!=i: #When the item is different, it means all the equals have been erased
            sol.append(i)
            temp=i
    return sol
    
def max_llista(a):
    if len(a)==1: #Just in case that the original list's lenght is 2
        return a
    if len(a)==2:
        if(a[1]-a[0]>0):#We could use the function 'max', but we will avoid it supposing it doesn't exist
            return a[1]
        else:
            return a[0]
    m=max_llista(a[1:]) #Looks for the max in the remainder list
    if(a[0]-m>0): #Compares the max in between the first element and the maximum of every other element
        return a[0]
    return m
    
from swampy.Gui import *
from math import *
import math 
def fractal(canv,endposx,endposy,ang,l,i):
    if(i==10):
        return canv
    else:
        l/=1.7
        canv.line([[endposx,endposy],[endposx+(l*math.cos(ang+math.pi/4)),
                                          endposy+(l*math.sin(ang+math.pi/4))]],width=5,fill='red')
        #"Positive" line
        canv.line([[endposx,endposy],[endposx+(l*math.cos(ang-math.pi/4)),
                                          endposy+(l*math.sin(ang-math.pi/4))]],width=5,fill='red')
        #"Negative" line
        i+=1
        fractal(canv,endposx+(l*math.cos(ang+math.pi/4)),
        endposy+(l*math.sin(ang+math.pi/4)),ang+math.pi/4,l,i)
        fractal(canv,endposx+(l*math.cos(ang-math.pi/4)),
        endposy+(l*math.sin(ang-math.pi/4)),ang-math.pi/4,l,i)
    return canv

def dibuix():
    g = Gui()
    g.title('Fractals')
    canv = g.ca(width=800, height=800, bg='silver')
    canv.line([[0,-400],[0,-100]],width=5,fill='red')
    endposx=0
    endposy=-100
    l=300
    fractal(canv,endposx,endposy,math.pi/2,l,0)
    g.mainloop()
    
