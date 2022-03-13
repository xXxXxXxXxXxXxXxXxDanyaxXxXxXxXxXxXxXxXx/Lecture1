#Part_1 
with open('input.txt') as f:
    list = f.readlines()
    Vowel = ['a', 'e', 'i', 'o', 'u']
    exeption = ['ab', 'cd', 'pq', 'xy']
    good_str = 0
    for i in range(len(list)):
        str_ = list[i]
        Vowel_count = 0
        dublicates = 0
        exeption_count = 0
        for j in range(len(str_)):
            if str_[j] in Vowel:
                Vowel_count += 1
        if Vowel_count >= 3:
            for j in range(len(str_) - 1):
                if str_[j] == str_[j+1]:
                    dublicates += 1
            if dublicates != 0:
                for j in range(len(str_) - 1):
                    if str_[j] + str_[j+1] in exeption:
                        exeption_count += 1
                if exeption_count == 0:
                    good_str += 1
    print(good_str)
with open('output1.txt','w') as h:
    h.write(str(good_str))
