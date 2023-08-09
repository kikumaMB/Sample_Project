from lxml import etree
import xml.etree.ElementTree as ET
xml_path = r"C:\Users\KIKUMA\Desktop\xml_chnages\jobd8966188d0a7fa920ac2a8e75e28e817.xml"
tag_name = 'ul'
attribute_name = 'y.id'
attribute_value = 'ID_8bd8e59a34a3c7d0354ae36511b76b05-769db98406602ff1354ae3657d9e268f'


parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(xml_path, parser)
root = tree.getroot()

for parent in root.findall('.//'):
    for elem in parent.findall(tag_name):
        atrr = elem.get(attribute_name)
        if attribute_value in atrr:
            parent.remove(elem)

tree.write(xml_path, pretty_print=True, xml_declaration=True, encoding='utf-8')
try:
    ET.parse(xml_path)
    print("OK")
except ET.ParseError as ep:
    print(ep)
    print("NOT OK")









