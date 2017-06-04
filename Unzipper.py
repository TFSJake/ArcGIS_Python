
import os, zipfile

dir_name = "C:\Users\jande\Desktop\Sentinel_Pics"
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files


for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
# Leave line 17 commented out unless you wish do delete the originals. I do not suggest it.
    # os.remove(file_name)



