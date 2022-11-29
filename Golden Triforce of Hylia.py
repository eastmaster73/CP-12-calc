
## courage (easton)
def superscript(n):
    out = ""
    while(n>0):
        v = n%10
        if(v==1):
            out = "\u00b9" + out
        elif(v==2 or v==3):
            out = chr(ord("\u00b0")+v) + out
        else:
            out = chr(ord("\u2070")+v) + out
        n //= 10
    return out

def mkTerm(deg,coef,lnth):##takes coefficent/degree and makes it into a term
    Term= ""    ## for the coefficent 
    if(deg == lnth -1): ##determines degree by index, not 0,1,2
        Term = str(coef) ##highest index coefficent does not require sign
        if(coef == -1 and deg > 0):
            Term = "-"
        elif(coef == 1 and deg > 0):
            Term= ""
        else:
            Term =str(coef)
    elif(coef == 1 and deg != 0):
        Term = " + "
    elif(coef == -1 and deg != 0):
        Term = " - "
    elif(coef > 0):
        Term = " + "+ str(coef)
    elif(coef < 0):
        Term = " - "+ str(abs(coef))
    elif(deg == 0 and coef > 0 ):
        Term = " + "+ str(coef)
    else:
        Term = " - "+ str(abs(coef))

    if (deg == 0):
        Term += ""
    elif(deg == 1):
        Term += "x"
    else:
        Term += ("x" + str(superscript(deg)))
    return Term 
        
def formatPoly(arr):##takes array and foramts it into a polynomial.
    polynom = ""
    allzero = True ##initalize all zeros to true
    cntdown = len(arr) ##length of array is how many times it runs through
    index = (len(arr) -1) ##initalizing to index of 1st element in array
    num = index

    while (num >= 0):
        arr[num] = round(arr[num],2)
        num -= 1

    while (cntdown > 0): ##runs when not 0, shuts down when cntdown = 0
        coef = arr[index]
        deg = index
        if(coef != 0):
            allzero = False ##if nonzero coef, false, does not print
            polynom += mkTerm(deg,coef,len(arr))  
        cntdown -= 1
        index -= 1
    if(allzero):
        print("0") ##prints 0 if no nonzero coefficent is encountered
    return polynom
##wisdom (Nicola)
import math as m

def solve ( x, arr):
    index = len(arr)- 1
    countdown = len(arr)
    ans = 0
    while (countdown > 0):

        tmp = 0
        deg = index
        coeff = arr(index)
        tmp = coeff(pow(x, deg))
        ans += tmp
        countdown -= 1
        index -= 1

    return ans


def quad (arr):
    if (len(arr) !=3):
        return ("only quadratics")
        a = arr[2]
        b = arr[1]
        c = arr[0]
        tmp = pow((b, 2)-4ac)
        if (tmp < 0):
            return (0)
        elif (tmp == 0):
            return (-b/(2a))
        tmp = m.sqrt(tmp)
        ans1 = (-b + tmp)/(2a)
        ans2 = (-b - tmp)/(2a)
        return ans1, ans2
    if (len(arr) == 2):
        ans = (-(arr[0]))/arr[1]
        return ans
    if (len(arr) == 1):
        if (arr[0] == 0):
            return "INF"
        else:
            return 0

        
##Power (alex)
startY = 15
startX = -8
Points = [(-8,77), (-7,60), (-6,45), (-5,32), (-4,21), (-3,12), (-2,5), (-1,0), (0,-3), (1,-4), (2,-3), (3,0), (4,5), (5,12), (6,21), (7,32), (8,45), (9,60), (10,77), (11,96)]
symbol = "@ "
symbol2 = "# "
Points2 = [(-8,2), (-7,2), (-6,3), (-5,3), (-4,4), (-3,4), (-2,5), (-1,5), (0,6), (1,6), (2,7), (3,7), (4,8), (5,8), (6,9), (7,9), (8,10), (9,10), (10,11), (11,11)]
def maptoindex (arr, startX, startY):
    index = []
    endY = startY - 20
    n = 0
    while (n <= 19):
        if (startY >= arr[n][1] >= endY):
            temp = startY - arr[n][1]
            temp = temp*20
            temp2 = startX - arr[n][0]
            temp2 = 0 + abs(temp2)
            temp = temp + temp2
            index += [temp]
            n += 1
        else:
            n += 1
    index = sorted (index)
    return index


def setupAxis2(startX, startY):
    graph = ["· "]*400
    n = 0
    i = 0
    if (startX <= 0):
        yaxis = abs(startX)
        n = yaxis 
        while (n <= 400):
            if (startY >= 0):
                center = (abs(startX) + startY*20)
            graph [n] = "| "
            n += 20
    if (startY >= 0):
        n = startY*20
        while (i <= 19):
            graph [n] = "- "
            i += 1
            n += 1
    if (center >= 0):
        graph[center] = "+ "
    return graph

def addToGraph (graph, points, symbol):
    pointind = points
    i = len(pointind) - 1
    graph = graph
    
    while (i >= 0):
        n = points [i]
        graph [n] = symbol
        i -= 1
    
    return graph

    
def printgraph (graph):
    graphout = ""
    n = 0
    while ( n < 400):
        if (n % 20 == 0):
            graphout += " \n "
        graphout += graph[n]
        n += 1
    return graphout



points = maptoindex (Points, startX, startY)
points2 = maptoindex (Points2, startX, startY)
graph = setupAxis2(startX, startY)
graphwp = addToGraph (graph, points, symbol)
graphwp2 = addToGraph (graphwp, points2, symbol2)
