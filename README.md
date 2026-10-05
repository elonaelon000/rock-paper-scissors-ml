# Rock Paper Scissors ML

This repository contains a cleaned image dataset and a trained model for **Rock-Paper-Scissors hand gesture classification**.

The project was developed using **Google Teachable Machine** and exported as a **TensorFlow / Keras** model.

## Table of Contents

1. [Dataset](#1-dataset)
2. [Dataset Diversity](#2-dataset-diversity)
3. [Data Cleaning and Augmentation](#3-data-cleaning-and-augmentation)
4. [Model](#4-model)
5. [Project Workflow](#5-project-workflow)
6. [Team](#6-team)
7. [Repository Structure](#7-repository-structure)
8. [Running a Prediction](#8-running-a-prediction)

## 1. Dataset

The dataset contains three hand-gesture classes:

- **Rock** — closed fist
- **Paper** — open hand
- **Scissors** — index and middle fingers extended in a V shape

### 1.1 Final Dataset

| Class | Number of Images |
| --- | ---: |
| Rock | 50 |
| Paper | 50 |
| Scissors | 53 |
| **Total** | **153** |

The final dataset is organized so that each class represents the **hand gesture itself**, rather than the literal object associated with the game.

## 2. Dataset Diversity

The image collection includes visual variation intended to help the model generalize beyond one specific hand or environment.

The dataset contains differences in:

- hand position and orientation
- camera angle and distance
- lighting conditions
- backgrounds
- skin tones and hand appearance
- sleeves and accessories
- left and right hand presentation

The goal is to reduce the chance that the model learns a specific background or visual shortcut instead of the actual gesture.

## 3. Data Cleaning and Augmentation

The original image collection was reviewed before organizing the final dataset.

### 3.1 Cleaning

Incorrect or misleading examples were removed.

In particular, the **Paper** class originally contained examples such as literal sheets of paper, graphics, icons, and other non-gesture images. These were removed so that the class represents an **open-hand gesture** consistently.

The Rock and Scissors collections were also reviewed to keep the classes focused on hand gestures.

### 3.2 Paper Augmentation

After cleaning, the valid Paper class contained fewer images than required.

To reach a balanced class size of **50 Paper images**, mild augmentation was applied to reviewed open-hand images.

The augmentation included variations such as:

- horizontal flipping
- small rotations
- brightness adjustment
- contrast adjustment
- mild crop and resize changes

The purpose of augmentation was to increase variation without changing the meaning of the gesture.

More details are available in [docs/DATASET.md](docs/DATASET.md).

## 4. Model

The final model was exported from **Google Teachable Machine** in TensorFlow / Keras format.

### 4.1 Model Information

| Property | Value |
| --- | --- |
| Input size | 224 × 224 × 3 |
| Number of classes | 3 |
| Model format | Keras H5 |
| Model file | `model/keras_model.h5` |
| Labels file | `model/labels.txt` |

The model uses the following class order:

```text
0 rock
1 paper
2 scissors
```

The model and labels should always be kept together because the output index is interpreted using this exact order.

## 5. Project Workflow

The project follows this process:

1. Collect images for Rock, Paper, and Scissors.
2. Review the dataset and remove misleading examples.
3. Organize images into three class folders.
4. Apply limited augmentation where needed.
5. Train the image classifier in Google Teachable Machine.
6. Export the trained model as a Keras model.
7. Use the exported model to classify new hand-gesture images.

## 6. Team

Responsibility for the image classes was divided between the group members.

| Team Member | Main Responsibility |
| --- | --- |
| Elona Tarja | Rock dataset and repository organization |
| Klei Laboti | Paper dataset |
| Sarita Koci | Scissors dataset |

The group combined the collected images into one dataset and used the three classes to train the final model.

## 7. Repository Structure

```text
rock-paper-scissors-ml/
├── README.md
├── requirements.txt
├── data/
│   ├── rock_dataset.zip
│   ├── paper_dataset.zip
│   └── scissors_dataset.zip
├── dataset/
│   ├── rock/
│   ├── paper/
│   └── scissors/
├── model/
│   ├── keras_model.h5
│   ├── labels.txt
│   └── README.md
├── results/
├── src/
│   └── predict.py
└── docs/
    └── DATASET.md
```

- `data/` contains compressed source dataset archives.
- `dataset/` contains the cleaned class structure used for the project.
- `model/` contains the trained model and class labels.
- `src/` contains prediction code.
- `results/` is reserved for evaluation outputs such as confusion matrices, accuracy summaries, and test examples.
- `docs/` contains additional dataset documentation.

## 8. Running a Prediction

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run the prediction script with an image:

```bash
python src/predict.py path/to/image.jpg
```

The script outputs the predicted class and its confidence score.

## Project Goal

The main goal of this project is to build a classifier that recognizes the **Rock-Paper-Scissors hand gesture itself**, rather than relying on literal objects, text, watermarks, or class-specific backgrounds.
