# # name="UdayaSree"
# # name=name.lower()
# # vowel_count=0
# # consonent_count=0
# # vowels="aeiou"
# # for i in range(0,len(name)):
# #     if name[i]=="a" or name[i]=="e" or name[i]=="i" or name[i]=="o" or name[i]=="u":
# #         vowel_count+=1
# #     else:
# #         consonent_count+=1
# # print( vowel_count, consonent_count)


# num=123456789
# fact=0
# while num!=0:
#     digit=num%10
#     for i in range(1,digit+1):
#         if digit%i==0:
#             fact+=1
#     if fact==2:
        
#         print(digit,end=" ")
#     num=num//10


# Given number
# number = 123456789

# # Initialize the prime digits
# prime_digits = [2, 3, 5, 7]
# result = 0
# place_value = 1  # To maintain place value when forming the number

# # Loop through each digit in the number
# while number > 0:
#     digit = number % 10  # Get the last digit
#     if digit in prime_digits:  # Check if the digit is prime
#         result += digit * place_value  # Add it to the result
#         place_value *= 10  # Move to the next place value
#     number = number // 10  # Remove the last digit

# Print the result
# print(result)
number=12335245678957
while number!=0:
    digit=number%10
    count=0
    for i in range(1,digit+1,1):
        if digit%i==0:
            count+=1
    if count==2:
            print(digit)
    number=number//10






