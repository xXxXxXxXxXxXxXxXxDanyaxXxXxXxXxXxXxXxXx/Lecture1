#Part2
with open('input.txt') as f:
    list = f.readlines()
    AllLength = 0
    for i in range(len(list)):
        list2 = list[i].split('x')
        l = int(list2[0])
        w = int(list2[1])
        h = int(list2[2])
        list3 = []
        list3.append(l)
        list3.append(w)
        list3.append(h)
        if list3[0] < list3[1]:
            if list3[1] < list3[2]:
                min1 = list3[0]
                min2 = list3[1]
            else:
                min1 =list3[0]
                min2 = list3[2]
        else:
            if list3[0] < list3[2]:
                min1 = list3[0]
                min2 = list3[1]
            else:
                min1 = list3[1]
                min2 = list3[2]

        atribut = l * w * h + 2 * (min1 + min2)
        AllLength += atribut
print(AllLength)
with open('output2.txt','w') as h:
    h.write(str(AllLength))
