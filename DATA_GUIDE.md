# Collecting and checking the hand-gesture dataset

## Review of the original collection

| Location | Files found | Review finding |
| --- | ---: | --- |
| `data/rock/rock_dataset_70.zip` | 70 images | Fists, with numbers printed in image corners. Replace with unnumbered hand photos for the corrected training run. |
| `paper dataset.zip` | 50 images | Mixed collection: sheets of paper, illustrations, and hand photos. Do not upload the entire archive as the paper class. |
| `photo scissors/` | 50 images | Mixed collection: physical scissors, illustrations, and hand gestures. Do not upload the entire folder as the scissors class. |

These are repository counts, not confirmed counts from the Teachable Machine training session. The exported model does not establish which source photos were used. Preserve the original files as a record of the first attempt; use a separate corrected dataset for the next training run.

## Collection plan — to carry out

The poll assigns responsibility for organizing each category: Elona organizes rock, Klei organizes paper, and Sarita organizes scissors. Everyone contributes all three gestures.

| Contributor | rock | paper | scissors |
| --- | ---: | ---: | ---: |
| Elona | 20 | 20 | 20 |
| Klei | 20 | 20 | 20 |
| Sarita | 20 | 20 | 20 |
| Total | 60 | 60 | 60 |

- `rock`: a closed fist.
- `paper`: an open hand with extended fingers.
- `scissors`: index and middle fingers extended in a V; remaining fingers folded.
- Take 10 photos of each gesture in one setting and 10 of each in a second setting.
- Include left and right hands, different angles, distances, backgrounds, and lighting.
- Use the same settings for all three gestures so that backgrounds do not identify a class.
- Keep the whole gesture visible. Exclude faces, physical scissors, sheets of paper, cartoons, numbers, captions, and watermarks.
- Review every image and replace blurry, ambiguous, or incorrectly labeled examples. Keep at least 50 suitable training images per class.
- Agree on public sharing before uploading personal photos. Do not claim that consent was obtained until each person has actually agreed.

For photo files, each person can prepare three folders named `rock`, `paper`, and `scissors`, then upload a ZIP here for checking. Include the contributor's name in filenames to prevent files from overwriting one another.

## Record the data statement before collecting the new photos

Write what is being collected, whose hands appear, where the images will be stored, and whether each participant is comfortable with public sharing and why. Record actual agreement. Keep the original dataset and the corrected collection distinguishable; do not describe a new statement as if it preceded the first collection.

## Train and export the corrected model

1. Save a backup of the original Teachable Machine project if it is still open.
2. Start an Image Project with a Standard image model.
3. Create the classes in this exact order: `rock`, `paper`, `scissors`.
4. Upload only the reviewed hand-gesture images to the corresponding classes.
5. Record the actual training count per class and take a screenshot of the class list.
6. Click **Train Model**.
7. Try new photos or live gestures in different conditions, including someone not represented in the training images. Record a correct prediction and a confidently wrong one with their confidence scores.
8. Export using **Tensorflow → Keras → Download my model**.
9. Check that `labels.txt` contains:
   ```text
   0 rock
   1 paper
   2 scissors
   ```
10. Replace `keras_model.h5`, `labels.txt`, and `converted_keras.zip` together with the new export. Upload the corrected public photo collection and identify its folder in the README.
11. Update the README with the actual collection details and screenshots. Keep descriptions accurate about any AI-generated or externally sourced images that were actually used.

Updating GitHub photos alone does not change the exported model. A new training run and export are required.

## Testing and the completed report

The professor's requested Keras files allow the trained model to be tested. The full handbook report also requires the external group's confusion matrix and accuracy, the worst confident failure, and 3–5 sentences explaining what the model learned. Add these from actual observations when the group test happens.

For the other group's test, collect 30 separate images: 10 rock, 10 paper, and 10 scissors, using your group's hands in a different location or on another day. Keep these out of training.

[Assignment](https://evisp.github.io/ml-handbook/projects/rock-paper-scissors/)
