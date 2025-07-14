import os
import shutil
import random

def split_dataset(image_dir, label_dir, output_base, train_ratio=0.7, val_ratio=0.15):
    images = [f for f in os.listdir(image_dir) if f.endswith(".jpg") or f.endswith(".png")]
    random.shuffle(images)

    train_cutoff = int(len(images) * train_ratio)
    val_cutoff = int(len(images) * (train_ratio + val_ratio))

    splits = {
        "train": images[:train_cutoff],
        "val": images[train_cutoff:val_cutoff],
        "test": images[val_cutoff:]
    }

    for split in splits:
        img_out = os.path.join(output_base, split, "images")
        lbl_out = os.path.join(output_base, split, "labels")
        os.makedirs(img_out, exist_ok=True)
        os.makedirs(lbl_out, exist_ok=True)

        for file in splits[split]:
            shutil.copy(os.path.join(image_dir, file), os.path.join(img_out, file))
            label_file = file.replace(".jpg", ".txt").replace(".png", ".txt")
            shutil.copy(os.path.join(label_dir, label_file), os.path.join(lbl_out, label_file))

# Run this
split_dataset(
    image_dir="VOC2028_Augmented/JPEGImages",
    label_dir="VOC2028_Augmented/YOLOLabels",
    output_base="YOLODataset",
    train_ratio=0.7,
    val_ratio=0.15
)