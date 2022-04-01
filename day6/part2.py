#Part_2
with open('input.txt') as f:
    list = f.readlines()
    luminosity = []
    for i in range(1000):
        for i in range(1000):
            luminosity_line = []
            luminosity_line.append(0)
        luminosity.append(luminosity_line)
    for i in range(len(list)):
        line = list[i]
        data = line.split()
        if data[0] == 'turn':
            element = data[2].replace(',',' ').split()
            element_2 = data[4].replace(',',' ').split()
            
            for i in range(len(element)):
                element[i] = int(element[i])
                element_2[i] = int(element_2[i])
        
            if data[1] == 'on':
                for y in range(element_2[1]-element[1] + 1):
                    for x in range(element_2[0]-element[0] + 1):
                        luminosity[element[1]+y][element[0]+x] += 1
            else:
                for y in range(element_2[1]-element[1] + 1):
                    for x in range(element_2[0]-element[0] + 1):
                        if luminosity[element[1]+y][element[0]+x] != 0:
                            luminosity[element[1]+y][element[0]+x] += -1
        else:
            element = data[1].replace(',',' ').split()
            element_2 = data[3].replace(',',' ').split()
            for i in range(len(element)):
                element[i] = int(element[i])
                element_2[i] = int(element_2[i])
            for y in range(element_2[1]-element[1] + 1):
                    for x in range(element_2[0]-element[0] + 1):
                        print(len(luminosity[0])
                        luminosity[element[1]+y][element[0]+x] += 2
    luminosity_sum = 0
    for i in range(len(luminosity)):
        luminosity_line = sum(luminosity[i])
        luminosity_sum += luminosity_line

    print(luminosity_sum)
    print(luminosity[999])  
with open('output2.txt','w') as h:
    h.write(str(luminosity_sum))
