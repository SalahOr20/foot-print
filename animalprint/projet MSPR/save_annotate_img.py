
import cv2
import xml.etree.ElementTree as ET
import os

def visualize_annotations(image_path, annotation_path):
    image = cv2.imread(image_path)
    tree = ET.parse(annotation_path)
    root = tree.getroot()

    for obj in root.findall('object'):
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

    cv2.imshow('Annotated Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_visualized_image(image_path, annotation_path, output_path):
    image = cv2.imread(image_path)
    
    tree = ET.parse(annotation_path)
    root = tree.getroot()

    for obj in root.findall('object'):
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

    #cv2.imwrite(output_path, image)
    success = cv2.imwrite(output_path, image)

    if success:
        print("Image saved successfully.")
    else:
        print("Error: Image not saved.")

image_path = 'C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/annotation_image/Ecureuil/2aea2wd.jpg'
annotation_path = 'C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/annotation_image/Ecureuil/2aea2wd.xml'
output_path = 'C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/annotation_image/Ecureuil/2aea2wd.jpg'
save_visualized_image(image_path, annotation_path, output_path)
visualize_annotations(image_path, annotation_path)


