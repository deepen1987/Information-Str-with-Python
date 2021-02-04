"""
CS521 - A2
Deependrasingh Shekhawat

Script to print FUN.
"""

# Created a list to store "F"
f_out = []
for horizontal in range(5):
    f_in = []
    for vertical in range(7):
        if(vertical == 0 or vertical == 1) or (horizontal == 0 or horizontal == 2):
            f_in.append("F")
        else:
            f_in.append(" ")
    f_out.append(f_in)

# Created a list to store "U"
u_out = []
for horizontal in range(5):
    u_in = []
    for vertical in range(7):
        if (vertical == 0 or vertical == 6) and (horizontal == 0 or horizontal < 3):
            u_in.append("U")
        elif (horizontal == 3) and (vertical == 1 or vertical == 5):
            u_in.append("U")
        elif (horizontal == 4) and (1 < vertical < 5):
            u_in.append("U")
        else:
            u_in.append(" ")
    u_out.append(u_in)

# Created a list to store "N"
n_out = []
for horizontal in range(5):
    n_in = []
    for vertical in range(8):
        if vertical < 2 or vertical > 5:
            n_in.append("N")
        elif horizontal == 1 and vertical == 2:
            n_in.append("N")
        elif horizontal == 2 and vertical == 3:
            n_in.append("N")
        elif horizontal == 3 and vertical == 4:
            n_in.append("N")
        elif horizontal == 4 and vertical == 5:
            n_in.append("N")
        else:
            n_in.append(" ")
    n_out.append(n_in)

# Printing FUN
for horizontal in range(5):
    for vertical in range(7):
        print(f_out[horizontal][vertical], end="")
    print(end=" ")
    for vertical in range(7):
        print(u_out[horizontal][vertical], end="")
    print(end=" ")
    for vertical in range(8):
        print(n_out[horizontal][vertical], end="")
    print()
