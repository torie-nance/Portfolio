# This program creates a one time use pad by generating random numbers
# and shifting the characters by that many characters

import random

def encode(userInputList):
    
    privateKey = []

    for x in range(len(userInputList)):
            privateKey.append(0)

    for x in range(len(userInputList)):

        #get the ASCII value of the character to make sure it's a letter
        asciiValue = ord(userInputList[x])

        #if the value of the character is a letter, then run the functions
        if (asciiValue >= 65 and asciiValue <= 90) or (asciiValue >= 97 and asciiValue <= 122):
            isLowerRange = randomRange()
            newAsciiValue = determineRange(isLowerRange)

            #replace the character with the character at the new ASCII value
            privateKey[x] = newAsciiValue
            userInputList[x] = (chr(newAsciiValue))
        else:
            privateKey[x] = asciiValue
            userInputList[x] = (chr(asciiValue))
    
    encodedOutput = ""
    for x in userInputList:
        encodedOutput += x
    
    print("Encoded message: " + encodedOutput)

    #turn the private key list into a string list
    keyListToString = map(str, privateKey)
    
    #turn the list into a basic string to be returned and outputted for the user
    stringPrivateKey = ""
    for x in keyListToString:
        stringPrivateKey += (x + " ")
    
    return stringPrivateKey

#determine whether to use the upper or lower range
def randomRange():
   
    isLowerRange = False

    if random.randint(0,9) < 5:
        isLowerRange = True
    elif random.randint(0,9) >= 5:
        isLowerRange = False

    return isLowerRange

def determineRange(isLowerRange):
    
    #if isLowerRange is true then that means use the range from 65 to 90
    if isLowerRange:
        newAsciiValue = random.randint(65,90)
    #if isLowerRange is false then that means use the range from 97 to 122
    elif not isLowerRange:
        newAsciiValue = random.randint(97,122)


    return newAsciiValue




#take user input in char list format
#create function 
    #generate a random number
    #shift the specific character by that many places
    #store the random number in a new list
    #store the new character in a new list
    #generate the new message
#ask user if they want to decode the message
    #use the list with the stored random numbers to decode

#if the new value plus the og value is in range then continue

print("What do you want to encode?:")

#Get the string of what the user wants encoded and turn it into a list
userInputList = list(input())
privateKey = encode(userInputList)

print("Would you like to view the private key? Y/N:")

answer = input()
if answer == "Y":
    print("What is the password?:")
    password = input()

    if password == "NopeWasRobbedAtTheOSCARS":
        print("The private key is: " + privateKey)
    else:
        print("Access Denied!")
else:
    print("Have a great day!")