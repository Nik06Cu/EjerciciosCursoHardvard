"""In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
 with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters. (CHECK)”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters. (CHECK)”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable
 … vanity plate; AAA22A would not be acceptable.(CHECK) The first number used cannot be a ‘0’(CHECK).”
“No periods, spaces, or punctuation marks are allowed.(CHECK)”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the 
requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your
 program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that
   s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per 
   requirement)."""

import string

def main():
    validez = is_Valid(getPlate())
    if validez ==True:
        print("Valid")
    else:
        print("Invalid")

def getPlate():
    return input('Type the plate in uppercase: ')

def is_Valid(plate):
    var1 = list() # Declaración de las variables que reciben el retorno de las funciones correspondientes
    var2 = list()
    var3 = list()
    var4 = list()

    var1 = puncValidation(plate)
    #print(var1[0])
    print(var1[1])

    var2 = minMaxCharacters(plate)
    #print(var2[0])
    print(var2[1])

    var3 = minLetras(plate)
    #print(var3[0])
    print(var3[1])


    var4 = middlePlate(plate)
    #print(var4[0])
    print(var4[1])
    
    if var1[0] == True and var2[0] == True and  var3[0] == True and  var4[0] == True:  
        return True
    else: 
        return False

def puncValidation(plate):

    error = 0
    retorno = list()
    for letter in plate:
        for signos in string.punctuation:
            if signos in letter:
                 
                 error = 1
                 break

    if error == 1:
        bolean = False
        mensaje = "Invalid. It hasn't contain any punctuation sign"
        
    else:
        bolean = True
        mensaje = "Ok"

    retorno = [bolean, mensaje]
    return retorno    

            
def minMaxCharacters(plate):
    
    error = 0
    retorno = list()

    if len(plate) >=2 and len(plate)<=6:
        error = 0
    else:
        error = 1
    
    if error == 1:
        retorno = [False,"Invalid. Plate has to contain minimun 2 or maximun 6 characters"]    
    else:
        retorno = [True,"OK"]        
    return retorno

def minLetras(plate):
    error = 0
    retorno = list()

    CLetters = 0
    abc = list(string.ascii_lowercase)#Lista con abecedario
    letras = list()#Lista donde se almacenarán cada caracter del plate
    abcUpper = list()

    for characters in plate:
        letras.append(characters) #Guarda la placa en una lista
        
    for i in abc:
        abcUpper.append(str.upper(i)) #Guarda todo el abecedario en mayúscula

    for i in range(2):
        if letras[i] in abcUpper:
            CLetters = CLetters + 1
    
    if CLetters == 2:
        error = 0
    else:
        error = 1

    if error == 1:

        retorno = [False,"It isn't valid. The plate must start with two letters"]
    else: 
        retorno = [True,"Ok"]

    return retorno
    

def middlePlate(plate):

    placas = list()
    aux = 0
    aux2 = 0
    message = 0
    message2 = 0

    error1 = 0
    error2 = 0
    retorno = list()

    for i in plate: #Permite recorrer la placa guardando los valores de cada indice en la varaible i

        bolean = str.isnumeric(i)#En esta variable se guarda True cuando se encuentra un número en la cadena de caracteres en la placa
        
        if bolean == True: #Si llega a ser un número marca True y entra al if
            aux = 1 #Guarda en este auxiliar que servirá para vericar que una vez se encuentre un número siga siendo así
            aux2 = aux2 + 1 #Ayuda a saber cual es el primer número encontrado para verificar que no sea cero

        if aux == 1 and bolean == False:
            error1 = 1
        
        if aux2 == 1 and i == "0":
            error2 = 1
        

        if error1 == 1:
            retorno = [False,"Plate is wrong. The plate can't content any letters after the numbers."]
            break
        elif error2 == 1:
            retorno = [False,"Plate is wrong. First number must be different to zero."]
            break
        else: 
            retorno = [True,"Ok"]


    return retorno

if __name__ == ("__main__"):
    main()