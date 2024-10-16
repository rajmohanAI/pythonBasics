def palindromeCheck(givenvalue):

    givenvalue = givenvalue.replace(" ", "").lower()

    length = len(givenvalue)

    for i in range(length // 2):
       
        print(givenvalue[i])
        print(givenvalue[length - i - 1])
        if givenvalue[i] != givenvalue[length - i - 1]:
            return False 

    return True  

givenvalue = input("Enter a number or a word or a phrase to check if thats a Palindrome...!")

result = palindromeCheck(givenvalue)

print(result)