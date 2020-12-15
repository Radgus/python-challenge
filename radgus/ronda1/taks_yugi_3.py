
''' Write a function that replaces all spaces in a string with %20 ''' 

def remplace(string1):
    strArray = []

    for caracter in string1:
        if caracter == ' ':
            strArray.append('%20')
        else:
            strArray.append(caracter)

    result = ''.join(strArray)
    return result


if __name__ == '__main__':
    String = 'hola mundo python'
    result = remplace(String) 
    print(result)
