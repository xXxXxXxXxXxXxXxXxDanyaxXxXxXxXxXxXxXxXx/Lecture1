#Part 1
with open ('input.txt') as f:
    list_ = f.readlines()
    bit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B','C', 'D', 'E', 'F']
    code_ = 0
    memory_ = 0
    
    for i in range(len(list_)):
        line = list_[i]
        line = line.strip()
        local_memory = 0
        atribut = -2
        for i in range(1,len(line) - 1):
            #print(line[i])
            
            if line[i] == '\\' and line[i+1] == '"':
                atribut = -2
            
            elif line[i] == '\\' and line[i+1] == '\\': 
                atribut += 1
                if atribut % 2 == 0 and atribut != -2: 
                    c = 1
                    local_memory += c
                    
            elif i < len(line) - 4 and line[i] == '\\' and line[i+1] == 'x' and line[i+2] in bit and line[i+3] in bit:
                local_memory -= 2
                atribut = -2

            else:
                local_memory += 1
                atribut = -2
            print(line[i] , 'и' , line[i+1] , local_memory)
                
        memory_ += local_memory
        code_ += len(line)
        print(line)
        print(local_memory,len(line))
    print('память =',memory_, 'код =',code_, 'разница =',code_ - memory_)

with open('output2.txt', 'w') as h:
    h.write(str(code_ - memory_))
