def primeFactors(num):
    i = 2
    output = ""
    if num < 1:
        print("Error! Please enter a number greater than 1")

    else:
        while num % 2 == 0:
            output += "2*"
            num /= 2
        
        for i in range(3,int(num**0.5)+1,2):
            while (num % i == 0):
                output += str(i)+ "*"
                num /= i
        
        if num > 2:
            output += str(int(num))
        
        print(output)

primeFactors(int(input("Enter a number greater than 1: ")))
primeFactors(int(input("Enter a number greater than 1: ")))
primeFactors(int(input("Enter a number greater than 1: ")))
