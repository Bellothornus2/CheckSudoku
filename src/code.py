def check_sudoku(sudoku):
    #para saber si es una lista
    assert isinstance(sudoku, list)
    result = len(sudoku[0])
    #para saber si es cuadrada
    for i in sudoku:
        if result == len(i):
            result = len(i)
        else:
            return False
    dictionary_keys = list(range(1,len(sudoku)+1))
    dictionary = dict.fromkeys(dictionary_keys,0)
    acumulator = 0
    for i in range(len(sudoku)**2):
        sudoku_index = int(i/len(sudoku))
        value = sudoku[sudoku_index][acumulator]
        if isinstance(value, int) == False or value not in dictionary_keys:
            return False
        dictionary[sudoku[sudoku_index][acumulator]] += 1
        acumulator += 1
        if acumulator == len(sudoku):
            acumulator = 0
    for x in dictionary:
        if dictionary[x] > len(sudoku):
            return False
    return True
    
