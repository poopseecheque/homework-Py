a = int(input('Enter 1st value: ')) # changed e to E
b = int(input('Enter 2nd value: ')) # changed e to E

if a + b >= 50:
    print("1st + 2nd =", a + b) 
elif a + b == 30:
    print("1st * 2nd =", a * b) # added the elif statement just to diversify the script a bit
else:
    print("1st - 2nd =", a - b)
