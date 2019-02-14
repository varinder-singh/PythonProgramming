# basically  explains using nonlocal vs global keyword
import os


def list_directory(s):
    def dir_list(directory):
        nonlocal tab_stop
        files = os.listdir(directory)
        for f in files:
            current_dir = os.path.join(directory, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory" + f)
                tab_stop = tab_stop + 1
                dir_list(current_dir)
                tab_stop = tab_stop - 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of {} ".format(s))
        dir_list(s)
    else:
        print("There is no {} directory present".format(s))


list_directory('/home/varinder/Desktop/MapReducePD')
