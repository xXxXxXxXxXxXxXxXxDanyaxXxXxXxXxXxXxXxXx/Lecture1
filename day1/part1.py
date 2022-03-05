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
result = up - down
with open('output.txt','w') as h:
    h.write(str(result))
