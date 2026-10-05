# Model

This folder contains the exported Google Teachable Machine / TensorFlow Keras model used for Rock-Paper-Scissors classification.

## Files

- `keras_model.h5` — trained Keras model
- `labels.txt` — class names in model output order

## Verified Model Information

The supplied `keras_model.h5` was inspected directly:

- Input shape: `224 x 224 x 3`
- Number of output classes: `3`
- Keras export metadata: `2.4.0`

The supplied labels are:

```text
0 rock
1 paper
2 scissors
```

The model and labels must stay together because prediction index 0, 1, or 2 is interpreted using this exact label order.

If the training dataset changes substantially, retrain and export a new model rather than assuming this model represents the updated dataset.
