#3 BUGS #SYNTAX BUGS
def isPhoneNumber(text): # function needed a colon
    if len(text) != 12: 
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-': #exclamation point for is equal
            return False
        for i in range(4,7): 
            if not text[i].isdecimal():
                return False
        if text[7] != '-': #hyphen in index 7
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True
        
print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi')) 