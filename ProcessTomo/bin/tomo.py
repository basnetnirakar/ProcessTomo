#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 22:11:06 2021

This is the main script that controls the whole process.

If the name of input text file containing parameter is named inputs.txt then you just have to run it

If you are running on all the tomograms you dont have provide any inputs.

if you want to run only in specific tomograms then provide the name as list in text file 
@author: basnetn2
"""

import numpy as np
import pandas as pd
import input_parse2 as inp2
import tomolist as tom
import organize_data as org
import os
import subprocess
import motioncor2 as mot2
import make_stack as make
import shutil
import dose_filter as dose
import ctf_estimate as ctf
from pathlib import Path
import argparse,pathlib

parser = argparse.ArgumentParser()
parser.add_argument("--filename",default='inputs.txt',type=pathlib.Path)
parser.add_argument("--tomolists",default=False,type=pathlib.Path)
args = parser.parse_args()

names = args.filename
tomolist = args.tomolists

def main(names,tomolist):

      #parses the input file and make a dictionary of all the inputs
      inps = inp2.input_parse(names)
      
      # getting the inputs from the dictionary
      ampc = inps['ampc']
      bin_f = inps['bin_f']
      cs = inps['cs']
      flip = inps['flip']
      kv = inps['kv']
      pix = inps['pix']
      def_file = inps['def_file']
      rot = inps['rot']
      R_pix = float(inps['R_pix'])
      gain_file = inps['gain_file']
      cwd = inps['cwd']
      frame = inps['frames']

      #if the list of tomograms not provided, creates the list based on .mrc.mdoc file in raw directory
      if tomolist is False:
            file = inps['raw_data']+'/'+ inps['files']
            tomolist2 = tom.tomolist(file,inps['prefix'])

      else:
            tomolist2 = np.loadtxt(tomolist,dtype='str')

      #if sort is 1 in the input text files its sort the file into respective folder
      if inps['sort']==str(1):
            for i in tomolist2:
                  try:
                        e_dose = float(inps['e_dose'])
                        raw_data= inps['raw_data']
                        frames = inps['frames']
                        org.organize_data(raw_data, frames,i,e_dose)

                  except:
                        print(f'{i} has some error, please double check')

      else:
            pass


      #if motioncorr is 1 in input text file it will do motion correction
      if inps['motion']==str(1):
            mot2.do_motioncor(tomolist2,frame)

            #doing dose filtering
            dose.dose_filtering(tomolist2,R_pix)
      else: pass

      #if ctf is 1 the ctf estimation will be performed usinf gctf
      if inps['ctf'] == str(1):
            ctf.ctf(tomolist2)
      else:pass

if __name__ == "__main__":
      main(names,tomolist)