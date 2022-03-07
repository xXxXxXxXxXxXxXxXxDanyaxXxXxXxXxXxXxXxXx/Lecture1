#Part_1
with open('input.txt') as f:
    list = f.read()
    big_list = set()
    x = 0
    y = 0
    big_list.add(str(x)+','+str(y))
    for i in range(len(list)):
        if list[i] == '>':
            x += 1
        if list[i] == '<':
            x += -1
        if list[i] == '^':
            y += 1
        if list[i] == 'v':
            y += -1
        big_list.add(str(x)+','+str(y))
    housesWithGifts = len(big_list)
    print(housesWithGifts)
with open('output1.txt','w') as h:
    h.write(str(housesWithGifts))
