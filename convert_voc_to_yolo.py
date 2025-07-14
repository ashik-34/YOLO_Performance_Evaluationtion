import os
import xml.etree.ElementTree as ET
from tqdm import tqdm

# Paths
dataset_dir = 'VOC2028'
xml_folder = os.path.join(dataset_dir, 'Annotations')
yolo_labels_folder = os.path.join(dataset_dir, 'YOLOLabels')
os.makedirs(yolo_labels_folder, exist_ok=True)

# Class list
classes = ["hat", "person"]

def convert_bbox(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (x * dw, y * dh, w * dw, h * dh)

for xml_file in tqdm(os.listdir(xml_folder)):
    if not xml_file.endswith(".xml"):
        continue

    tree = ET.parse(os.path.join(xml_folder, xml_file))
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    out_lines = []
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)

        xml_box = obj.find('bndbox')
        box = (
            float(xml_box.find('xmin').text),
            float(xml_box.find('xmax').text),
            float(xml_box.find('ymin').text),
            float(xml_box.find('ymax').text),
        )
        bb = convert_bbox((w, h), box)
        out_lines.append(f"{cls_id} {' '.join(map(str, bb))}")

    with open(os.path.join(yolo_labels_folder, xml_file.replace('.xml', '.txt')), 'w') as f:
        f.write('\n'.join(out_lines))
