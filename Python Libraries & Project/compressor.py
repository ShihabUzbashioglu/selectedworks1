from zipfile import ZipFile


with ZipFile('binood.zip', 'r') as zip_object :
    zip_object.extractall()

#list of all files that are archieved in the zip file

print(zip_object.namelist)