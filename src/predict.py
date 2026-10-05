#!/usr/bin/env python3
"""Run Rock-Paper-Scissors prediction on one image."""

import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model


def load_labels(path):
    """Return class names from a Teachable Machine labels file."""
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip().split(" ", 1)[-1] for line in file if line.strip()]


def predict(image_path):
    """Predict the class of one image and return label and confidence."""
    root = Path(__file__).resolve().parents[1]
    model_path = root / "model" / "keras_model.h5"
    labels_path = root / "model" / "labels.txt"

    model = load_model(model_path, compile=False)
    labels = load_labels(labels_path)

    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    data = np.asarray(image).astype(np.float32)
    data = (data / 127.5) - 1
    data = np.expand_dims(data, axis=0)

    prediction = model.predict(data, verbose=0)[0]
    index = int(np.argmax(prediction))
    return labels[index], float(prediction[index])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python src/predict.py path/to/image.jpg")

    label, confidence = predict(sys.argv[1])
    print(f"Prediction: {label}")
    print(f"Confidence: {confidence:.2%}")
