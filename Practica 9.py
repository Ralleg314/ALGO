def func1d(n):
    import math
    return n * math.sin(10*math.pi*n) + 1.0


def frange1d(start,end,inc):
    i=start
    while i<=end:
        yield (i,func1d(i))
        i+=inc


def search1d():
    import time
    t0=time.clock()
    m=[0,-float('inf')]
    for i in frange1d(-1.0, 2.0, 0.01):
        if i[1]>m[1]:
            m=i
    print m, time.clock()-t0,'s'
    
    t0=time.clock()
    max=[0,-float('inf')]
    for i in frange1d(-1.0, 2.0, 0.0001):
        if i[1]>m[1]:
            m=i
    print m, time.clock()-t0,'s'
    
    t0=time.clock()
    m=[0,-float('inf')]
    for i in frange1d(-1.0, 2.0, 0.000001):
        if i[1]>m[1]:
            m=i
    print m, time.clock()-t0,'s'


from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-6, 6, 0.25)
Y = np.arange(-6, 6, 0.25)
X, Y = np.meshgrid(X, Y)
Z = 200 - (X**2 + Y -11)**2 - (X+Y**2-7)**2

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.hot)


show()



def func2d(X,Y):
    import math
    return 200 - (X**2 + Y -11)**2 - (X+Y**2-7)**2


def frange2d(start,end, inc):
    i=start
    while i<=end:
        j=start
        while j<=end:
            yield (i,j,func2d(i,j))
            j+=inc
        i+=1

def search2d():
    import time
    t0=time.clock()
    m=[0,0,-float('inf')] #This will return only the first max it finds. If we wanted all of them, we would have to 
                          #make another search with abs(m-i)<tol, where tol is a small value like 10^(-5).
    for i in frange2d(-6.0, 6.0, 0.01):
            if i[2]>m[2]:
                m=i
    print m, time.clock()-t0,'s'

    t0=time.clock()
    m=[0,0,-float('inf')]
    for i in frange2d(-6.0, 6.0, 0.0001):
            if i[2]>m[2]:
                m=i
    print m, time.clock()-t0,'s'
    
    t0=time.clock()
    m=[0,0,-float('inf')]
    for i in frange2d(-6.0, 6.0, 0.000015):
            if i[2]>m[2]:
                m=i
    print m, time.clock()-t0,'s'




Punt = complex
Ciutat  = Punt

def X(punt): 
    "La coordenada X d'un punt"
    return punt.real

def Y(punt): 
    "La coordenada Y d'un punt"
    return punt.imag

def Crear_ciutat(lat,long):
    return Ciutat(-48 * float(long),69 * float(lat))


def distancia(a, b): 
    return abs(a - b)


import csv
def lectura0():
    with open('ciutats_USA.csv', 'rb') as fp:
        text=fp.read()
    text2=text.strip().splitlines()
    csvreader=csv.reader(text2,delimiter=' ',skipinitialspace=True)
    for row in csvreader:
        print ', '.join(row)



import csv
def lectura():
    diccionari={}
    with open('ciutats_USA.csv', 'rb') as fp:
        text=fp.read()
    text2=text.strip().splitlines()
    csvreader=csv.reader(text2,delimiter=' ',skipinitialspace=True)
    for row in csvreader:
        diccionari[row[0]]=Crear_ciutat(row[1],row[2])
    return diccionari


from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib inline')

def plot_diccionari(diccionari, style='bo-'):
    '''
    Prenem com entrada un diccionari amb clau el nom de la ciutat i valor les seves coordenades,
    per a graficar, ens calen només les coordenades (els valors del diccionari)
    '''
    plt.plot(map(X, diccionari.values()), map(Y, diccionari.values()), style)
    plt.axis('scaled'); plt.axis('off') #fa que l'àrea de representació sigui proporcional 
                                        #i que no dibuixi els eixos
def plot_linies_ciutats(ciutats, style='bo-'):
    '''
    Prenem com entrada el nom de les ciutats,
    per a graficar, ens calen les coordenades que trobem als valors del diccionari (ciutat:coordenades),
    accedim mitjançant el nom de la ciutat
    '''
    punts = [diccionari[c] for c in ciutats]
    plt.plot(map(X, punts), map(Y, punts), style)
    plt.axis('scaled'); plt.axis('off') #fa que l'àrea de representació sigui proporcional 
                                        #i que no dibuixi els eixos
def plot_recorregut(recorregut): 
    '''
    Mostrem un recorregut com un cicle. 
    Per a fer-ho, afegim al tour la primera ciutat al final, 
    de forma que sempre tornem al principi del recorregut.
    '''
    recorregut.append(recorregut[0])
    plot_linies_ciutats(recorregut)



import random
def generar_poblacio(n, ciutats, rnd_seed):
    random.seed(rnd_seed) #fixem la llavor
    poblacio=[]
    rec=list(ciutats)
    i=0
    while i<n:
        random.shuffle(rec)
        poblacio.append(rec[:])
        i+=1
    return poblacio


