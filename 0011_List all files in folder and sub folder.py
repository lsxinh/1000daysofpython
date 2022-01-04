# -*- coding: utf-8 -*-
import os
import time
input_folder = r'D:\DoTWA_Data\FR201410_NoSBET_Q2\fr_1014\Tide\TideData'

#Different ways to list files in folder and sub folder
#%% using os.listdir() - list all file and folders in a folder
start_time = time.time()
#List all files and folders
os.listdir(input_folder)
#list only file 
all_files = [f for f in os.listdir(input_folder) if os.path.isfile(f)]
#list only folder
all_folder = [f for f in os.listdir(input_folder) if os.path.isdir(f)]

#list all *.FRE files 
all_files = [f for f in os.listdir(input_folder) if (os.path.isfile(f) and f.endswith('.FRE'))]

#list all *.TID files 
all_files = [f for f in os.listdir(input_folder) if (os.path.isfile(f) and f.endswith('.tid'))]

#list all *.FRE files without extension
all_files = [f.split('.')[0] for f in os.listdir(input_folder) if (os.path.isfile(f) and f.endswith('.FRE'))]

#list all *.tid files without extension
all_files = [f.split('.')[0] for f in os.listdir(input_folder) if (os.path.isfile(f) and f.endswith('.tid'))]

print("--- %s seconds ---" % (time.time() - start_time))

#%% Using glob
import glob
import os
#all files - full path
all_files = [f for f in glob.glob(os.path.join(input_folder,'*.*'))]

#all files - full path - including subdirectories - not working -becareful
all_files = [f for f in glob.glob(os.path.join(input_folder,'*.*'),recursive=True)]

#all files and folders - full path
all_ff = [f for f in glob.glob(os.path.join(input_folder,'*'))]

#all *.FRE files - full path
all_FRE = [f for f in glob.glob(os.path.join(input_folder,'*.FRE'))]

#all *.tid files - full path
all_tid = [f for f in glob.glob(os.path.join(input_folder,'*.tid'))]


#%% Using os.scandisk
#all files and folder
all_ff = [f.name for f in os.scandir(input_folder)]

#all *.FRE
all_FRE = [f.name for f in os.scandir(input_folder) if f.name.endswith('.FRE')]

#all *.tid
all_tid = [f.name for f in os.scandir(input_folder) if f.name.endswith('.tid')]

#all folder
all_f = [f.name for f in os.scandir(input_folder) if os.path.isdir(f)]


#%% Using os.walk
def file_lst_ext_subfolder(src_folder,file_ext="*"):
    '''
    list all files with extentions in a folder including subfolders using os.walk
    file_ext can be '*' or '.TIF' or '.ALL' named should be capitalised

    '''
    #Directory management
    root_p_lst = list()
    folder_p_lst = list()
    file_p_lst_full = list()
    for root, folders, filenames in os.walk(src_folder):
        root_p_lst.append(root)
        for folder in sorted(folders):
            folder_p_lst.append(str(os.path.join(root,folder)))
        for filename in sorted(filenames):
            file_p_lst_full.append(os.path.join(root,filename))
    file_p_lst = list()
    for f in file_p_lst_full:
        if file_ext == "*":
            return file_p_lst_full
        if file_ext.upper() in f[-5:].upper(): #asume ext has 3 characters
            file_p_lst.append(f)
        else: next
    return file_p_lst

def file_lst_ext_subfolder2(src_folder,file_ext="*"):
    '''
    list all files with extentions in a folder including subfolders using os.walk
    file_ext can be '*' or '.TIF' or '.ALL' named should be capitalised

    '''
    #Directory management
    root_p_lst = list()
    folder_p_lst = list()
    file_p_lst_full = list()
    for root, folders, filenames in os.walk(src_folder):
        root_p_lst.append(root)
        for folder in sorted(folders):
            folder_p_lst.append(str(os.path.join(root,folder)))
        for filename in sorted(filenames):
            file_p_lst_full.append(os.path.join(root,filename))
    for f in file_p_lst_full:
        if file_ext == "*": 
            return file_p_lst_full
        else:
            file_p_lst = [file for file in file_p_lst_full if file.endswith(file_ext)]
            return file_p_lst

#list all files
file_lst_ext_subfolder(input_folder,file_ext="*")


#list all *.FRE
file_lst_ext_subfolder(input_folder,file_ext=".FRE")

#list all files named *.tid
file_lst_ext_subfolder(input_folder,file_ext=".tid")


#list all files named *.FRE
file_lst_ext_subfolder2(input_folder,file_ext=".FRE")

#list all files named *.tid
file_lst_ext_subfolder2(input_folder,file_ext=".tid")

def folder_lst_ext_subfolder(src_folder,file_ext="*"):
    '''
    list all folders with extentions in a folder including subfolders

    '''
    #Directory management
    root_p_lst = list()
    folder_p_lst = list()
    for root, folders, filenames in os.walk(src_folder):
        root_p_lst.append(root)
        for folder in sorted(folders):
            folder_p_lst.append(str(os.path.join(root,folder)))
    return folder_p_lst

#list all folders
folder_lst_ext_subfolder(input_folder,file_ext="*")

#%% Using pathlib.Path
from pathlib import Path

#all files and folder
all_ff = [f.name for f in Path(input_folder).iterdir()]

#all files
all_f = [f.name for f in Path(input_folder).iterdir() if f.is_file()]

#all folders
all_f = [f.name for f in Path(input_folder).iterdir() if f.is_dir()]

#all .FRE files
all_f = [f.name for f in Path(input_folder).iterdir() if f.name.endswith('.FRE')]

#all .tid files
all_f = [f.name for f in Path(input_folder).iterdir() if f.name.endswith('.tid')]

