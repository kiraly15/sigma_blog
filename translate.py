# import required module
import cmd
import os
from re import sub

rootdir = '/usr/src/app/sigma/rules/windows/wmi_event/'
cmd = './sigma/tools/sigmac -t devo -c sigma/tools/config/devo-win.yml '

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ruleoutput = 'Devo_'+ file
        devorule= ruleoutput.replace(".yml","") 
        cmdLine = cmd +subdir+'/'+file + ' -o '+ devorule
        os.system(cmdLine)
