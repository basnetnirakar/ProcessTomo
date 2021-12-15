# ProcessTomo
Python modules to process tomograms. This is the updated version of my previous scripts and now availiable via pip

pip install ProcessTomo
this is the alpha version and works only with tomograms taken with Serial-EM


# Tomo
This is the modular version of the previous tomogram processing.Tomograms acquired in serial em

#General usafe
tomo.py is the main script that controls the whole script

usage: tomo.py --filename inputs.txt [--tomolist tomo.txt](optional)

filename: provide all the microscope and acquistion parameters, example inputs.txt
tomolist: list of tomograms that you want to process, provide tomogram's meta data file name, e.g. tomo01.mrc.mdoc
In the beginning or if you dont want to process all tomograms.It prepares its own list form the mrc.mdoc file present in your raw dir
