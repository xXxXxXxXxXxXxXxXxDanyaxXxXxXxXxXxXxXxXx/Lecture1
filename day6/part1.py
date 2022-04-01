#Part_1 
with open('input.txt') as f:
    list = f.readlines()
    on = set()
    for i in range(len(list)):
        line = list[i]
        data = line.split()
        if data[0] == 'turn':
            element = data[2].replace(',',' ').split()
            element_2 = data[4].replace(',',' ').split()
            for i in range(len(element)):
                # element.insert(i,int(element[i]))
                # del element[i+1]
                element[i] = int(element[i])
                # element_2.insert(i,int(element_2[i]))
                # del element_2[i+1]
                element_2[i] = int(element_2[i])
            if data[1] == 'on':
                for y in range(element_2[1]-element[1] + 1):
                    for x in range(element_2[0]-element[0] + 1):
                        if (element[0]+x,element[1]+y) not in on:
                            on.add((element[0]+x,element[1]+y))
                            #print((element[0]+x,element[1]+y))
            else:
                for y in range(element_2[1]-element[1] + 1):
                    for x in range(element_2[0]-element[0] + 1):
                        on.discard((element[0]+x,element[1]+y))
                            
        else:
            element = data[1].replace(',',' ').split()
            element_2 = data[3].replace(',',' ').split()
            for i in range(len(element)):
                # element.insert(i,int(element[i]))
                # del element[i+1]
                element[i] = int(element[i])
                # element_2.insert(i,int(element_2[i]))
                # del element_2[i+1]
                element_2[i] = int(element_2[i])
            for y in range(element_2[1]-element[1] + 1):
                    for x in range(element_2[0]-element[0] + 1):
                        if (element[0]+x,element[1]+y) not in on:
                            on.add((element[0]+x,element[1]+y))
                        else:
                            on.discard((element[0]+x,element[1]+y))
print(len(on))
with open('output1.txt','w') as h:
    h.write(str(len(on)))
