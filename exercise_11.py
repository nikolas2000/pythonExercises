#That's a function that returns the number of sos found in a table (SOS GAME).
def lst(sos_Table):
    #At first, check if the dimensions of the table are correct.
    if(check_Dimensions(sos_Table)!=None):
        return check_Dimensions(sos_Table)+"\n"+"The dimensions of the table are invalid."
    else:
        #calculates the number of sos per direction:
        horizontal_sos = horizontal_Check(sos_Table)
        vertical_sos = vertical_Check(sos_Table)
        right_diag_sos = right_diag_check(sos_Table)
        left_diag_sos = left_diag_check(sos_Table)
        # total number of sos:
        total_found_sos = horizontal_sos + vertical_sos + right_diag_sos + left_diag_sos
        return "Number of sos found: " + str(total_found_sos)

#returns how many sos exist horizontally
def horizontal_Check(sos_Table):
    sos_found=0
    for row in sos_Table:
        for i in range(0,len(row)-2):
            if((row[i]+row[i+1]+row[i+2])=="sos"):
                sos_found+=1
    return sos_found

#returns how many sos exist vertically
def vertical_Check(sos_Table):
    sos_found=0
    for j in range(0,len(sos_Table)-2):
        for i in range(0,len(sos_Table[j])):
            if((sos_Table[j][i]+sos_Table[j+1][i]+sos_Table[j+2][i])=="sos"):
                sos_found+=1
    return sos_found

#returns how many sos exist if you search diagonally from left to right.
def right_diag_check(sos_Table):
    sos_found = 0
    for j in range(0, len(sos_Table) - 2):
        for i in range(0, len(sos_Table[j])-2): #It starts from left and goes right.
            if ((sos_Table[j][i] + sos_Table[j + 1][i+1] + sos_Table[j + 2][i+2]) == "sos"):
                sos_found += 1
    return sos_found

#returns how many sos exist if you search diagonally from right to left.
def left_diag_check(sos_Table):
    sos_found = 0
    for j in range(0, len(sos_Table) - 2):
        for i in range(len(sos_Table[j])-1, 1, -1): #It starts from right and goes left.
            if ((sos_Table[j][i] + sos_Table[j + 1][i-1] + sos_Table[j + 2][i-2]) == "sos"):
                sos_found += 1
    return sos_found

#Checks if the table is empty and if the rows have the same length.
def check_Dimensions(sos_Table):
    if len(sos_Table)==0:
        return "The table must contain at least one row."
    else:
        row_size=len(sos_Table[0]) #That's the length of the first row. All the rows must have the same length!
        for row in sos_Table:
            if len(row)!=row_size:
                return "All rows' length must be the same."
"""
print(lst([
     ["s","o","s","s","s","s"],
     ["s","o","o","s","o","s"],
     ["s","s","s","s","o","s"],
     ["s","s","o","s","o","s"],
     ["s","s","s","s","o","s"]]))
"""

