import os
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
                                print(fr"{file}--{pa}--{path}")
                                break

            except FileNotFoundError as fe:
                print(f"Not found-{pa}-{path}")



