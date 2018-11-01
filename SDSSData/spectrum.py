from .errors import *
from astropy.io import fits
from astropy.table import Table

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
		self._isValid(filepath)

	
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
		
	@property
	def wavelength(self):
		"""Wavelength binning, linear bins."""
		if getattr(self,'_wavelength',None) is None:
			self._wavelength = 10**self.datafile[1].data['loglam']
		return(self._wavelength)
	
	@property
	def flux(self):
		if getattr(self,'_flux',None) is None:
			self._flux = self.datafile[1].data['flux']
		return(self._flux)
    
	def getspec(self):
		'''return the spectrum as a table'''
		t = Table([self.wavelength, self.flux], names=('wavelength','flux'))
		return(t)