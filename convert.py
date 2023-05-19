
"""Decimal to binary converter and vice versa"""

#Function
def Convert_Decimal_Binary(number):
    #We initialize a list empty that binary number
    binary = []
    #While loop that runs while the number is greater than or equal to 1
    while (number >= 1):
        #Check if the number is divisible by 2
        if number%2==0:
            binary.append(0) #Add a 0 th the list if it's even
            number//=2 #Divide the number by 2 using interger division
        elif number%2!=0:
            number//=2
            binary.append(1)
    #Return the reversed binary list
    return (binary[::-1])

def run():
    #We ask for a number on the screen
    number = int(input("Ingrese un número entero: "))
    #We call the function and pass the number as parameter
    binary = Convert_Decimal_Binary(number)
    print(f"{binary} es el número en Binario de {number}")

if __name__ == "__main__":
    run()

