#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
"""
Now let?s turn this into a function.
The main part of your script should use a workspace and
1) create a list of all  the polygon feature classes in that workspace.
! You can use a workspace of shapefiles or a workspace of feature classes in a geodatabase ? either way,
you only need to consider a single workspace.
2) n the script needs to use a function to determine the mean center for all
polygons in a feature class and
3)  write this as a new feature class.
4) When calling    the function, you should specify the name of the input feature class and the
 name of the output feature class to write the result.

  An easy way to set the  name of the output feature class
Lab Assignment 5 4
would be to add something to the name of the input, for example zipcodes.shp as
 input would become zipcodes_center.shp or some alternative version of this.

So in your script you will need to iterate over the polygon feature classes and
 with each iteration call the function to create a new feature class of the mean center.


Note: By creating a function, your code become more re-usable since you could
more easily copy the function into another script.
The next step could be to actually place the function into a stand-alone script
 and import the script as a module when you want to use the function.
  No need to create a stand-alone script here.


"""
# Author:      yamakak
#
# Created:     09/02/2018
# Copyright:   (c) yamakak 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import arcpy, fileinput, os
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise05"

env.overwriteOutput = True
def  centerPolygon() :
     featureclasses = arcpy.ListFeatureClasses("*",'POLYGON',"")
     print   featureclasses

     for fc in featureclasses:
        desc = arcpy.Describe(fc)
        spatialref = desc.spatialReference
        print  desc.name
        cursor = arcpy.da.SearchCursor(fc, ["SHAPE@X", "SHAPE@Y"])
        sumx = 0
        sumy = 0
        count = 0
        for row in cursor:
            sumx = sumx + row[0]
            sumy = sumy + row[1]
            count += 1
        meanx = sumx/count
        meany = sumy/count
        newfc = desc.name.split('.')[0] +"_center" + ".shp"
        print   newfc
        if arcpy.Exists(newfc):
           arcpy.Delete_management(newfc)
        arcpy.CreateFeatureclass_management( env.workspace, newfc, "POINT", "", "", "", spatialref)
        cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
        point = arcpy.Point(meanx, meany)
        cursor.insertRow([point])
        del cursor
if __name__ == '__main__':
   centerPolygon()

