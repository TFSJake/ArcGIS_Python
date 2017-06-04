# What this does:
#
# KML to point, points then get a GUID added, unnecessary fields removed.


import arcpy, os, uuid


KML_input = ('')
OutputFolder = ('')
poles = 'Pole Name'


arcpy.KMLToLayer_conversion(KML_input, OutputFolder, poles)




arcpy.DeleteField_management(poles, "Name;FolderPath;SymbolID;AltMode;Base;Snippet;PopupInfo;HasLabel;LabelID")