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

    inputs = [1,-5,4]   
    print(formatpoly(inputs)) 
        
    
