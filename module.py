print('Imported module')
test = 'test string'

def find_index(to_search,target):
    '''find the index of a value in a sequance'''
    for i, value in enumerate(to_search):
        if value == target :
            return 1

    return -1