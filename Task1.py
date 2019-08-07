S = float(input("Enter S "))
A = float(input("Enter diff "))
D = A**2 + 8 * S
#print (D )
if D < 0:
    print("No solution")
elif D == 0:
     h = -A / 2
     if h <= 0:
         print("No solution")
     else:
         print("h = ", round(h,3))
else:
    h1 = (-A - D**0.5) / 2
    if h1 <= 0:
       print("No solution")
    else:
        print("h = ", round(h1, 3))
    h2 = (-A + D**0.5) / 2
    if h2 <= 0:
        print("No solution")
    else:
        print("h = ", round(h2, 3))