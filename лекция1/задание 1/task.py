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
    for i in range(10):
        element = f.read(1)
        if element != '\n' and element != '':
            list2.append(element)
    print(list2)
with open('output.txt','w') as h: 
    h.write('100')

# list2 = []
# probel = 1
# while probel < 3:
#     element = f.read(1)
#     if element != '\n' and element != ' ':
#        list2.append(element)
#         probel += -1
#    else:
#         probel += 1
# print(list2)
