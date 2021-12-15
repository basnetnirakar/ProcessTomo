#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:31:40 2021

@author: basnetn2
"""
import subprocess
import os
import shutil
import pandas as pd
import make_stack as make

kv = 'kv'
pix='pix'
gain_file= 'gain_file'
def_file='def_file'
flip='flip'
bin_f = 'bin_f'
rot = 'rot'
cwd = 'cwd'
df_tomo = 'df_tomo'
gain_file = 'gain_file'
def_file = 'def_file'

def motioncor(df,gain,defect,Rot, Flip,bin_f):
      """
      Runs motioncor2 and creates a stack file

      Parameters
      ----------
      df : dataframe
            dataframe containing name of frames
      gain : str
            name of gain image obtained. 
      defect : str
            defect file for the camera
      Rot : int
            rotation needed to apply for gain file
      Flip : int
            if the gain image needed to be flipped
      bin_f : int =2
            bin factor while tomogram processing. normally superresolution tiff files are 0.5 binned

      Returns
      -------
      None.

      """
      for i in df['frames']:
            cmd = f'MotionCor2 -InTiff {i.strip()} -OutMrc {i.split(".")[0]}.mrc -Patch 7,5 -Iter 10 -Tol 0.5 -Kv {kv} -PixSize {pix} -Gpu 0 -Bft 500 150  -LogFile {i.split(".")[0]}.log -Gain {gain_file} -DefectFile {def_file} -RotGain {rot} -FlipGain {flip} -FtBin {bin_f}'

            subprocess.run(cmd,shell=True)

def do_motioncor(tomolist,frames):
      cwd = os.getcwd()
      for l in tomolist:
            try:
                  os.chdir(f'{l[0:-9]}/Motioncorr')
                  print('Running Motioncor2..')
                  shutil.copy(f'../{l[0:-9]}.txt',os.getcwd())
                  shutil.copy('../missing_frames.txt',os.getcwd())
                  df_tomo = pd.read_csv(f'{l[0:-9]}.txt')
                  tilt = df_tomo['tilts']
                  tilt.to_csv(f'{l[0:-9]}_motion_corr_dosefilt.rawtlt', header=False,index=False)

                  ########Run motioncorr
                  motioncor(df_tomo,gain_file,def_file,rot,flip,bin_f)
      
                  #check if there are some frames missing
      
                  count = len(open('missing_frames.txt').readlines())
      
                  if count == 0:
                        output = f'{l[0:-9]}_motion_corr_nofilt.mrc'
                        make.make_stack(df_tomo,output)
      
                  else:
                        pass
                        print(f'You have missing frame {l[0:-9]}')

                  os.chdir(cwd)

            except:
                  raise
                  pass
                  print(f'tomogram{l[0:9]} might have some error')