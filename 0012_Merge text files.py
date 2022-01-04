# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 21:21:36 2022

@author: lsxin
"""
#%% Merge text file using pandas
import os,glob
import pandas as pd
from pathlib import Path
#Define a function to read and merge txt file using pandas
#Input: indir, outfname, in_extension, colNames, Header: output, output delimiter

#Script development
#list all *.FRE file inside the input folder
indir = r'D:\DoTWA_Data\FR201410_NoSBET_Q2\fr_1014\Tide\TideData'
in_Ext = '.FRE'
in_delimiter = ','
in_header = None
all_FRE = [f.name for f in Path(indir).iterdir() if f.name.endswith(in_Ext) ]

out_header = 'N'
out_Ext = in_Ext
out_delimiter = in_delimiter
out_colNames=['Day','Time','Tide','unknown','unknown']
out_fname = 'merge' + out_Ext

df_mergeList = list()
for fname in all_FRE:
    if fname != out_fname:
        df = pd.read_csv(fname,sep = in_delimiter,header=in_header)
        df_mergeList.append(df)        
df_merge = pd.concat(df_mergeList, axis=0) #row merge
if out_header == 'Y':
    df_merge.columns = out_colNames
    df_merge.to_csv(out_fname, index = None, header = out_colNames)
else:
    df_merge.to_csv(out_fname, index = None, header = None)

#%% Merge text files using pure Python - Keep original format
from pathlib import Path

indir = r'D:\DoTWA_Data\FR201410_NoSBET_Q2\fr_1014\Tide\TideData'

in_delimiter = ','
in_Ext = '.FRE'


out_header = 'N'
out_delimiter = in_delimiter
out_colNames=['Day','Time','Tide','unknown','unknown']
out_Ext = in_Ext
out_fname = 'merge' + out_Ext
outfile = open(out_fname,'w')
colNames = str(out_colNames)[1:-2].replace("'","").replace(', ',out_delimiter)
if out_header == 'Y':
        outfile.write(colNames+'\n')
else: pass

all_FRE = [f.name for f in Path(indir).iterdir() if f.name.endswith(in_Ext) ]

for fname in all_FRE:
    if fname != out_fname:
        with open(fname,'r') as infile:
            for line in infile:
                line = line.replace(in_delimiter,out_delimiter)
                if line != '\n': 
                    outfile.write(line)
                    print(line)
outfile.close()





















