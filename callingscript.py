#callingscript.py
import arcpy
from arcpy import env
import mycount      # Add your custom module folder to the system paths
try:
    env.workspace = "D:/JHU/Sp 2018/Exercise12"
    
     
#  a layer object  
    streetsLayer = "streets.shp"
     
# Call  countstringfields
    numberOfFieldsTypeString = countstringfields(streetsLayer)

# Remove  
    del streetsLayer

# Print your results
    print numberOfFieldsTypeString
except arcpy.ExecuteError:
    print arcpy.GetMessages(2)
except:
    print "There has been a nontool error."    
