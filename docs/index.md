# Dose-Aware and Robust Contour Assessment for RT (DARCART)

This site presents the PhD thesis of Amith Kamath, carried out at the ARTORG Center for Biomedical Engineering Research and the Medical Image Analysis Lab at the University of Bern.

## Overview

Radiotherapy planning relies heavily on accurate anatomical contouring, and the quality assurance (QA) of those contours is central to the effectiveness of treatment. Yet the geometric metrics traditionally used to check contours — overlap scores such as the Dice coefficient — correlate poorly with the delivered dose distribution, and therefore with patient outcomes. This thesis works towards **dose-aware contour QA**: evaluating a contour by its clinical, dosimetric consequences rather than its pixel-wise overlap.

It builds that case in three connected steps: first establishing the clinical need for dosimetry-grounded QA, then assessing whether automated dose-prediction tools are fast, sensitive, and robust enough to support it, and finally examining the segmentation architectures these tools depend on. Along the way it develops two proof-of-concept tools — **ASTRA**, which produces local dose-sensitivity maps for real-time contour review, and **AutoDoseRank**, which ranks candidate segmentations by their clinical impact. Together these contributions argue for a shift from purely geometric to clinically meaningful contour evaluation, laying groundwork for intelligent QA in the next generation of treatment planning.

## What's inside

The work is organized by theme, in three parts:

- **[Part One — Dosimetric Awareness of Radiation Oncology Professionals](partone/index.md)** shows, through a survey of clinicians and a head-to-head comparison, that experts struggle to judge the dosimetric impact of contour changes and that a deep-learning dose predictor can match or beat them — culminating in *AutoDoseRank*, a dosimetry-informed way to rank contours.
- **[Part Two — Sensitivity of Dose Prediction Models](parttwo/index.md)** examines whether the underlying dose predictors are accurate, sensitive to realistic contour variation, and fast enough for review, and turns that sensitivity into *ASTRA*, a dose-aware map of where a contour edit matters most.
- **[Part Three — Robustness of Segmentation Models](partthree/index.md)** looks beneath these models at the U-Net architectures they rely on, and asks how design choices such as skip connections affect robustness under real-world distribution shifts.

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
