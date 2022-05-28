with open('input.txt') as f:
    l = int(f.readline())

    set_ = set()
    bin_ = bin(l)
    l = bin_[2:len(bin_)]

    for i in range(len(l)):
        str_1 = l[:-1]
        str_2 = l[-1:]
        operand = str_2 + str_1
        
        set_.add(int(operand,2))
        
        l = operand 
        max_ = max(set_)
        
with open('output.txt','w') as h:
    h.write(str(max_))
