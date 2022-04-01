# Part_2
with open('input.txt') as f:
    sequence = f.read()
    count = 0 
    while count < 50:
        instances = 1
        sequence_new = ''
        for i in range(len(sequence)-1):
            if sequence[i] == sequence[i+1]:
                instances += 1
            else:
                sequence_new = sequence_new + str(instances)
                sequence_new = sequence_new + str(sequence[i])
                instances = 1
        if sequence[i] != sequence[i+1]:
            sequence_new = sequence_new + '1'
            sequence_new = sequence_new + str(sequence[i+1])
        else:
            sequence_new = sequence_new + str(instances)
            sequence_new = sequence_new + str(sequence[i])
        count += 1
        sequence = sequence_new
with open('output2.txt','w') as h:
    h.write(str(len(sequence)))
