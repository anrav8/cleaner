import os, os.path, shutil
outF = open('myOutFile.txt', 'w')
rmvfile = 'remove.txt'
if os.path.exists(rmvfile) and os.path.isfile(rmvfile):
    path = input("Please enter the path to root directory to start with clean-up:\n")
    with open(rmvfile) as (fp):
        line = fp.readline()
        cnt = 1
        while line:
            if os.path.exists(path+line.strip()):
                if os.path.isfile(path+line.strip()):
                    os.remove(path+line.strip())
                    print('File ', line.strip(), ' has been removed')
                if os.path.isdir(path+line.strip()):
                    shutil.rmtree(path+line.strip())
                    print('Directory ', line.strip(), ' has been removed')
            else:
                print(line.strip(), ' does not exist in your cleaner utility directory')
            line = fp.readline()
            cnt += 1
