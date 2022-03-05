# Lecture_1
with open('input.txt') as f:
    # формирование list1
    N = int(f.read(1))
    print(N)
    list1 = []
    for i in range(2*N):
        element = f.read(1)
        if i % 2 != 0:
            list1.append(element)
    print(list1)
    
    # формирование list2
    list2 = []
    atribut = 2
    while atribut < 3:
        letter = f.read(1)
        if letter != '/n' and letter != '':
            list2.append(letter)
            atribut += -1
        else:
            atribut += 1
    print(list2)
    
    # сравнение и формирование ответа в list3
    list3 = []
    for i in range(len(list2)):
        atribut = 0
        for j in range(len(list1)):
            if list2[i] == list1[j]:
                atribut += 1
                list3.append(j)
        if atribut == 0:
            list3.append(str(-1))
    print(list3)
    
    # запись ответа в файл
        
with open('output.txt','w') as g:
    for i in range(len(list3)):
        g.write(str(list3[i])+'\n')
