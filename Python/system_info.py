#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import os
import shutil
osn=list(os.uname())

def sys_name():
    return osn[0]

def load_avg():
    return os.getloadavg()

def arch_name():
    return osn[4]


def home_env():
    return os.environ["HOME"]

def current_uid():
    return os.getuid() 

def clear_screen():
    return os.system("clear")

def user_name():
    return os.getlogin()

def disk_size():
    BytesPerGB = 1024 * 1024 * 1024
    (total, used, free) = shutil.disk_usage("/")
    print ("Total Disk Usage        :- %.2fGB" % (float(total)/BytesPerGB))
    print ("Used                    :-  %.2fGB" % (float(used)/BytesPerGB))
    print ("Free                    :-  %.2fGB" % (float(free)/BytesPerGB))

clear_screen()
print ("Name of Operating System is :- ", sys_name())
print ("Load Average                :- ", load_avg())
print ("System Architecture         :- ", arch_name())
print ("Home environment is set to  :- ", home_env())
print ("Current UID                 :- ", current_uid())
print ("Current User Name           :- ", user_name())
print ( disk_size())
