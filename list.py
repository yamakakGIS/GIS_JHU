import arcpy
def listfieldnames(table):
  fields = arcpy.ListFields(table)
  namelist = []
  for field in fields:
    namelist.append(field.name)
    return namelist
if __name__ == "__main__":    
    fieldnames = listfieldnames("D:/JHU/Sp 2018/Exercise12/streets.shp")
    print fieldnames    
 
