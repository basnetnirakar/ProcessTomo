#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:20:37 2021

@author: basnetn2
"""

import numpy as np
import math
from datetime import datetime

def dose_info(array,dose_perframe):

      """
      Description: This will take array created by function get_tomolist and dose per frame and calulates dose information for each tilt.
      the output will be array with the two dose information for each tilt: prior cumulative dose and cumulative dose at the end of the image


      Parameters
      ----------
      array : numpy array
            output of function get_tomolist
      dose_perframe : dose per frame in e/A2
             float value

      Returns
      -------
      array 

      """

      #sort according to date and time.Important fortomograms ran with dose symmetric data collection

      sortedArray = np.array(sorted(array, key=lambda x: datetime.strptime(x[3], '%d-%b-%y %H:%M:%S')))


      dose_per_tilt = []
      prior_tilt_dose = []
      dose = 0
      new_dose = []
      for i in sortedArray:
          prior_tilt_dose.append(dose)
          #dose_O = float(i[3])*dose_perframe
          dose_t = (1/math.cos(abs(float(i[0])*math.pi/180)))*dose_perframe
          dose_per_tilt.append(dose_t)
          cum_dose = dose_t + dose
          new_dose.append(cum_dose)
          dose = cum_dose
          print(dose)

      array_dose = np.array([prior_tilt_dose,new_dose]).swapaxes(1, 0)
      array_dose = np.append(sortedArray,array_dose,axis=1)
      sorted_dose_array = np.array(sorted(array_dose, key=lambda l:float(l[0]))) #sort according to tilt angles
      return(sorted_dose_array)