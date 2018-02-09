#-------------------------------------------------------------------------------
# Name:        module1
"""Challenge 2
You are given a feature class called parcels.shp located in the Exercise12
folder that contains the following fields: FID, Shape, Landuse, and Value.
Modify the parceltax.py script so that it determines the property tax for
each parcel and stores these values in a list. You should use the class
created in the parcelclass.py script ? the class can remain unchanged.
Print the values of the final list as follows:    FID: <property tax>
"""
# Author:      yamakak
#
# Created:     08/02/2018
# Copyright:   (c) yamakak 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#parcelTax.py
import arcpy
from arcpy import env
import parcelclass
try:
    env.workspace = "C:/EsriPress/Python/Data/Exercise12"
    fc = "parcels.shp"
#each parcel and stores these values in a list
#FID, Shape, Landuse ("SFR" "MFR") or , and Value  125000

    with arcpy.da.SearchCursor(fc, ['Landuse', 'Value']) as cursor:
         for row in cursor:
       # print('Feature {0} has an area of {1}'.format(row[0], row[1]))

                        myparcel = parcelclass.Parcel(row[0], row[1])
                        print "Land use: ", myparcel.landuse
                        mytax = myparcel.assessment()
                        print "Tax assessment: ", mytax

# Remove
    del row

# Print your results

except arcpy.ExecuteError:
    print arcpy.GetMessages(2)
except:
    print "There has been a non tool error."


