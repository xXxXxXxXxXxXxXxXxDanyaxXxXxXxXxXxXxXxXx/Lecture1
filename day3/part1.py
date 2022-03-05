#Part_1
with open('input.txt') as f:
    list = f.read()
    list2 = []
    x = 0
    y = 0
    for i in range(len(list)):
        if list[i] == '>':
            x += 1
        if list[i] == '<':
            x += -1
        if list[i] == '^':
            y += 1
        if list[i] == 'v':
            y += -1
        element = str(x) + str(y)
        print(element)
        if list2.count(element) == 0:
            list2.append(element)
    housesWithGifts = len(list2) + 1
with open('output1.txt','w') as h:
    h.write(str(housesWithGifts))
