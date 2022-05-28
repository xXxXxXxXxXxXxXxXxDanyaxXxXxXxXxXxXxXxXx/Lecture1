with open('input.txt') as f:
    data = f.readlines()
    position = 0
    vector = 3
    movement = [[[0,1,2,3],[0,4,2,5],[0,3,2,1],[0,5,2,4]],
                [[1,2,3,0],[1,4,3,5],[1,0,3,2],[1,5,3,4]],
                [[2,4,0,5],[2,5,0,4],[2,1,0,3],[2,3,0,1]],
                [[3,2,1,0],[3,0,1,2],[3,4,1,5],[3,5,1,4]],
                [[4,1,5,3],[4,3,5,1],[4,0,5,2],[4,2,5,0]],
                [[5,2,4,0],[5,0,4,2],[5,1,4,3],[5,3,4,1]]] # матрица позиций 
                
    orientation = [[1,4,3,5],[2,4,0,5],[3,4,1,5],[5,0,4,2],[1,2,3,0],[1,0,3,2]] # матрица связанная с параметрами вектора 
    for i in range(len(data)):
        local_data = data[i] 
        local_data = local_data.split() # сплитим 
        if local_data[0] == 'FORWARD':
            for i in range(len(movement[position])):
                if movement[position][i][3] == vector: # определяем нужный элемент матрицы
                    atribut = i
                    break
            circle = movement[position][atribut] 
            for i in range(int(local_data[1])):
                circle = [circle[1],circle[2],circle[3],circle[0]] # переопределяем позицию
                position = circle[0]
                vector = circle[3] # инициализация для следующей итерации

        elif local_data[0] == 'RIGHT':
            parametr = 0
            for j in range(len(orientation[position]) - 1): # определение нужного элемента в матрице позиций
                if orientation[position][j] == vector:
                    vector = orientation[position][j+1] # выявление нового вектора
                    parametr += 1
            if parametr == 0:
                vector = orientation[position][0]
        
        elif local_data[0] == 'LEFT': # аналогично тому что было выше
            parametr = 0
            for i in range(1,len(orientation[position])):
                if orientation[position][i] == vector:
                    vector = orientation[position][i-1]
                    parametr += 1 
            if parametr == 0:
                vector = orientation[position][3]
        else:
            break 
with open('output.txt','w') as h: 
    h.write(str(position))
