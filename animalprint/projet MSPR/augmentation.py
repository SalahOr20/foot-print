import os
import xml.etree.ElementTree as ET
import cv2
from imgaug import augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage


def augment_dataset(image_folder, annotation_folder, output_images_folder, output_annotation_folder):
    seq = iaa.Sequential([
        iaa.Fliplr(0.5), 
        iaa.Affine(rotate=(-10, 10)),  
        iaa.GaussianBlur(sigma=(0, 1.0)),  
        iaa.Multiply((0.5, 1.5), per_channel=0.5),  
        iaa.ContrastNormalization((0.5, 2.0), per_channel=0.5),  
    ], random_order=True)

    for filename in os.listdir(image_folder):
        image_path = os.path.join(image_folder, filename)
        image = cv2.imread(image_path)
        annotation_filename = os.path.splitext(filename)[0] + '.xml'
        annotation_path = os.path.join(annotation_folder, annotation_filename)
        annotation_tree = ET.parse(annotation_path)
        annotation_root = annotation_tree.getroot()

        image_aug, annotation_aug = augment_image_and_annotation(image, annotation_root, seq)

        output_image_path = os.path.join(output_images_folder, filename)
        output_annotation_path = os.path.join(output_annotation_folder, annotation_filename)
        cv2.imwrite(output_image_path, image_aug)
        annotation_tree.write(output_annotation_path)

def augment_image_and_annotation(image, annotation_root, seq):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    bboxes = []
    for obj in annotation_root.findall('object'):
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        bboxes.append([xmin, ymin, xmax, ymax])

    bboxes_imgaug = [BoundingBox(x1=xmin, y1=ymin, x2=xmax, y2=ymax) for xmin, ymin, xmax, ymax in bboxes]
    bboxes_imgaug = BoundingBoxesOnImage(bboxes_imgaug, shape=image.shape)

    image_aug, bboxes_aug = seq(image=image, bounding_boxes=bboxes_imgaug)

    for obj, bbox_aug in zip(annotation_root.findall('object'), bboxes_aug.bounding_boxes):
        bbox = obj.find('bndbox')
        bbox.find('xmin').text = str(int(bbox_aug.x1))
        bbox.find('ymin').text = str(int(bbox_aug.y1))
        bbox.find('xmax').text = str(int(bbox_aug.x2))
        bbox.find('ymax').text = str(int(bbox_aug.y2))

    return image_aug, annotation_root

image_folder = 'C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/Mammiferes/Ecureuil'
annotation_folder = 'C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/annotation/Ecureuil'
output_images_folder = 'C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/augmentation_images/Ecureuil'
output_annotation_folder = 'C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/augmentation_annotation/Ecureuil' 
augment_dataset(image_folder, annotation_folder, output_images_folder,output_annotation_folder)

