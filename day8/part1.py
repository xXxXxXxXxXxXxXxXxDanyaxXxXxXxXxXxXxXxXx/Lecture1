#Part 1
with open ('input.txt') as f:
    list_ = f.readlines()
    bit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    code_ = 0
    memory_ = 0
    
    for i in range(len(list_)):
        line = list_[i]
        local_memory = 0
        for i in range(1,len(line) - 2):
            #print(line[i])
            local_memory += 1
            if line[i] == '\\' and (line[i+1] == '\\' or line[i+1] == '"'):
                #print('True')
                local_memory -= 1
            elif i < len(line) - 4 and line[i] == '\\' and line[i+1] == 'x' and line[i+2] in bit and line[i+3] in bit:
                local_memory -= 3
        memory_ += local_memory
        code_ += len(line) - 1
        print(line)
        print(local_memory,len(line) - 1)
    print('память =',memory_, 'код =',code_, 'разница =',code_ - memory_)
