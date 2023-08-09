import os
import zipfile

folder_path = r'C:\Users\KIKUMA\Desktop\Deo\Images'
output_path = r'C:\Users\KIKUMA\Desktop\Deo\zpipfile.zip'

files = os.listdir(folder_path)

with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files:
        file_path = os.path.join(folder_path, file)
        arcname = os.path.relpath(file_path, folder_path)
        zipf.write(file_path, arcname)




