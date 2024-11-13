x = int(input("Give me a four digit number that is even but does not end with 0"))

if x >= 1000 and x <= 9999 and x % 2 == 0 and x % 10 != 0:
    print("Good job!")
else:
    if x < 1000:
        print("Nope, that's not right! It is too small")
    elif x > 9999:
        print("Nope, that's not right! It is too big")
    elif x % 2 != 0:
        print("Nope, that's not right! It is not even")
    elif x % 10 == 0:
        print("Nope, that's not right! It ends with 0")

quit()