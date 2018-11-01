#! /usr/bin/env python

import glob
from SDSSData.spectrum import Spectrum

files = glob.glob("*.fits")
print(files[0])

spec = Spectrum(files[0])

# spec._isValid()