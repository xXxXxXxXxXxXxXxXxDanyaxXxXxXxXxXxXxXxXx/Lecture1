#Part 2
with open ('input.txt') as f:
    list_ = f.readlines()
    bit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B','C', 'D', 'E', 'F']
    code_ = 0
    new_code = 0
    
    for i in range(len(list_)):
        line = list_[i]
        line = line.strip()
        local_memory = 0
        i = 0
        local_code = 4
        while i < len(line):
            if line[i] == '\\':
                i += 1
                local_code += 2

            elif line[i] == '"' and i != 0 and i != len(line) - 1: 
                i += 1
                local_code += 2
                
            else:
                i += 1
                local_code += 1
                
        code_ += len(line)
        new_code += local_code
        print(line , len(line), local_code )
        
with open('output2.txt', 'w') as h:
    h.write(str(new_code - code_))
