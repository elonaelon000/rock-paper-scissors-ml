# Rock Paper Scissors ML

A group machine learning project using Google Teachable Machine to recognize three hand gestures: `rock`, `paper`, and `scissors`.

We used a group poll to divide responsibility for collecting images for each category:

| Team member | Image category |
| --- | --- |
| Elona | Rock |
| Klei | Paper |
| Sarita | Scissors |

Our training dataset included both AI-generated images and photos we took ourselves. We combined the collected images, organized them into the three classes, and used them to train the model in Teachable Machine.

## Model files

- [keras_model.h5](keras_model.h5): the trained model exported from Teachable Machine as TensorFlow / Keras.
- [labels.txt](labels.txt): output class names in the required order: `0 rock`, `1 paper`, `2 scissors`.
- [converted_keras.zip](converted_keras.zip): the same model and labels together.

Download the model and labels to the same folder to use them with TensorFlow / Keras. These are exported prediction files; they do not contain the original Teachable Machine training project.

## Image review

The original image collection contains paper objects, physical scissors, illustrations, and numbered rock images. These can introduce misleading features when training a hand-gesture classifier. The exported model has not yet been replaced following this review.

See [DATA_GUIDE.md](DATA_GUIDE.md) for the image review, the collection plan, and the steps to produce the corrected export. Repository image counts should not be reported as verified training counts.

[Project instructions](https://evisp.github.io/ml-handbook/projects/rock-paper-scissors/)
