#Part_2
with open('input.txt') as f:
    list = f.readlines()
    good_str = 0
    for i in range(len(list)):
        str_ = list[i]
        dublicates = 0
        element = 0
        for i in range(len(str_) - 1):
            atribut = str_.count(str_[i]+str_[i+1])
            if atribut >= 2:
                dublicates += 1
        for i in range(len(str_) - 2):
            atribut_2 = str_.count(str_[i+1]+str_[i+2])
            if atribut_2 >= 2:
                dublicates += 1
        for i in range(len(str_) - 2):
            if str_[i] == str_[i+2]:
                element += 1
        if dublicates != 0 and element !=0:
            good_str += 1
    print(good_str)
with open('output2.txt','w') as h:
    h.write(str(good_str))
