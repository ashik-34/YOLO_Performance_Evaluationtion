# YOLO_Performance_Evaluationtion
Code for "Performance Evaluation of YOLOv8 to YOLOv12 for Safety Helmet Detection on Weather-Augmented Images"
This repository contains the code and instructions for the paper "Performance Evaluation of YOLOv8 to YOLOv12 for Safety Helmet Detection on Weather-Augmented Images". The experiments focus on testing YOLO models (v8 to v12) on A100 and T4 GPUs for real-time safety helmet detection on construction sites.

## Project Description
This project implements and evaluates the YOLOv12 model (along with earlier versions) for detecting safety helmets and persons in images. The code provided here is specifically for experiments conducted on a T4 GPU, optimized for performance and efficiency. Preprocessing scripts and the main experiment notebook are included to ensure reproducibility.

## Dataset
The dataset used in this project is the "Safety-Helmet-Wearing-Dataset," which is publicly available. It can be downloaded from: njvisionpower, "Safety-Helmet-Wearing-Dataset," GitHub, 2019. [Online]. Available: https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset. [Accessed: Jul. 7, 2025].

#### Dataset Preparation
Since the dataset is not included in this repository, follow these steps to download and prepare it:

#### 1. Download the Dataset: 

Clone the dataset repository: git clone https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset.git


The dataset is provided in VOC format with images and XML annotations.


#### 2. Convert VOC to YOLO Format:

Use the provided convert_voc_to_yolo.py script to convert VOC annotations to YOLO format.
Update the dataset_dir path in the script to point to your local dataset folder, then run the convert_voc_to_yolo.py script. 


This will create a YOLOLabels folder with .txt files in YOLO format.


#### 3. Augment the Dataset:

Use the augment_with_boxes.py script to apply augmentations (e.g., fog, rain, blur, brightness, darkness) to the images and copy their labels.
Update the input and output paths in the script as needed, then run:python processing/augment_with_boxes.py


This generates augmented images and labels in VOC2028_Augmented/.


#### 4. Organize the Dataset:

Use the organize_dataset.py script to split the dataset into train, validation, and test sets (70%, 15%, 15% by default).
Update the paths in the script to point to your augmented dataset, then run:python processing/organize_dataset.py


This creates a YOLODataset/ folder with subdirectories train/, val/, and test/, each containing images/ and labels/.


#### 5. Upload to Google Drive:

Upload the YOLODataset/ folder to your Google Drive.
Create a data.yaml file in YOLODataset/ with the following content, adjusting paths to match your Google Drive structure:train: /content/drive/MyDrive/YOLODataset/train/images
val: /content/drive/MyDrive/YOLODataset/val/images
test: /content/drive/MyDrive/YOLODataset/test/images
nc: 2
names: ["hat", "person"]





## Installation

Clone the Repository:
git clone https://github.com/yourusername/Safety-Helmet-Detection-YOLOv12-Conference2025.git
cd Safety-Helmet-Detection-YOLOv12-Conference2025


Install Dependencies:

Ensure you have Python 3.8 or later installed.
Install the required packages:pip install -r requirements.txt




Set Up Google Colab:

Open the code/YOLOv8_12m_Tested_on_T4.ipynb notebook in Google Colab.
Mount your Google Drive in Colab to access the dataset:from google.colab import drive
drive.mount('/content/drive')





## Usage

Run the Experiment:

In Google Colab, open code/YOLOv8_12m_Tested_on_T4.ipynb.
Update the DATASET_PATH and SAVE_DIR variables in the notebook to match your Google Drive paths.
Run all cells to test YOLOv8m to YOLOv12m models on the T4 GPU using the test split of the dataset.


Trained Models:

The trained models are not included in this repository. To use the pre-trained weights, you need to train the models using the provided code or download them from [source if applicable].
Ensure that the paths to the model weights in the notebook are updated to point to your trained models.


Results:

Metrics (precision, recall, mAP, FPS, model size) will be saved in the UpdatedMetrices/ directory on your Google Drive as .txt files and a summary CSV (YOLO_T4_Benchmark_Comparison.csv).
A comparison chart (balance_map50_95_vs_fps.png) will also be generated.



## Citation
If you use this code or dataset in your research, please cite our paper:
[Your Paper Title], International Conference on Computer Vision and Machine Learning 2025.
Source code available at: https://github.com/yourusername/Safety-Helmet-Detection-YOLOv12-Conference2025

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or feedback, please open an issue on this repository or contact [your email].
