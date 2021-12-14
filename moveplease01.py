#!/usr/bin/env python3


# import utilities
import shutil
import os

# change directory to mycode
os.chdir('/home/student/mycode/')

# move folders and files
shutil.move('raynor.obj', 'ceph_storage/')

# prompt user for name
xname = input('What is the new name for kerrigan.obj? ')


# rename file 
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



