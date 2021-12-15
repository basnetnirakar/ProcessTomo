#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:00:21 2021

@author: basnetn2
"""

import pandas as pd
import os
import subprocess
import shutil


R_pix = 'R_pix'

def dose_filtering(tomolist,R_pix):
      """
      dose-Filter the tomogram tilts according as described in Grant and Grigoreiff, 2015
      using mtffilter from IMOD

      Parameters
      ----------
      tomolist : TYPE
            DESCRIPTION.
      R_pix :float 
            pixel size of the images

      Returns
      -------
      dose filtered stack

      """
      cwd = os.getcwd()
      for l in tomolist:
            try:
                  os.chdir(f'{l[0:-9]}/Motioncorr')
                  print('Running Dosefiltering..')
                  df_tomo = pd.read_csv(f'{l[0:-9]}.txt')
                  df_dose = df_tomo[['pre-dose','dose']]
                  df_dose.to_csv(l[0:-9]+'dose.txt',sep = ' ',index=False,header=False)
                  mtfilter = f" mtffilter -InputFile {l[0:-9]}_motion_corr_nofilt.mrc -OutputFile {l[0:-9]}_motion_corr_dosefilt.mrc -TypeOfDoseFile 3 -DoseWeightingFile {l[0:-9]}dose.txt -PixelSize {R_pix/10}"
                  subprocess.run(mtfilter,shell=True)


                  ########## move the stacks
                  shutil.move(f'{l[0:-9]}_motion_corr_nofilt.mrc', f'../{l[0:-9]}_motion_corr_nofilt.mrc')
                  shutil.move(f'{l[0:-9]}_motion_corr_dosefilt.mrc', f'../{l[0:-9]}_motion_corr_dosefilt.mrc')
                  shutil.move(f'{l[0:-9]}_motion_corr_dosefilt.rawtlt',f'../{l[0:-9]}_motion_corr_dosefilt.rawtlt')
                  os.chdir(cwd)

            except:
                  raise
                  print('Check the input file')

