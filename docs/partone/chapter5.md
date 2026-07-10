# AutoDoseRank: Automated Dosimetry-Informed Segmentation Ranking for Radiotherapy

This work was presented as an [oral talk](https://link.springer.com/chapter/10.1007/978-3-031-73376-5_21) at the [CaPTion Workshop at MICCAI 2024](https://caption-workshop.github.io/#Workshop%20sessions).

Radiotherapy planning for glioblastoma relies on carefully balancing tumour coverage against toxicity to the organs-at-risk (OARs). As deep-learning-based auto-segmentation takes over the manual contouring task, the role of clinicians is shifting from producing segmentations to supervising and correcting automated results. Ensuring the quality of these segmentations is critical, since errors in tumour delineation have been shown to make up to 25% of treatment plans non-compliant. Geometric measures such as the Dice Similarity Coefficient (DSC) and Hausdorff Distance (HD) are commonly used to assess segmentation quality, but they correlate poorly with either the dosimetric consequences of contouring errors or with clinician judgement.

In this work, we propose the first (to the best of our knowledge) dose-informed framework for ranking a set of segmentations, taking advantage of recent advances in deep-learning-based dose prediction. This dosimetric triage — termed **AutoDoseRank** (**Auto**mated **Do**simetry-informed **Se**gmentation **Rank**ing) — is based on (i) OAR-specific dose constraints and (ii) relative prioritization between OARs, effectively bringing knowledge from the subsequent radiotherapy planning step forward into segmentation quality assessment. Evaluated on 65 segmentations from 13 glioblastoma patients, AutoDoseRank outperformed three of four radiation oncologists in ranking contours by dosimetric quality, achieving a mean Kendall's Tau of 0.129 (close to the best expert at 0.148 and well above the worst at 0.014).

See [the project repository](https://github.com/amithjkamath/autodoserank) to reproduce these results.

## Citation

If you find this work useful, please cite it as:

    @inproceedings{mercado2024autodoserank,
    title={AutoDoseRank: Automated Dosimetry-Informed Segmentation Ranking for Radiotherapy},
    author={Mercado, Zahira and Kamath, Amith and Poel, Robert and Willmann, Jonas and Ermis, Ekin and Riggenbach, Elena and Mose, Lucas and Andratschke, Nicolaus and Reyes, Mauricio},
    booktitle={Cancer Prevention through Early Detection (CaPTion) Workshop, MICCAI 2024, Lecture Notes in Computer Science},
    pages={221--230},
    publisher={Springer Nature Switzerland},
    doi={10.1007/978-3-031-73376-5_21},
    year={2024}
    }
