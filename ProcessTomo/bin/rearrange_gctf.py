#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:36:30 2021

@author: basnetn2
"""


import starfile

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