import os
import random
import shutil
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import cv2

# Define paths
original_images_dir = 'VOC2028/JPEGImages'
original_labels_dir = 'VOC2028/YOLOLabels'
output_images_dir = 'VOC2028_Augmented/JPEGImages'
output_labels_dir = 'VOC2028_Augmented/YOLOLabels'

os.makedirs(output_images_dir, exist_ok=True)
os.makedirs(output_labels_dir, exist_ok=True)

# Augmentation functions

def apply_fog(img):
    fog = Image.new('RGB', img.size, (255, 255, 255))
    return Image.blend(img, fog, 0.25)


def apply_rain(img):
    img_cv = np.array(img)
    rain_layer = np.zeros_like(img_cv, dtype=np.uint8)
    num_drops = 300

    for _ in range(num_drops):
        x = random.randint(0, img_cv.shape[1])
        y = random.randint(0, img_cv.shape[0])
        length = random.randint(8, 12)  # shorter streaks
        thickness = 1  # thinner
        color = (random.randint(170, 210),) * 3
        angle = random.uniform(-0.2, 0.2)

        x_end = int(x + length * np.sin(angle))
        y_end = int(y + length * np.cos(angle))

        cv2.line(rain_layer, (x, y), (x_end, y_end), color, thickness)

    rain_layer = cv2.blur(rain_layer, (3, 3))  # soft blur
    blended = cv2.addWeighted(img_cv, 0.9, rain_layer, 0.2, 0)
    return Image.fromarray(blended)


def apply_blur(img):
    return img.filter(ImageFilter.GaussianBlur(radius=2.5))


def apply_brightness(img):
    return ImageEnhance.Brightness(img).enhance(1.5)

def apply_darkness(img):
    return ImageEnhance.Brightness(img).enhance(0.5)


augmentation_funcs = [None, apply_fog, apply_rain, apply_blur, apply_brightness, apply_darkness]

# Load image list
image_filenames = [f[:-4] for f in os.listdir(original_images_dir) if f.lower().endswith('.jpg')]
image_filenames.sort()
random.shuffle(image_filenames)

# Balanced distribution
num_images = len(image_filenames)
images_per_aug = num_images // 6

# Apply one augmentation per image
output_count = 0
for idx, base_filename in enumerate(image_filenames):
    img_path = os.path.join(original_images_dir, base_filename + '.jpg')
    label_path = os.path.join(original_labels_dir, base_filename + '.txt')

    if not os.path.exists(img_path) or not os.path.exists(label_path):
        continue

    img = Image.open(img_path).convert('RGB')

    # Determine augmentation type
    aug_type = idx // images_per_aug
    if aug_type > 5:  # edge case for remainder
        aug_type = 5

    aug_func = augmentation_funcs[aug_type]
    if aug_func:
        img = aug_func(img)

    new_img_name = f"{output_count:06}.jpg"
    new_label_name = f"{output_count:06}.txt"

    img.save(os.path.join(output_images_dir, new_img_name))
    shutil.copy(label_path, os.path.join(output_labels_dir, new_label_name))

    output_count += 1

print(f"✅ Augmented dataset created with {output_count} images (one per original).")
