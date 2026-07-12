# Dose-Aware and Robust Contour QA for Radiotherapy

This site presents the PhD thesis of Amith Kamath, carried out at the ARTORG Center for Biomedical Engineering Research and the Medical Image Analysis Lab at the University of Bern.

## Overview

Radiotherapy planning relies heavily on accurate anatomical contouring, and the quality assurance (QA) of those contours is central to the effectiveness of treatment. Yet the geometric metrics traditionally used to check contours — overlap scores such as the Dice coefficient — correlate poorly with the delivered dose distribution, and therefore with patient outcomes. This thesis works towards **dose-aware contour QA**: evaluating a contour by its clinical, dosimetric consequences rather than its pixel-wise overlap.

It tests the hypothesis that fast, dose-aware AI can make contour QA more consistent and clinically meaningful, provided that the dose-prediction and segmentation components are sensitive to consequential contour variations and robust to distribution shifts. The chapters build that case in three connected steps: first establishing the clinical need and testing automated assessment, then evaluating dose-prediction sensitivity and robustness, and finally examining the robustness of the segmentation architectures these tools depend on. Two proof-of-concept tools are embedded where they arise in that progression: **AutoDoseRank** in Part One ranks candidate segmentations by dosimetric quality, while **ASTRA** in Part Two produces local dose-sensitivity maps for contour review.

## What's inside

The work is organized by theme, in three parts:

- **[Part One — Dosimetric Awareness of Radiation Oncology Professionals (Chapters 3–5)](partone/index.md)** shows, through a survey and a head-to-head comparison, that experts struggle to judge the dosimetric impact of contour changes and that a deep-learning dose predictor can outperform them, culminating in *AutoDoseRank*.
- **[Part Two — Sensitivity of Dose Prediction Models (Chapters 6–8)](parttwo/index.md)** examines whether the underlying dose predictors are accurate, sensitive to realistic contour variation, robust to unusual cases, and fast enough for review, then turns that sensitivity into *ASTRA*.
- **[Part Three — Robustness of Segmentation Models (Chapters 9–11)](partthree/index.md)** studies how U-Net design and data choices — including skip connections, task complexity, texture, context, and foreground ratio — affect robustness under distribution shift.

New readers may want to start with the [Introduction](intro/index.md) for the clinical motivation, or the [Background](background/index.md) for a primer on the radiotherapy workflow and the AI methods used throughout. The [Conclusions](conclusions/index.md) revisit the central hypothesis across all three parts, and every claim is backed by a linked [reference](references/index.md).

```{toctree}
:maxdepth: 2
:caption: Contents
intro/index
background/index
partone/index
parttwo/index
partthree/index
conclusions/index
references/index
```
