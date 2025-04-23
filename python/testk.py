# """
# #Write a Python program that takes an integer as input and prints whether it is even or odd.
# num=int(input("Enter the value: "))
# if num%2==0:
#     print(num,"is an even number")
# else:
#     print(num,"is not prime number")"""

# # num=65432178
# # temp=num
# # length=0
# # position=5
# # while num>0:
# #     num=num//10
# #     length+=1
# # if length>=position:
# #     while temp>0:
# #         digit=temp%10
# #         temp=temp//10
# #         if length==position:
# #             print(digit)
# #             break
# #         length-=1
# # else:
# #     print("no answer")

# num=8247358258
# temp=num
# dig=8
# count=0 #3
# digits=[]
# digit1=0
# length=0 #10
# # while num>0:
# #     digit=num%10 #8,2,4,7,3,5,8,2,5,8
# #     length+=1 #1,2,3,4,5,6,7,8,9,10
# #     if digit==dig:
# #         count+=1
# #     num=num//10 #824735825
# #     length-=1
# # print(count)
# while temp>0:
#     digit1=temp%10
#     if digit1==dig:
#         digits.append(digit1)
#         length-=1

#     else:
#         pass
    
# print(digits)

# # print(count)

# # while temp>0:
# #     req_digit=temp%10
# #     if req_digit==dig:
def check_digit_in_number(number, digit):
    count = 0
    positions = []
    position = 1  # To track the position of the digits in the number (starting from 1)

    # Loop through each digit of the number
    while number > 0:
        current_digit = number % 10  # Get the last digit
        if current_digit == digit:
            count += 1
            positions.append(position)
        number //= 10  # Remove the last digit
        position += 1

    # If count is greater than 0, print the results
    if count > 0:
        print(f"The digit {digit} is present {count} times at positions: {positions[::-1]}")
    else:
        print(f"The digit {digit} is not present in the number.")

# Example usage:
number = 123456789  # A 9-digit number
digit = 3  # The digit you want to check
check_digit_in_number(number, digit)


    