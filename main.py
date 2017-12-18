from pathlib import Path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def err_msg(text):
    '''
    Prints input text with red color
    :param text:
    :return:
    '''
    print(bcolors.FAIL, text, bcolors.ENDC)

def cd(curr_dir, dir_name=''):
    '''
    :param curr_dir: Path object of directory from which 'cd' was called \n
    :param dir_name: Str name of the path user want to go into \n
    :return: if dir_name is empty then Path.home(), if dir_name is valid then Path of curr_dir/dir_name otherwise curr_dir
    '''

    if not dir_name: return Path.home()

    new_dir = curr_dir/dir_name

    if not new_dir.exists():
        err_msg('Path "{}" doesn\'t exist'.format(new_dir))
    elif not new_dir.is_dir():
        err_msg('"{}" is not a directory'.format(new_dir))
    else:
        curr_dir = new_dir
    return curr_dir.resolve()

def pwd(curr_dir):
    '''
    Prints working directory
    :param curr_dir:
    '''

    print(str(curr_dir))

def mkdir(curr_dir, dir_name):
    '''
     Makes a directory with name "dir_name" in curr_dir
    :param curr_dir:
    :param dir_name:
    '''

    new_dir = curr_dir/dir_name
    try:
        Path.mkdir(new_dir)
    except FileExistsError:
        err_msg('Directory "{}" already exists'.format(str(new_dir)))

def ls(curr_dir):
    '''
    Lists all files and directories in a given directory
    :param curr_dir:
    :return:
    '''

    for f in curr_dir.iterdir():
        if f.is_dir():
            print(bcolors.OKBLUE, f.parts[-1:][0], bcolors.ENDC)
        else:
            print(f.parts[-1:][0])

def touch(curr_dir, file_name):
    '''
    Create new file at curr_dir with file_name
    :param curr_dir:
    :param file_name:
    '''
    new_file = curr_dir/file_name
    open(str(new_file), 'w')

def cat(curr_dir, file_name):
    '''
    Opens and outputs file with file_name from curr_dir
    :param curr_dir:
    :param file_name:
    '''
    new_file = curr_dir/file_name
    if not new_file.exists():
        err_msg('File "{}" doesn\'t exist'.format(str(new_file)))
    elif not new_file.is_file():
        err_msg('{} is not a file'.format(str(new_file)))
    else:
        with new_file.open() as f:
            print(f.readline(), end='')

def main():
    curr_dir = Path.home().resolve()
    while True:
        command = input('current_dir:{}$ '.format(curr_dir))
        command = command.split()

        if len(command) < 1: continue
        if command[0] == 'cd':
            if len(command) == 2:
                curr_dir = cd(curr_dir, command[1])
            elif len(command) == 1:
                curr_dir = cd(curr_dir)
            else:
                err_msg('Wrong number of arguments')

        elif command[0] == 'pwd':
            if not len(command) == 1:
                err_msg('pwd command doesn\'t have arguments')
            else:
                pwd(curr_dir)

        elif command[0] == 'mkdir':
            if not len(command) == 2:
                err_msg('Wrong number of arguments')
            else:
                mkdir(curr_dir, command[1])

        elif command[0] == 'ls':
            if not len(command) == 1:
                err_msg('ls command doesn\'t have arguments')
            else:
                ls(curr_dir)

        elif command[0] == 'touch':
            if not len(command) == 2:
                err_msg('Wrong number of arguments')
            else:
                touch(curr_dir, command[1])

        elif command[0] == 'cat':
            if not len(command) == 2:
                err_msg('Wrong number of arguments')
            else:
                cat(curr_dir, command[1])
        else:
            err_msg('Unknown command "{}"'.format(command[0]))

if __name__ == '__main__':
    main()