def distancia_total(o_gene):
    '''
    Aquesta funció retorna el cost d'un gen (un recorregut)
    '''
    visitades = []
    cost = 0
    gene = o_gene[:]
    gene.append(gene[0]) # tanquem el cicle
    for i in range(len(gene)-1):
        if gene[i] in visitades:
            cost += 10000
        else:
            if gene[i] != gene[i+1]: # verifiquem si la darrera ciutat es repeteix
                cost += distancia(diccionari[gene[i]], diccionari[gene[i+1]])
            visitades.append(gene[i])
    if gene[-2] != gene[-1]: # verifiquem si la darrera ciutat es repeteix
        cost += distancia(diccionari[gene[-2]], diccionari[gene[-1]])
    return cost


def mergesort(llista): #Implement mergesort algorithm as in theory class
    if len(llista)==2:
        return llista
    else:
        middle = len(llista) / 2
        if middle%2==0:
            left = mergesort(llista[:middle])
            right = mergesort(llista[middle:])
            return merge(left, right)
        else:    
            left = mergesort(llista[:middle+1])
            right = mergesort(llista[middle+1:])
            return merge(left, right)

def merge(left, right):
    result = []
    i ,j = 0, 0
    while(i < len(left)-1 and j < len(right)-1):
        if (left[i+1] <= right[j+1]):
            result.append(left[i])
            result.append(left[i+1])
            i = i + 2
        else:
            result.append(right[j])
            result.append(right[j+1])
            j = j + 2
    result += left[i:]
    result += right[j:]
    return result

def probabilitat_seleccio(poblacio,p):
    d=[]
    for i,x in enumerate (poblacio):
        d.append(i)
        d.append(distancia_total(x))
    sd=mergesort(d)
    sumr=1
    prob=[]
    for i in (sd[0::2]):
        prob.append(i)
        prob.append(sumr*p)
        sumr=(1-sumr*p)
    probabilitat=dict(zip(prob[0::2],prob[1::2]))
    return probabilitat


def ordenar_probabilitat(probabilitat):
    return sorted(probabilitat.items(),key=lambda x:x[1], reverse=True)
    
def seleccionar_pare(probabilitat_ordenada, poblacio):
    valor_ruleta = random.random() # nombre aleatori
    probabilitat_acumulada = 0
    idx = 0
    # mentres no assolim el valor de la ruleta o sortim de la llista
    while idx < len(probabilitat_ordenada)-1 and probabilitat_acumulada < valor_ruleta: 
        probabilitat_acumulada += probabilitat_ordenada[idx][1] # acumulem la probabilitat
        idx += 1
    #retornem el darrer element (el que correspon amb el nombre aleatori)
    return poblacio[probabilitat_ordenada[idx][0]] 


def generar_descendencia(g1, g2):
    '''
    Aquesta funció creua dos gens g1 i g2 i retorna dos fills
    El creuament es fa dividint cadascuna de les llistes i barrejant-les
    Aquest algorisme pot generar camins no hamiltonians, que seran penalitzats 
    per la funció distancia_total(gene).
    '''
    split = random.randint(0,len(g1)) # seleccionem un pivot aleatori
    fill_1 = g1[:split]+g2[split:] # el primer descendent és la primera combinació
    fill_2 = g2[:split]+g1[split:] # el segon descendent és la segona combinació
    return fill_1, fill_2 # retornem la descendència


def generar_fills(poblacio,probabilitat,percent_descendencia):
   fills = [] # aquesta llista ha de contenir percent_descendencia*len(poblacio) elements
   probabilitat_ordenada=ordenar_probabilitat(probabilitat)
   for i in range(int(percent_descendencia*len(poblacio)/2)):
       pare1=seleccionar_pare(probabilitat_ordenada,poblacio)
       pare2=seleccionar_pare(probabilitat_ordenada,poblacio)
       while pare1==pare2:
           pare2=seleccionar_pare(probabilitat_ordenada,poblacio)
       fill=generar_descendencia(pare1,pare2)
       fills.append(fill[0])
       fills.append(fill[1])
   return fills


def regenerar(poblacio,fills,probabilitat_ordenada,percent_elit,percent_descendencia):
    no_elit=probabilitat_ordenada[int(percent_elit*len(probabilitat_ordenada)):]      #aqui guardarem les probabilitats que no queden incloses a l'elit
    random.shuffle(no_elit)
    mor=no_elit[:int(percent_descendencia*len(poblacio))]
    poblacio_mor=[]
    for i in mor:
        poblacio_mor.append(poblacio[i[0]])
    #aqui guardarem la població que no pertanyera a la següent generacio
    for i in poblacio_mor: 
            poblacio.remove(i)
    #intercanviar la poblacio_mor pels fills
    for i in fills:
        poblacio.append(i)
    return poblacio

def mutar(gene, beta):
    '''
    Aquesta funció muta aleatoriament les ciutats d'un tour.
    El que farem per assegurar-nos que els resultats son hamiltonians 
    és intercanviar dues posicions
    '''
    for i in range(len(gene)): # per cada ciutat
        if random.random() <= beta: # amb probabilitat beta
            pos = random.randint(0,len(gene)-1) # seleccionem una segona posició
            gene[i], gene[pos] = gene[pos], gene[i] # les intercanviem
    return gene



