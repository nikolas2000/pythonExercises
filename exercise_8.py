#That's a function that converts an integer in (0,1.000.000) to a latin/roman number.
def latin(n):
    #Must: n>0 and n<1.000.000
    if n<=0 or n>=1000000:
        return "The integer must be bigger than zero and less than 1 million."
    #That's a dictionary with the latin characters of the integers that cannot been calculated,
    #Those values are taken from this site: https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php
    latinNumbers_dict =\
        {
            1:"I",
            #4:"IV", The comments are the key-values that will be added and calculated with a different way than the other numbers out of that dictionary.
            5:"V",
            #9:"IX",
            10:"X",
            #40:"XL",
            50:"L",
            #90:"XC",
            100:"C",
            #400:"CD",
            500:"D",
            #900:"CM",
            1000:"M", # M or _I
            #4000: "__IV",
            5000:"_V",
            #9000: "__IX",
            10000:"_X",
            #40000: "__XL",
            50000:"_L",
            #90000: "__XC",
            100000:"_C",
            #400000: "__CD",
            500000:"_D",
            900000: "__CM"
        }

    latin_number=""
    listOfNumbers = list(latinNumbers_dict.keys()) #I put all the keys into a list.
    # I call the function calculateNumbersStartWith_4_or_9 to return the new listOfNumbers.
    listOfNumbers = calculateNumbersStartWith_4_or_9(latinNumbers_dict,listOfNumbers)

    index = len(listOfNumbers)-1

    while n>0:
        if(n-listOfNumbers[index]>=0): #finds the first smaller number (we work from the last to the first element).
            latin_number+=latinNumbers_dict[listOfNumbers[index]]
            n-=listOfNumbers[index]
        else:
            index-= 1

    return latin_number


#That function calculates the latin numbers
#of the integers that start with 4 or 9 and have only zeros after them (4,9,40,90,400,e.t.c).
#Those numbers' symbols are the difference between the right symbol and the left one.
def calculateNumbersStartWith_4_or_9(latinNumbers_dict,listOfAllNumbers):
    numbersList = [4,9,40,90,400,900,4000,9000,40000,90000,400000]
    latin_number = ""
    index = len(listOfAllNumbers) - 1

    for number in range (0,len(numbersList)):
        while numbersList[number] > 0:

            if (numbersList[number] - listOfAllNumbers[index] >= 0):
                index += 1
                if numbersList[number] >= 4000:
                    latin_number += "__"  # Perispomenes
                #Now the latin number is the difference between the right and the left symbol.
                latin_number += latinNumbers_dict[listOfAllNumbers[index] - numbersList[number]][-1] + \
                                latinNumbers_dict[listOfAllNumbers[index]][-1] #we use -1 to take the last element of the string.
                                                                    #It's important because some symbols(>=4000) start with "_" (Perispomenes)
                listOfAllNumbers.append(numbersList[number]) #I add it to the total list and dictionary.
                listOfAllNumbers.sort()
                latinNumbers_dict[numbersList[number]] = latin_number
                break
            else:
                index -= 1
        index = len(listOfAllNumbers) - 1
        latin_number=""
    return listOfAllNumbers

#print(latin(34))
