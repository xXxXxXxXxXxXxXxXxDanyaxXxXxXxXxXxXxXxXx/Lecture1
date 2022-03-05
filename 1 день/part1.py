# АоС_1
with open('input.txt') as f:
    up = 0
    down = 0
    letter2 = 0
    for row in f:
        for letter in row:
            if letter == '(':
                up += 1
                print(letter,up)
            if letter == ')':
                down += 1
                print(letter,down)
result = up - down
with open('output.txt','w') as h:
    h.write(str(result))
