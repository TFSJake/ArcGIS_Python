
# Import arcpy module
import arcpy


# Local variables:
Default_gdb__3_ = "C:\\Users\\jande\\Desktop\\ArcGIS\\Default.gdb"
elevation = "C:\\Users\\jande\\Desktop\\ArcGIS\\Default.gdb\\elevation2"
elevation__2_ = elevation
elevation__3_ = elevation
elevation__4_ = elevation
Default_gdb__2_ = "C:\\Users\\jande\\Desktop\\ArcGIS\\Default.gdb"
nasa_locations = "C:\\Users\\jande\\Desktop\\ArcGIS\\Default.gdb\\nasa_locations"
nasa_locations__2_ = nasa_locations
nasa_locations__3_ = nasa_locations

# Process: Create Feature Class (3)
arcpy.CreateFeatureclass_management(Default_gdb__3_, "elevation", "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1966',DATUM['D_WGS_1966',SPHEROID['WGS_1966',6378145.0,298.25]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98314157377769E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")

# Process: Add Field (3)
arcpy.AddField_management(elevation, "z", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field (6)
arcpy.AddField_management(elevation, "X", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field (7)
arcpy.AddField_management(elevation, "Y", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Create Feature Class (4)
arcpy.CreateFeatureclass_management(Default_gdb__2_, "nasa_locations", "POINT", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1966',DATUM['D_WGS_1966',SPHEROID['WGS_1966',6378145.0,298.25]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98314157377769E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")

# Process: Add Field (4)
arcpy.AddField_management(nasa_locations, "X", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field (8)
arcpy.AddField_management(nasa_locations, "Y", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

