LENGTH = 9

def solve(matrix):
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if not is_power_of_two(cell):
                continue

            # traverse row
            for i in range(LENGTH):
                if i == x:
                    continue
                
                matrix[y][i] &= bit_not(cell)

            # traverse column
            for j in range(LENGTH):
                if j == y:
                    continue

                matrix[j][x] &= bit_not(cell)

            # traverse square
            for dy in range(3):
                for dx in range(3):
                    j = y // 3 * 3 + dy
                    i = x // 3 * 3 + dx
                    
                    if j == y and i == x:
                        continue
                    
                    matrix[j][i] &= bit_not(cell)

    return matrix

def is_power_of_two(number):
    if number < 1:
        raise Exception
    return (number & (number - 1)) == 0

def bit_not(number):
    return (1 << 9) - 1 - number

matrix = [[0,9,1,0,0,5,3,0,0],
          [6,0,0,3,1,9,4,0,0],
          [0,3,0,0,0,7,0,9,1],
          #-----------------#
          [0,0,9,4,2,3,1,6,8],
          [3,4,6,8,7,1,2,5,9],
          [8,1,2,9,5,6,7,4,3],
          #-----------------#
          [9,8,0,1,0,0,0,3,0],
          [0,0,3,5,9,0,0,0,2],
          [0,0,5,7,3,0,9,0,0]]

def from_human_readable(matrix):
    result = []
    
    for y, row in enumerate(matrix):
        new_row = []
        
        for x, number in enumerate(row):
            if number == 0:
                coded_value = 0x1ff
            else:
                coded_value = 1 << (number - 1)
                
            new_row.append(coded_value)

        result.append(new_row)

    return result

def to_human_readable(matrix):
    for y, row in enumerate(matrix):
        for i in range(3):
            for x, cell in enumerate(row):
                for j in range(i * 3, i * 3 + 3):
                    #print(row, i, cell, j)
                    number = 1 << j

                    if cell & number:
                        print(j + 1, end=" ")
                    else:
                        print(end="  ")

                if x % 3 == 2:
                    print(end="\\")
                else:
                    print(end="|")
                    
            print()
            
        if y % 3 == 2:
            print("=" * (27 * 2 + 9))
        else:
            print("-" * (27 * 2 + 9))

converted_matrix = from_human_readable(matrix)
solved_matrix = solve(converted_matrix)

to_human_readable(solved_matrix)
    
