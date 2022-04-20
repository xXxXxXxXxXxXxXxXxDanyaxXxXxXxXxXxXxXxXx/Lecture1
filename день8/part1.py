#Part 1
with open ('input.txt') as f:
    list_ = f.readlines()
    bit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B','C', 'D', 'E', 'F']
    code_ = 0
    memory_ = 0
    
    for i in range(len(list_)):
        line = list_[i]
        line = line
        local_memory = 0
        i = 0
        while i < len(line) - 2:
            
            if line[i] == '\\' and line[i+1] == '"':
                i += 2
                local_memory += 1

            elif line[i] == '\\' and line[i+1] == '\\': 
                i += 2
                local_memory += 1

            elif i < len(line) - 4 and line[i] == '\\' and line[i+1] == 'x' and line[i+2] in bit and line[i+3] in bit:
                i += 4
                local_memory += 1

            else:
                i += 1
                local_memory += 1
                
        memory_ += local_memory
        code_ += len(line)

with open('output1.txt', 'w') as h:
    h.write(str(code_ - memory_))
