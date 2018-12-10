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

def total_disk_size():
    BytesPerGB = 1024 * 1024 * 1024
    (total, used, free) = shutil.disk_usage("/")
    return (" %.2fGB " % (float(total)/BytesPerGB))
    #return ("Total Disk Size         :-  %.2fGB " % (float(total)/BytesPerGB))
    #return ("Used                    :-  %.2fGB" % (float(used)/BytesPerGB))
    #return ("Free                    :-  %.2fGB" % (float(free)/BytesPerGB))


def disk_usage():
    BytesPerGB = 1024 * 1024 * 1024
    (total, used, free) = shutil.disk_usage("/")
    #return ("Disk Used               :-  %.2fGB" % (float(used)/BytesPerGB))
    return (" %.2fGB" % (float(used)/BytesPerGB))



def disk_free():
    BytesPerGB = 1024 * 1024 * 1024
    (total, used, free) = shutil.disk_usage("/")
    #return ("Free                    :-  %.2fGB" % (float(free)/BytesPerGB))
    return (" %.2fGB" % (float(free)/BytesPerGB))

clear_screen()
print ("Name of Operating System is :- ", sys_name())
print ("Load Average                :- ", load_avg())
print ("System Architecture         :- ", arch_name())
print ("Home environment is set to  :- ", home_env())
print ("Current UID                 :- ", current_uid())
print ("Current User Name           :- ", user_name())
print ("Actual Disk Size            :-", total_disk_size())
print ("Disk Used                   :-", disk_usage())
print ("Free Space Available        :-", disk_free())
