#!/usr/bin/python

import numpy as np
from SDSSData.spectrum import Spectrum

filename = "spec-10000-57346-0002.fits"

# check we can read spectrum file, has 4 HDUs
def test_hdu():
	s = Spectrum(filename)
	assert len(s.datafile) == 4, "unexpected number of HDUs in file"

# check ra value makes sense 	
def test_ra():
	s= Spectrum(filename)
	assert 0 < s.ra() < 360 
