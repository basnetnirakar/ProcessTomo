#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:28:28 2021

@author: basnetn2
"""
import os
import pandas as pd
import subprocess
import starfile
from pathlib import Path

R_pix = 'R_pix'
kv = 'kv'
cs = 'cs'
ampc = 'ampc'

def rearrange_gctf(gctf_file, df):
      """
      Re-arranges the gdct output file as per tilt angle
      Parameters
      ----------
      gctf_file :str
            name of gctf file
      df : dataframe
            dataframe which consists list osrted as per tilt angle,used as reference for ctf file

      Returns
      -------
      None.

      """
      if gctf_file.is_file():
            gctf_star =starfile.open('micrographs_all_gctf.star')
            gctf_star = gctf_star.set_index('rlnMicrographName')
            gctf_star = gctf_star.reindex(index=df['aligned_frames'])
            gctf_star = gctf_star.reset_index()
            starfile.write(gctf_star,'ctf.star')
      else:
            pass




def ctf(tomolist):
      cwd = os.getcwd()
      for l in tomolist:
            try:
                  os.chdir(f'{l[0:-9]}/Motioncorr')
                  print('Running Dosefiltering..')
                  df_tomo = pd.read_csv(f'{l[0:-9]}.txt')
                  df_dose = df_tomo[['pre-dose','dose']]
                  df_dose.to_csv(l[0:-9]+'dose.txt',sep = ' ',index=False,header=False)
                  ctf_cmd = 'Gctf --apix '+ str(R_pix) + ' --kV ' + str(kv) + ' --Cs ' + str(cs) + ' --ac ' + str(ampc) + ' -defS 500 --resL 50 --resH 5 ' + '*.mrc' + ' --boxsize 512  --defL  5000 --defH 50000 --defS  500 --astm 100'


                  subprocess.run(ctf_cmd,shell=True)

                  ##rearrange the output the gctf file according to the tilt
                  gctf_file_name = Path('micrographs_all_gctf.star')
                  rearrange_gctf(gctf_file_name, df_tomo)
                  os.rename('ctf.star',f'{l[0:-9]}_ctf.star')

                  os.chdir(cwd)


            except:
                  pass
                  raise
                  print('Check the input file')