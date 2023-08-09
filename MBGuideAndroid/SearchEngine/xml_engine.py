import os
import shutil
import time
import zipfile
import lxml
from lxml.html.clean import Cleaner
import xml.etree.ElementTree as ET
import pandas as pd

xml_path = r"C:\Users\KIKUMA\Desktop\xml_chnages\test\jobd8966188d0a7fa920ac2a8e75e28e817.xml"
tree = ET.parse(xml_path)
root = tree.getroot()
tag_texts = []
elements_to_remove = []
for element in root.findall('.//{}'.format('ul')):
    print(element.get("y.id"))
    if 'ID_8bd8e59a34a3c7d0354ae36511b76b05-769db98406602ff1354ae3657d9e268f' in element.get("y.id"):
        root.remove(element)


print("Done")








