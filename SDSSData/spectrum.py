from .errors import *
from astropy.io import fits

# ========================
# Define spectrum class
# ========================

class Spectrum(object):
	def __init__(self, filepath = None):
		if filepath == None:
			raise SDSSFileNotSpecified("A spectrum file must be specified.")
		self.filepath = filepath
		self.datafile = fits.open(self.filepath)
		self._ra = None
		
# 		if not self._isValid:
# 			pass
	
	def _isValid(self, file=None):
		# check file is valid
		if len(self.datafile) != 4:
			raise HDUError("The number of HDU is not 4")
	
	def ra(self):
		''' Returns the RA of this spectrum in degrees'''
		if self._ra == None:
			hdr = self.datafile[0].header
			# check if key exists
			if not "RA" in list(hdr.keys()):
				raise HDUKeyError("Key does not exist in header")
			self._ra = hdr['RA']
		return(self._ra)
