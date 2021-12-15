#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:50:47 2021

@author: basnetn2
"""

def input_parse(file):
      """
      It parses a input text file and creates the dictionary

      Parameters
      ----------
      file : str
            the file containig text inputs

      Returns
      -------
      inputs : TYPE
            DESCRIPTION.

      """
      try:
            inputs = {}
            with open(file) as f1:
                lines = [line for line in f1.readlines() if line.strip() if "#" not in line]
                for i in lines:
                      key,value = i.split('=')
                      inputs[key.strip()] = value.strip()

      except:
            raise
            #print('Something is wrong with your input file,Are you sure it is present?')

      return inputs

