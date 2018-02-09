import arcpy
import list
arcpy.env.workspace = "D:/JHU/Sp 2018/Exercise12/"
fields = list.listfieldnames("streets.shp")
print fields