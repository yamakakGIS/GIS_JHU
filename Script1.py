import arcpy
from arcpy import env
env.workspace = "D:/JHU/Sp 2018/Exercise12"
n = 0
fields = arcpy.ListFields( "streets.shp" )
for field in fields : #arcpy.ListFields(fields):
    if field.type == "String":
        n += 1

print n        