# Dataset Notes

## Final class counts

- Rock: 50 images
- Paper: 50 images
- Scissors: 53 images
- Total: 153 images

## Cleaning

The original paper collection contained literal sheets of paper, paper textures, icons, illustrations, and other examples that could teach the model the wrong visual concept. Those examples were removed from the cleaned dataset.

The retained paper source images show an open-hand gesture. To reach a 50-image paper class without reintroducing incorrect examples, mild augmentation was applied to the reviewed open-hand images. The transformations include horizontal flipping, small rotations, brightness/contrast changes, and mild crop/resize operations.

Rock and scissors were reviewed as gesture classes and organized with consistent filenames.

## Dataset design goal

The classifier should learn the **shape of the hand gesture**, not a literal rock, sheet of paper, pair of scissors, caption, watermark, or class-specific background.

For future improvement, the best next step is to collect more unique real open-hand photos from different people, angles, distances, lighting conditions, and backgrounds, then replace augmented paper examples with those new originals.
