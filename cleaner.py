import os.path
import read
import shutil
from _datetime import datetime

def cleanup():
    i = 0
    while i <= len(tormv) - 1:
        line = tormv[i]
        if len(line.strip()) != 0:
            if os.path.exists(path + line.strip()):
                if os.path.isfile(path + line.strip()):
                    os.remove(path + line.strip())
                    print("File ", line.strip(), "has been removed")
                    logmsg = "File " + line.strip() + " has been removed\n"
                    outF.write(logmsg)
                if os.path.isdir(path + line.strip()):
                    files = os.listdir(path + line.strip())
                    if len(files) == 0:
                        os.rmdir(path + line.strip())
                        print("Directory", line.strip(), "has been removed")
                        logmsg = "Directory " + line.strip() + " has been removed\n"
                        outF.write(logmsg)
                    else:
                        askmsg = "Directory " + path + line.strip() + " is not empty. Please confirm removal of directory along with entire subtree (Y/N) "
                        flag = False
                        while flag is not True:
                            confirm = input(askmsg)
                            if confirm in ["Y", "y"]:
                                shutil.rmtree(path + line.strip())
                                print("Directory", line.strip(), "has been removed")
                                logmsg = "Directory " + line.strip() + " has been removed\n"
                                outF.write(logmsg)
                                flag = True
                            if confirm in ["N", "n"]:
                                print("Directory", line.strip(), "has not been removed (User denial)")
                                logmsg = "Directory " + line.strip() + " has not been removed (User denial)\n"
                                outF.write(logmsg)
                                flag = True
                            if confirm not in ["N", "n", "Y", "y"]:
                                print("Invalid input")
            else:
                print(line.strip(), " does not exist")
                logmsg = line.strip() + " does not exist\n"
                outF.write(logmsg)
        i += 1

logname = "Log" + datetime.now().strftime('%m%d%Y%H%M%S') + ".txt"
outF = open(logname, 'w+')
path = input("Please enter the path to directory to start with clean up:\n")
logmsg = "Cleaning up directory " + path + ":\n"
outF.write(logmsg)

name = input("Please enter the name of your what_to_remove list:\n")
if os.path.exists(name):
    tormv = read.excelread(name)
    cleanup()
else:
    print(name, " does not exist")





