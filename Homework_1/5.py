x = float(input("Vvedite x"))
y = float(input("Vvedite y"))

if x > 0 and y > 0:
    print("1 ch")
elif x < 0 and y > 0:
    print("2 ch")
elif x < 0 and y < 0:
    print("3 ch")
elif x > 0 and y < 0:
    print("4 ch")
else:
    print("Na osi")
