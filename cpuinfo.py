# -*- coding: utf-8 -*-
##
## cpuinfo2.py (Python3 Version)
##
import re
from time import sleep

import numpy as np

stat_path = "/proc/stat"
stat_path1 = "stat.sample_1"
stat_path2 = "stat.sample_2"


def readcpu(path):
    f = open(path,"r")

    line = f.readline()
    while line:
        if re.match(r'model name',line):
            line = line.replace('\n','')
            line = line.replace('model name	: ','')
            cpu_model = line
            return cpu_model 
        line = f.readline()

    return ""


def readstat(path, usrtm, nicetm, systm, idletm, iowaittm):
    f = open(path,"r")

    line = f.readline()
    while line:
        result = re.match(r'cpu[\d+]',line)
        if result:
            #line.replace('\n','')
            tok = line.split(' ') 

            usrtm.append(int(tok[1])) 
            nicetm.append(int(tok[2]))
            systm.append(int(tok[3]))
            idletm.append(int(tok[4]))
            iowaittm.append(int(tok[5]))
            #print("{:s} {:.1f}%".format(tok[0], (usage/sum)*100 ) )
        line = f.readline()
    return 0


# RED       = '\033[31m' # 80-99
# YELLOW    = '\033[33m' # 60-79
# CYAN      = '\033[36m' # 41-59
# GREEN     = '\033[32m' # 20-39
# BLUE      = '\033[34m' # 0 -19
def PresetColor(usage):
    if      usage < 20.0 :
        print(Color.BLUE,end="") 
    elif usage < 40.0 :
        print(Color.GREEN,end="") 
    elif usage < 60.0 :
        print(Color.CYAN,end="") 
    elif usage < 80.0 :
        print(Color.YELLOW,end="") 
    else :
        print(Color.RED,end="") 


class Color:
    BLACK     = '\033[30m'
    RED       = '\033[31m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    BLUE      = '\033[34m'
    PURPLE    = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    END       = '\033[0m'
    BOLD      = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE   = '\033[07m'
    
    CLEAR     = '\033[2J\033[0;0H'
    CLEARLINE = '\033[K'
    

def CPUINFO():    
    usrtm1=[]
    nicetm1=[]
    systm1=[]
    idletm1=[]
    iowaittm1=[]
    
    usrtm2=[]
    nicetm2=[]
    systm2=[]
    idletm2=[]
    iowaittm2=[]
    
    readstat(stat_path, usrtm1, nicetm1, systm1, idletm1, iowaittm1)
    #readstat(stat_path1, usrtm1, nicetm1, systm1, idletm1, iowaittm1)
    sleep(0.5)
    readstat(stat_path, usrtm2, nicetm2, systm2, idletm2, iowaittm2)
    #readstat(stat_path2, usrtm2, nicetm2, systm2, idletm2, iowaittm2)

    usrtm    = np.array(usrtm2)    - np.array(usrtm1)
    nicetm   = np.array(nicetm2)   - np.array(nicetm1)
    systm    = np.array(systm2)    - np.array(systm1)
    idletm   = np.array(idletm2)   - np.array(idletm1)
    iowaittm = np.array(iowaittm2) - np.array(iowaittm1)
    #
    cpu_time = usrtm + nicetm + systm
    total      = cpu_time + idletm
    
    cpu_usage = (cpu_time*100.0)/total 
    
    num_of_cpu = len(cpu_usage)
    
    print(Color.CLEAR,end="")
    print("[CPU] {:s}".format(readcpu("/proc/cpuinfo")))
    print("+------------+------------+------------+------------+------------+")
    for i in range(num_of_cpu):
        
        usage = cpu_usage[i]
        print("|{:2d}| ".format(i), end="")
        
        PresetColor(usage)
        print("{:>5.1f} % ".format(usage), end="")
        print(Color.END,end="")
    
        if ((i+1) % 5) == 0 :
            print("|")
            
    print("|")
    print("+------------+------------+------------+------------+------------+")

#exit()

if __name__ == '__main__':
    while True:
        CPUINFO()
        sleep(0.5)
