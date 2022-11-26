try:
    file = open('sample.txt', 'r')
    print('File found!!!')
    
except IOError:
    print('File not found!!!')