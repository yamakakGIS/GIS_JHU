import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"

def countstringfields(layer = None):   #numberStringFieldsWithLayer

    # If no layer is passed in, stop the function
    if layer == None:
        return None

    # Get the count for each field with type "String"
    n = 0
    for field in arcpy.ListFields(layer):
        if field.type == "String":
            n += 1

    return n