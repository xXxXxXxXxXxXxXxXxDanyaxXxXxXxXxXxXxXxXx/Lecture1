# АоС_1
with open('input.txt') as f:
    up = 0
    down = 0
    for row in f:
        for letter in row:
            if letter == '(':
                up += 1
            if letter == ')':
                down += 1
            if (down - up) == 1:
                with open('output2.txt','w') as h:
                    h.write(str(down + up))
                    break
