#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:19:02 2021

@author: basnetn2
"""
import numpy as np

def get_tomolist(f1):

      """
      This functions extract all necessary information from the mdoc files and makes an table.
      This contains various metadata information for various processes
      """
      co1 = []
      frames = []
      image = []
      time = []
      frame_number= []
      file = open(f1)
      for line in file:
            if 'TiltAngle' in line:
                (col1,col2)=line.split('=')
                #print (col2)
                co1.append(float(col2))
        
            elif 'DateTime' in line:
                (ind, date_time) = line.split('=')
                time.append(date_time.strip())

            elif 'NumSubFrames' in line:
                  subframes = line.split('=')[-1]
                  frame_number.append(subframes)

            if 'SubFramePath' in line:
                (col1,col2)=line.split('=')
                name=col2.split('\\')[-1]
                aligned_frame = name.split('.')[0]+'.mrc'

                frames.append(name)
                image.append(aligned_frame)

      
      array = np.array([co1,frames,image,time,frame_number]).swapaxes(1,0)
      return (array)
      file.close()
