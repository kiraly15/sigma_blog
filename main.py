from pathlib import Path
import sys
import cmd
import os
from re import sub
import cmd

cmd = 'python devo_request.py '

folder = "/usr/src/app/Translations/"
for file in os.listdir(folder):
    filepath = os.path.join(folder, file)
    f = open(filepath, 'r')
    r = f.read()
    cmdLine = cmd +("\'"+r+"\'")
    print('\n')
    print("Query results from the last 30 Days are printed to file "+ r)
    f.close()
    os.system(cmdLine)
