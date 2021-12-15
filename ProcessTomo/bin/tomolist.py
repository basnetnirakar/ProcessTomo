#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 22:02:53 2021

@author: basnetn2
"""
import glob

def tomolist(files,tomo_prefix=0):
      """
      creates a list of tomogram needed for processing

      Parameters
      ----------
      files : str
            *.mrc.mdoc,*.mrc.mdoc file are created by the serail em for each tomogram
      
      tomo_prefix:  str
      the prefix used for tomo,it should be similar for all tomograms,for eg. prefix for tomo01.mrc,tomo02.mrc
      will be tomo
      sometimes there willbe other rawdata files like gridmap.mrc or other .mrc files which are not tomograms

      Returns
      -------
      list of tomograms

      """

      tomos = []
      tomo_pref = tomo_prefix   ###### Master input ###make sure it finds absoultye value not tomogram

      for k in glob.glob(files):
            if tomo_prefix == str(0):
                  tomos.append(k.split('/')[-1])

            elif tomo_pref in k:
                  tomos.append(k.split('/')[-1])

      return tomos