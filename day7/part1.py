#Part 1
with open('input.txt') as f:
    list = f.readlines()
    dictionary = {}
    print('длинна = ',len(list))
    while list:
        
        del_elements = []
        
        for i in range(len(list)):
            line = list[i]
            data = line.split()

            if len(data) == 3 and data[0].isdigit():
                dictionary[data[2]] = data[0]
                del_elements.append(list[i])
                
            elif len(data) == 4 and data[1] in dictionary:
                dictionary[data[3]] = ~ data[1]
                del_elements.append(list[i])
                
            else: # len(data) == 5:
                if data[1] == 'AND' and data[0] in dictionary and data[2] in dictionary:
                    dictionary[data[4]] = data[0] & data[2]
                elif data == 'OR' and data[0] in dictionary and data[2] in dictionary:
                    dictionary[data[4]] = data[0] | data[2]
                elif data == 'RSHIFT' and data[0 in dictionary and data[2] in dictionary:
                    dictionary[data[4]] = data[0] >> data[2]
                else:
                    dictionary[data[4]] = data[0] << data[2]
                del_elements.append(list[i])
                                               
        for i in del_elements:
            list.remove(i)
