# Rock Paper Scissors ML

A machine learning project for classifying **rock**, **paper**, and **scissors** hand gestures from images.

The project uses a cleaned custom image dataset and a Google Teachable Machine / TensorFlow Keras model.

## Project Structure

```text
rock-paper-scissors-ml/
├── README.md
├── requirements.txt
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

## Dataset

| Class | Images |
| --- | ---: |
| Rock | 50 |
| Paper | 50 |
| Scissors | 53 |
| **Total** | **153** |

The dataset is organized around **hand gestures**, not literal objects. The paper class was cleaned so sheets of paper, icons, and unrelated graphics were removed. Mild augmentation was used only to bring the reviewed open-hand paper class to 50 images.

## Model

The supplied Teachable Machine Keras model was inspected and matches the project setup:

- Input shape: **224 × 224 × 3**
- Output classes: **3**
- Label order: **rock, paper, scissors**
- Model file: `model/keras_model.h5`
- Labels file: `model/labels.txt`

The labels are:

```text
0 rock
1 paper
2 scissors
```

## Team

| Team member | Main responsibility |
| --- | --- |
| Elona Tarja | Rock dataset / repository organization |
| Klei Laboti | Paper dataset |
| Sarita Koci | Scissors dataset |

## Workflow

1. Collect images for the three gesture classes.
2. Review and clean misleading examples.
3. Organize the final dataset by class.
4. Train the classifier in Google Teachable Machine.
5. Export the TensorFlow / Keras model.
6. Test the model on unseen images.
7. Store evaluation outputs in `results/`.

## Classes

- **Rock** — closed fist
- **Paper** — open hand
- **Scissors** — index and middle fingers extended in a V shape

## Run a Prediction

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python src/predict.py path/to/image.jpg
```

The script prints the predicted class and confidence.

## Dataset Notes

See [docs/DATASET.md](docs/DATASET.md) for the cleaning and augmentation notes.

## Project Goal

The goal is to train a model that recognizes the **gesture itself** rather than learning shortcuts from literal objects, text, watermarks, or class-specific backgrounds.
