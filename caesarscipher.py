



message=input("Enter your message\n")                                                 #Takes input message from user

key=int(input("Enter Cipher Key\n"))                                                  #The super secret cipher key

mode=input("encrypt or decrypt\n")                                                    #We can set mode to encrypt or decrypt




Symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$_-+="  #The set of symbols we will be using in our
                                                                                  #code
                                                                                  
                                                                                  
                                                                                  

translated=""                                                                    #Stores the translated message


for symbol in message:                                                          '''The Ceaser working:- It takes one single character at a
                                                                                time from the entered message and checks whether it is 
                                                                                in the Symbols list. If true, it finds the index of 
                                                                                that symbol in the Symbols index, adds or subtracts 
                                                                                the key value depending on encrypt or decrypt mode and
                                                                                returns the translatedIndex and the character at 
                                                                                translated Index gets appended where we want 
                                                                                to store the appended message.
                                                                                If flase, it does nothing and the symbol gets appended to 
                                                                                the former. '''
                                                                                
                                                                                
    if symbol in Symbols:
        symbolIndex=Symbols.find(symbol)
        if mode=='encrypt':
            translatedIndex=symbolIndex+key
        elif mode=='decrypt':
            translatedIndex=symbolIndex-key



        if translatedIndex>=len(Symbols):
            translatedIndex=translatedIndex-len(Symbols)
        elif translatedIndex<0:
            translatedIndex=translatedIndex+len(Symbols)


        translated=translated+Symbols[translatedIndex]

    else:
        translated=translated+symbol

print(translated)                                                    #The translated message is printed on the console
