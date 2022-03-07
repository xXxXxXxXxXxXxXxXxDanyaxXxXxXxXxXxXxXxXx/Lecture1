#Part_1
with open('input.txt') as f:
    list = f.read()
    big_list = []
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
        list_mini = []
        list_mini.append(x)
        list_mini.append(y)
        if big_list.count(list_mini) == 0:
            big_list.append(list_mini)
    housesWithGifts = len(big_list) + 1
with open('output1.txt','w') as h:
    h.write(str(housesWithGifts))
