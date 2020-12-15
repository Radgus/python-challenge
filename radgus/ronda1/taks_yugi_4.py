
''' There are 3 edits that you can perform in a string, add a character, remove a character and replace a character. Make a function that given two strings determines if they are exactly one edit away. ''' 

def oneEdit(string1, string2):
    result = True
    s1Len = len(string1)
    s2Len = len(String2)
    subs = abs( s1Len - s2Len)

    if subs > 1:
        result = False
        return result 
    
    def comp(stringLess, stringMore):
        string1 = stringLess
        string2 = stringMore
        for caracter in string1:
            if caracter in string2:
                string2 = string2.replace(caracter, '', 1)
        
        print(len(string2))
        if len(string2) > 1:
            return False
        else:
            return True


    if s1Len <= s2Len:
        result = comp(string1, string2)
    else:
        result = comp(string2, string1)
    
    return result


if __name__ == '__main__':
    ''' ¿ are they exactly one edit away ? '''
    String1 = 'sdf23&4s6%wwpo'
    String2 = 'sdf23&4s6%wwp'
    result = oneEdit(String1, String2) 
    print(result)
