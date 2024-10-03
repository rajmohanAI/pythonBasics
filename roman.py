#print("Convert Roman Values to Integer")

def romantoInt(roman, finalNumber):
    romanList = []
    single = "I"
    fours = "V"
    tens = "X"
    for char in roman:

        if(char == single and finalNumber < 3):
            finalNumber = finalNumber + 1
            romanList.append(1)
            
            #print(romanList)
           
    return finalNumber

while True:
    roman = input("Enter the Roman Value")
    if len(roman) < 4 and roman.isupper():
        print(f"Valid Input: {roman}")
        break
    else:
        print("Invalid User Input. Please enter a Valid Roman Value between 1 and 10")

finalNumber = 0
result = romantoInt(roman, finalNumber)
print(result)


    