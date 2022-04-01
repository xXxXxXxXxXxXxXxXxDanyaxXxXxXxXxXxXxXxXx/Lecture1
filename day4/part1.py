#Part_1
from hashlib import md5
with open('input.txt') as f:
    key = f.readline()
    search = False
    iteration = 0
    while search == False:
        key_2 = key + str(iteration)
        hash_ = md5(key_2.encode()).hexdigest()
        count_zero = 0
        for i in range(5):
            if hash_[i] == '0':
                count_zero += 1
            else:
                break
        if count_zero == 5:
            search = True
            break
        else:
            iteration += 1
with open('output1.txt','w') as h:
    h.write(str(iteration))
