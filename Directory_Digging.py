# coding=utf-8
import os, shutil



# Select the bands you want to retrieve.
#
# Sentinel-2 Bands	Central Wavelength (µm)	Resolution (m)
# Band 1 – Coastal aerosol	0.443	60
# Band 2 – Blue	0.490	10
# Band 3 – Green	0.560	10
# Band 4 – Red	0.665	10
# Band 5 – Vegetation Red Edge	0.705	20
# Band 6 – Vegetation Red Edge	0.740	20
# Band 7 – Vegetation Red Edge	0.783	20
# Band 8 – NIR	0.842	10
# Band 8A – Narrow NIR	0.865	20
# Band 9 – Water vapour	0.945	60
# Band 10 – SWIR – Cirrus	1.375	60
# Band 11 – SWIR	1.610	20
# Band 12 – SWIR	2.190	20
bands = ["12.jp2", "08.jp2"]


directory = "C:\Users\jande\Desktop\Final_Project\Data"
dstdir = "C:\Users\jande\Desktop\Final_Project\NBR_DataORIGINAL"

os.makedirs(dstdir)
for root, dirs, files in os.walk(directory):
    for file in files:
        fullpath = os.path.join(root,file)
# Copies the selected files to a new folder
        if file.endswith(tuple(bands)):
            shutil.copy(fullpath, dstdir)
