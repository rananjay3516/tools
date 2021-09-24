theBoard = {'top-L':' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L':' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L':' ', 'low-M': ' ', 'low-R': ' ',}

theBoard['mid-M'] = 'X'

def printBoard(b):
    
    print(' '+ b['top-L'] + ' | ' + b['top-M'] + ' | ' + b['top-R'] + ' | ')
    print('------------')
    print(' '+ b['mid-L'] + ' | ' + b['mid-M'] + ' | ' + b['mid-R'] + ' | ')
    print('------------')
    print(' '+ b['low-L'] + ' | ' + b['low-M'] + ' | ' + b['low-R'] + ' | ')
    

printBoard(theBoard)
