import os

def write_authorized_keys():
    with open('authorized_keys_vinuni', 'w') as f:
        dirs = os.listdir('/home/vinuni/.ssh/user/')
        for dirn in dirs:
            path = os.path.join('/home/vinuni/.ssh/user/', dirn, 'authorized_keys')
            print(path)
            if os.path.isfile(path):
                f.write(open(path).read())

if __name__ == '__main__':
    write_authorized_keys()