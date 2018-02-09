#parcelTax.py
import parcelclass
myparcel = parcelclass.Parcel("SFR", 125000)
print "Land use: ", myparcel.landuse
mytax = myparcel.assessment()
print "Tax assessment: ", mytax