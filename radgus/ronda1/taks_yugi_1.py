''' Write a function that determines if a string has all unique characters '''

def uniqueCharacters(string):
    result = True
    strArray= []

    for caracter in string:
        if caracter in strArray:
            result = False
            break
        else:
            strArray.append(caracter)
          
    return result


if __name__ == '__main__':
    String = 'sdf231456%&$'
    Unique = uniqueCharacters(String) 
    print(Unique)
