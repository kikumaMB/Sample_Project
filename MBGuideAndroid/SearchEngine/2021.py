import os
import openpyxl

def get_all_folders(root_directory):
    all_folders = []
    for foldername, _, _ in os.walk(root_directory):
        all_folders.append(foldername)
        print(all_folders)
    return all_folders

def write_to_excel(folders_list, output_file):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    for index, folder_name in enumerate(folders_list, start=1):
        sheet.cell(row=index, column=1, value=folder_name)

    workbook.save(output_file)
    print(f"Folder names written to {output_file}")

# Replace this with the root directory from where you want to start walking
root_directory = r"Z:\WebfsContent_2021"

# Replace this with the desired output Excel file name
output_excel_file = "2021f_content.xlsx"

all_folders_list = get_all_folders(root_directory)
write_to_excel(all_folders_list, output_excel_file)
