#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:34:07 2021

@author: basnetn2
"""
import numpy as np
import subprocess


def make_stack(df,output):
      """
      Makes stack fromt he motion corrected images using newstack imod

      Parameters
      ----------
      df : dataframe
            DESCRIPTION.
      output :image stack
            mrc stack stack sequentially -min to +max

      Returns
      -------
      None.

      """
      section = 0
      total_images = len(df['aligned_frames'])
      newstack_image_file = [total_images]
      for i in df['aligned_frames']:
            try:
                  newstack_image_file.append(i)
                  newstack_image_file.append(section)
                  np.savetxt('images.txt',np.array([newstack_image_file]).swapaxes(1,0),fmt='%s')
                  stack = 'newstack ' + '-filei images.txt ' + output
                  subprocess.run(stack,shell=True)
            except:
                  pass