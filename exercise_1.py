#Smurf number finder in [a,b]. Examples of Smurf numbers: 89=8^1+9^2 and 135=1^1+3^2+5^3
def gargamel(a,b):
    exists=False
    found_numbers = []
    for i in range (a,b+1): # +1 because we want: [a,b].
        if(showIfSmurf(i)==True):
            exists=True
            found_numbers.append(i)
            #print(i)
    if(exists==True):
        return ("Exists. Found numbers: "+ str(found_numbers))
    else:
        return ("Does not exist.")

#checks if a number is Smurf or not.
def showIfSmurf(number):
    sum = 0
    index = 1
    for i in str(number): # I transform it to string because i want to iterate its digits
        sum+= int(i)** index # I transform it again to integer and exponent with index.
        index+=1
    if(number==sum):
        return True
    else:
        return False

#print(gargamel(2,1000))