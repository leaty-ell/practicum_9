def palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

for mileage in range(100000, 1000000):
    condition1 = palindrome(mileage % 100000)       
    condition2 = palindrome((mileage + 1) % 100000) 
    condition3 = palindrome((mileage + 2) % 10000)  
    condition4 = palindrome(mileage + 3)           

    if condition1 and condition2 and condition3 and condition4:
        print(mileage)
        break  
