#!/usr/bin/python

import numpy as np
from ..Spectrum import Spectrum

filename = "spec-10000-57346-0002.fits"

# check we can read spectrum file, has 4 HDUs
def test_hdu():
	s = Spectrum(filename)
	assert len(s.hdu_list) == 4, "unexpected number of HDUs in file"
	
def test_ra
	s = Spectrum(filename)
	np.testing.assert_approx_equal(s.ra, 12.3432)