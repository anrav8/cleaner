import os, os.path, shutil
outF = open('Log.txt', 'w')
rmvfile = 'remove.txt'
if os.path.exists(rmvfile) and os.path.isfile(rmvfile):
    path = input("Please enter the path to root directory to start with clean-up:\n")
    with open(rmvfile) as (fp):
        line = fp.readline()
        cnt = 1
        while line:
            if len(line.strip()) != 0:
                if os.path.exists(path + line.strip()):
                    if os.path.isfile(path + line.strip()):
                        os.remove(path + line.strip())
                        print("File", line.strip(), "has been removed")
                        logmsg = "File " + line.strip() + " has been removed\n"
                        outF.write(logmsg)
                    if os.path.isdir(path + line.strip()):
                        files=os.listdir(path+line.strip())
                        if len(files)==0:
                            os.rmdir(path + line.strip())
                            print("Directory", line.strip(), "has been removed")
                            logmsg = "Directory " + line.strip() + " has been removed\n"
                            outF.write(logmsg)
                        else:
                            askmsg = "Directory" + path + line.strip() + "is not empty. Please confirm removal of directory along with entire subtree (Y/N) "
                            flag=0
                            while flag < 1:
                                confirm = input(askmsg)
                                if confirm == "Y" or confirm == "y":
                                    shutil.rmtree(path + line.strip())
                                    print("Directory", line.strip(), "has been removed")
                                    logmsg = "Directory " + line.strip() + " has been removed\n"
                                    outF.write(logmsg)
                                    flag = 1
                                if confirm == "N" or confirm == "n":
                                    print("Directory", line.strip(), "has not been removed by user confirmation")
                                    logmsg = "Directory " + line.strip() + " has not been removed by user confirmation\n"
                                    outF.write(logmsg)
                                    flag=1
                                if confirm!="N" and confirm!="n" and confirm!="Y" and confirm!="y":
                                    print("Invalid input")
                else:
                    print(line.strip(), "does not exist")
                    logmsg = line.strip() + " does not exist\n"
                    outF.write(logmsg)
            else:
                print(path, line.strip(), "is empty entry in remove file")
            line = fp.readline()
            cnt += 1
outF.close()