import os
import shutil

import pandas as pd


path = r"C:\Users\KIKUMA\PycharmProjects\MBGuideAndroid\SearchEngine\output_all.xlsx"
df_Pa = pd.read_excel(path,sheet_name='PA', usecols='A')
df_Path = pd.read_excel(path,sheet_name='mbio', usecols='A')
df_lang = pd.read_excel(path,sheet_name='Lang', usecols='A')
PA = df_Pa.PA_Num.to_list()
Path = df_Path.PATH.to_list()
Lang = df_lang.Langcode.to_list()

for pa in PA:
    for path in Path:
        if pa in path:
            fldr_path = fr"{path}"
            try:
                list_of_files = os.listdir(fldr_path)
                for file in list_of_files:
                    for lang in Lang:
                        if 'Edition of BAIx' in file:
                            if lang in file:
                                destination_folder = fr'Z:\WebfsDownload\XML_Changes\{lang}\{pa}'
                                if not os.path.exists(destination_folder):
                                    os.makedirs(destination_folder)
                                source_file = fr'{path}\{file}'
                                filename = os.path.basename(source_file)
                                destination_path = os.path.join(destination_folder, filename)
                                shutil.copy(source_file, destination_path)
                                break

            except FileNotFoundError as fe:
                print(f"Not found-{pa}-{path}")



