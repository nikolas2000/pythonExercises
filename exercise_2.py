#That function shifts every letter of the input to 13 Ascii places. If shift 13 is bigger than z or Z, it starts again
#from a or A.
def ROT13(word):
    newWord=""
    for i in word:
        if((ord("a")<=ord(i)<=ord("z")) and ord(i)+13>ord("z")): #if the shift is bigger than z
            dif_from_z=ord("z")-ord(i) #Finds the Ascii difference from z
            new_start=13-dif_from_z #Finds how many shifts it will be moved from a
            newWord += chr(ord("a")-1 + new_start) #-1 because i want the "a" to be included.
        elif ((ord("A") <= ord(i) <= ord("Z")) and ord(i)+13>ord("Z")):#if the shift is bigger than Z
            dif_from_Z = ord("Z") - ord(i) #Finds the Ascii difference from Z
            new_start = 13 - dif_from_Z #Finds how many shifts it will be moved from A
            newWord += chr(ord("A")-1 + new_start) #-1 because i want the "A" to be included.
        else:
            newWord += chr(ord(i) + 13)
    return newWord

#print(ROT13("CaTz")) #PnGm
