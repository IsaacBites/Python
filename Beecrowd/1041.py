X = float(input())
Y = float(input())

if (X == 0.0 and Y == 0.0):
    print("Origem")
elif (X > 0.0 and Y > 0.0):
    print("Q1")
elif (X < 0.0 and Y < 0.0):
    print("Q3")
elif (X < 0.0 and Y > 0.0):
    print("Q2")
else:
    print("Q4")
