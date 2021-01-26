def prime_ck2(y):
    is_prime = True
    for n in range(2,y-1):
        if y % n == 0:
            is_prime = False
    if is_prime:
        print("Prime!!!")
    else:
        print("Not Prime!!!")

# def check_prime(x):
#     check = True
#     for i in range(2,x+1):f
#         if x/i == 1:
#             check = False
#     if check:
#         print("Prime")
#     else:
#         print("Not Prime")

# check_point = int(input("Enter any number to check: "))
# check_prime(check_point)

check_point2 = int(input("Enter second to check: "))
prime_ck2(check_point2)