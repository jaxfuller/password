#Jackson Fuller
#1/25/2023
#Password Program
#Checks to make sure user entered password as 8 characters, 1 Upper, 1 Lower, and 1 Digit.
#Then asks for password confirmation

#imports pwinput which censors characters as your typing your password
import pwinput

#defines first function: which checks to make sure the password meets the requirements
def passChecker(str):
    
    #defines and sets all variables to default
    passwordLength = 0
    passwordUpper = 0
    passwordLower = 0
    passwordDigit = 0
    followsRules = False
    
    #finds length of password and saves it under passwordLength Variable
    passwordLength = len(str)
    
    #For loop that cycles through the password
    for i in str:
        if(i.islower()):
            #if it detects lowercase, ups the count by 1
            passwordLower = passwordLower + 1
        elif(i.isupper()):
            #if it detects uppercase, ups the count by 1
            passwordUpper = passwordUpper + 1
        elif(i.isdigit()):
            #if it detects a digit, ups the count by 1
            passwordDigit = passwordDigit + 1
   
    #if/elif statements that check to make sure the password meets requirements             
    if passwordLength < 8:
        print("Please enter more than 8 characters.")
        followsRules = False
    elif passwordLower < 1:
        print("Please use 1 or more lower case letters.")
        followsRules = False
    elif passwordUpper < 1:
        print("Please use 1 or more upper case letters.")
        followsRules = False
    elif passwordDigit < 1:
        print("Please use 1 or more digits.")
        followsRules = False
    else:
        followsRules = True
        
    #returns a boolean    
    return followsRules

#define second function, which confirms password
def passConfirm(confirm,password):
    
    #defines variable and sets it to default
    confirmPassword = False 
    
    #if/else that makes sure the confirmation inputted matches orginal password
    if confirm == password:
        confirmPassword = True
        print("Confirmation Complete.")
    else:
        print("Incorrect Password. Try again.")
    
    #returns a boolean
    return confirmPassword
    
    
#Defines main function    
def main():
    #defines variable and sets it to default
    followsRules = False
    
    #introduction
    print()
    print("Enter your password. Required: 8 Characters, 1 Upper, 1 Lower, and 1 Digit.")
    
    
    #while loop for entering password
    while followsRules == False:
        print()
        #user input here:
        password = str(pwinput.pwinput())
        print()
        #Calls on the passChecker function and stores the return in the followsRules Variable
        followsRules = passChecker(password)
        #if it returns true, the while loop is broken

    #defines variable and sets it to default
    confirmPassword = False
    
    #confirmation introduction       
    print("Please confirm your password:")
    print()
    
    #while loop for confirming password
    while confirmPassword == False:
        print()
        #user input for confirmation
        confirm = str(pwinput.pwinput())
        print()
        #Calls on the passConfirm function which checks to make sure they match
        confirmPassword = passConfirm(confirm,password)
        #Loop breaks if function returns true
        
    print("Congratulations. You have created your password.")
        
if __name__ == "__main__":
    main()