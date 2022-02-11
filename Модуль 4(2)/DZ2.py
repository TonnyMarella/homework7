# Создайте XML файл с вложенными элементами и воспользуйтесь языком поиска XPATH.
# Попробуйте осуществить поиск содержимого по созданному документу XML,
# усложняя свои запросы и добавляя новые элементы, если потребуется

import xml.etree.ElementTree as ET

p = ET.Element('parent')
p2 = ET.Element('second_parent')

c = ET.SubElement(p, 'child')
c2 = ET.SubElement(p, 'child2')
c3 = ET.SubElement(p, 'child3')

tree = ET.ElementTree(p)
second = ET.ElementTree(p)
tree.write("second.xml")
second.write("secondTree.xml")

value = ET.parse('second.xml')

x = value.findall('.//*')

print(x[2])