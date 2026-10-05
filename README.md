# Rock Paper Scissors ML

A machine learning project for classifying **rock**, **paper**, and **scissors** hand gestures from images.

The project uses a custom image dataset together with a Teachable Machine / Keras model workflow.

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

The dataset is organized around hand gestures rather than literal objects. The paper class was cleaned so literal sheets of paper and unrelated graphics were removed.

## Team

| Team member | Main responsibility |
| --- | --- |
| Elona Tarja | Rock dataset / repository organization |
| Klei Laboti | Paper dataset |
| Sarita Koci | Scissors dataset |

## Workflow

1. Collect and organize images into three gesture classes.
2. Review the dataset for misleading examples.
3. Train an image classification model in Google Teachable Machine.
4. Export the final TensorFlow / Keras model.
5. Keep model files in `model/`.
6. Test with unseen images.
7. Store evaluation outputs in `results/`.

## Classes

- **Rock** — closed fist
- **Paper** — open hand
- **Scissors** — index and middle fingers extended in a V shape

## Notes

This repository keeps the dataset, model export, evaluation results, and inference code separate so the project is easy to inspect and reproduce.
