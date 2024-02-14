"""In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
 with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable
 … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the 
requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your
 program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that
   s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per 
   requirement)."""
import string

def main():
    is_Valid(getPlate())

def getPlate():
    return input('Type the plate in uppercase: ')

def is_Valid(plate):

    print(list(string.ascii_lowercase))
    puncValidation(plate)
    minMaxCharacters(plate)
    minLetras(plate)
    
        

def puncValidation(plate):

    for letter in plate:
        for signos in string.punctuation:
            if signos in letter:
                print("Invalid. It hasn't contain any punctuation sign")
                
            
def minMaxCharacters(plate):
    if len(plate) >=2 or len(plate)<=6:
        print("")
    else:
        print("Invalid. Plate has to contain minimun 2 or maximun 6 characters")
        


def minLetras(plate):

    for characters in plate:
        i = 0
        print(f"i = {i}")
        if i == 0 and type(characters) is not str:
            print("Invalid. First is a letter")
        elif i == 2 and characters is not str():
            print("Invalid. Second is a letter")
        i = i+1


if __name__ == ("__main__"):
    main()