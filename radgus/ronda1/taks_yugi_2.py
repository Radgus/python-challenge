
''' Write a function that given two strings determines if one is a permutation of the other ''' 

def permutation(string1, string2 ):
    result = True
    
    if len(string1) != len(string2):
        result = False
        return result

    for caracter in string1:
        if caracter not in string2:
            result = False
            break
        else: 
            string2 = string2.replace(caracter, '', 1)
          
    return result


if __name__ == '__main__':
    ''' ¿ Is String1 a permutation of String2 ? '''
    String1 = 'sdf23&4s6%k&'
    String2 = 'sdf23&4s6%k&'
    result = permutation(String1, String2) 
    print(result)
