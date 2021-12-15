#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:24:55 2021

@author: basnetn2
"""

import os
import shutil
import numpy as np
import pandas as pd
import get_tomolist as get_tomo
import dose_info as get_dose

def organize_data(raw_data,frames,l,e_dose):
      """
      

      Parameters
      ----------
      raw_data : str
            path/name of directory which contains raw data. ".mrc files or .mrc.mdoc files"
      frames : str
            path/name of directory which contains frames
      l : list
      name containing the list of tomograms

      Returns
      -------
      None.
      creates subdirectory for each tomograms 

      """

      cwd = os.getcwd()
      
      os.chdir(cwd+'/'+raw_data)

      os.chdir(cwd)


      os.makedirs(l[0:-9])

      os.chdir(l[0:-9])

      os.makedirs('Motioncorr')

      shutil.move(cwd+'/'+raw_data+'/'+l, os.getcwd())

      shutil.move(cwd+'/'+raw_data+'/'+l[0:-5], os.getcwd())

      array_sort = get_tomo.get_tomolist(l)  #local modules

      array_dose = get_dose.dose_info(array_sort, e_dose)

      np.savetxt ('tomolist.log',array_sort,fmt = '%s',delimiter=" ")
      df_tomo = pd.DataFrame(array_dose, columns = ['tilts','frames','aligned_frames', 'time', 'subframes','pre-dose','dose'])
      df_tomo.to_csv(l[0:-9]+'.txt')

      missing_frames = []

      print(l)

      for j in range(len(array_sort)):
            try:
                  mrc_file = str(array_sort[j][1]).strip()

                  shutil.move(cwd+'/'+frames+'/'+mrc_file, "Motioncorr")
            except:
                  missing_frames.append(mrc_file)
                  pass

      missing_frames = np.array([missing_frames]).swapaxes(1, 0)
      np.savetxt('missing_frames.txt',missing_frames,fmt='%s')
      os.chdir(cwd)

      return