def find_cube_pairs(target):                                # needs colon for correct function syntax.
    solutions = []                                          # no semicolons in python.
    max_num = round(target ** (1/3))                        # no such thing as 'targ', corrected to target. *** is not exponentiation operator, corrected to **.

    for a in range(1, max_num + 1):                         # no such thing as 'ranges', corrected to range. Added colon for correct for loop syntax.
        for b in range(a, max_num + 1):                     # same fixes as previous line.
            if a**3 + b**3 == target:                       # *** -> **, 'targ' -> target, added semicolon for correct if block syntax.
                solutions.append((a, b))                    # corrected 'sol' to solutions, no such thing as 'sol'. removed semicolon.
    return solutions                                        # corrected 'sol' to solutions, no such thing as 'sol'.

pairs = find_cube_pairs(1729)                               # removed comma, incorrect syntax
print("Valid cube pairs for 1729:")                         # removed comma, incorrect syntax. Changed 'printf' to print. Changed 1728 to 1729.
for a, b in pairs:                                          # changed 'pair' to pairs, no such thing as 'pair'. Added colon for correct for loop syntax.
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")       # changed 'printf' to print. Fixed incorrect exponentiation (was squaring instead of cubing (**2 -> **3)). Changed 1728 to 1729.

"""Submit your response here:  https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u"""
