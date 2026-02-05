decimal = int(input("Enter a decimal number: "))
binary = ""

while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    
 
    temp = ""
    for digit in str(remainder):
        temp += digit
    binary = temp + binary

print("Binary number:", binary)
