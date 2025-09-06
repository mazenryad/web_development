FILEPATH = 'test.txt'


def read_file(filepath=FILEPATH) :

    """reads the file and stores the content in todo list"""
    
    with open(filepath , 'r' ) as file :
         todo = file.readlines()

    return todo 


def write_file(filepath , todo):

    """writes in the file the new list"""

    with open(filepath , 'w') as file :
            file.writelines(todo)


if __name__ == '__main__' :
                         # useful for testing the functions as it doesn't run in my main code
     print(read_file())
