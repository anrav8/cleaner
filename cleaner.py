import os, os.path, shutil
outF = open('Log.txt', 'w')
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
                    print("File", line.strip(), "has been removed")
                    logmsg="File "+line.strip()+" has been removed"
                    outF.write(logmsg)
                if os.path.isdir(path+line.strip()):
                    shutil.rmtree(path+line.strip())
                    print("Directory", line.strip(), "has been removed")
                    logmsg="Directory "+line.strip()+" has been removed"
                    outF.write(logmsg)
            else:
                print(line.strip(), "does not exist in your cleaner utility directory")
                logmsg = line.strip() + " does not exist"
                outF.write(logmsg)
            line = fp.readline()
            cnt += 1
