import face_detector as fd


def register(name):
    """ register new persons """
    img = fd.detect('crop', name=name)

def login():
    """ login the person """
    img = fd.detect('check')

if __name__ == "__main__":
    option = input('Register or Login [R|L]: ')
    
    if option == 'R':
        name = input('enter your name: ')
        if name:
            register(name)
    
    elif option == 'L':
        login()
