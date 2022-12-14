#----------------- MATCH CASE STATEMENTS-----------
x=6
match x:
    case 0:
        print(" x is zero")
    case 6 if x == 6:
        print("x is six")
    case _:
        print("numbers are positive")
