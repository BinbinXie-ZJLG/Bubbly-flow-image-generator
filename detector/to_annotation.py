import os
import xml.dom.minidom

# def transfrom_xlm_to_txt(file_dirpath, savepath):
#     xml_list = []
#     for dirpath, dirname, filepath in os.walk(file_dirpath):
#         for one_filepath in filepath:
#             xml_path = os.path.join(dirpath, one_filepath)
#             xml_list.append(xml_path)
#     dir_path_txt = savepath
#     if os.path.exists(dir_path_txt) == False:
#         os.mkdir(dir_path_txt)
#     for one_xml_path in xml_list:
#         print(one_xml_path)
#         DOMTree = xml.dom.minidom.parse(one_xml_path)
#         collection = DOMTree.documentElement
#         filename = collection.getElementsByTagName('filename')[0].childNodes[0].data
#         filename='picture\\'+filename
#         objects = collection.getElementsByTagName('object')
#         image_number = one_xml_path.split("\\")[-1].split(".")[0]
#         with open(dir_path_txt + "\\" + "{}".format(image_number) + ".txt", 'w', encoding='utf-8') as writer:
#             for obj in objects:
#                 name = obj.getElementsByTagName("name")[0].childNodes[0].data
#                 bndbox = obj.getElementsByTagName("bndbox")[0]
#                 xmin = bndbox.getElementsByTagName("xmin")[0].childNodes[0].data
#                 ymin = bndbox.getElementsByTagName("ymin")[0].childNodes[0].data
#                 xmax = bndbox.getElementsByTagName("xmax")[0].childNodes[0].data
#                 ymax = bndbox.getElementsByTagName("ymax")[0].childNodes[0].data
#                 values = "{}\t{},{},{},{},{}\n".format(filename, xmin, ymin, xmax, ymax,name)
#                 writer.write(values)

# file_dirpath = "E:\\record\\label"
# savepath = "E:\\record\\annotation"
# transfrom_xlm_to_txt(file_dirpath, savepath)


import os

for filename in os.listdir("E:\\record\\annotation"):
    print(filename)
    with open("E:\\record\\annotation\\"+filename,encoding='utf-8') as f:
        for line in f.readlines():
            with open("all.txt","a") as fp:
                fp.write(line)