# Part_2 
with open('input.txt') as f:
    list = f.read()
    big_list = set()
    big_list.add('0'+','+'0')
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    for i in range(len(list)):
        if i % 2 == 0:
            if list[i] == '>':
                x1 += 1
            if list[i] == '<':
                x1 += -1
            if list[i] == '^':
                y1 += 1
            if list[i] == 'v':
                y1 += -1
            big_list.add(str(x1)+','+str(y1))
            print(str(x1)+','+str(y1),'SANTA')
        else:
            if list[i] == '>':
                x2 += 1
            if list[i] == '<':
                x2 += -1
            if list[i] == '^':
                y2 += 1
            if list[i] == 'v':
                y2 += -1
            big_list.add(str(x2)+','+str(y2))
            print(str(x2)+','+str(y2),'ROBO')
    housesWithGifts = len(big_list)
    print(housesWithGifts)
with open('output2.txt','w') as h:
    h.write(str(housesWithGifts))
