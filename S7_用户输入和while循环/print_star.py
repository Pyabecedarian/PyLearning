"""

*
**
***
****
*****
****
***
**
*

"""

row = 1

while row <= 9:

    if row <= 5:
        col = 1
        while col <= row:
            print("*", end="")
            col += 1
        print()
    else:
        col = 9
        while col > row:
            print("*", end="")
            col -= 1
        print()

    row += 1


"""

    *                
   ***   
  *****
 *******
*********
 *******
  *****
   ***
    *
    
"""

"""
row     1   2   3   4   5   |   6   7   8   9
stars   1   3   5   7   9   |   7   5   3   1 
gap     4   3   2   1   0   |   1   2   3   4 
                                2*gap + stars = 9
                                stars = 9 - 2*gap
"""

row = 1

while row <= 9:
    if row <= 5:

        gap = 5 - row
        while gap > 0:
            print(" ", end="")
            gap -= 1

        star = 2 * row - 1
        while star > 0:
            print("*", end="")
            star -= 1

        print()
    else:

        gap = row - 5
        while gap > 0:
            print(" ", end="")
            gap -= 1

        star = 9 - 2 * (row - 5)
        while star > 0:
            print("*", end="")
            star -= 1
        print()

    row += 1


"""
     ********
    ********
   ********
  ********
 ********
********

"""
"""
row     1   2   3   4   5   6
star    8   8   8   8   8   8 
gap     5   4   3   2   1   0

gap + row = 6
gap = 6 - row
"""

row = 1

while row <= 6:

    gap = 6 - row
    while gap > 0:
        print(" ", end="")
        gap -= 1

    star = 8
    while star > 0:
        print("*", end="")
        star -=1
    print()

    row += 1

"""
     ********
    *      *
   *      *
  *      *
 *      *
********

row     1   2   3   4   5   6
star    8   2   2   2   2   8
gap     5   4   3   2   1   0
    
"""

row = 1
while row <= 6:

    gap = 6 - row
    while gap > 0:
        print(" ", end="")
        gap -= 1

    if row == 1 or row == 6:
        star = 8
        while star > 0:
            print("*", end="")
            star -= 1
        print()
    else:
        star = 2
        c_gap = 8 - star
        while star > 0:
            print("*", end="")
            while c_gap > 0:
                print(" ", end="")
                c_gap -= 1
            star -= 1
        print()

    row += 1
