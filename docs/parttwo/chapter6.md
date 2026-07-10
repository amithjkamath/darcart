# Deep-learning-based dose predictor for glioblastoma–assessing the sensitivity and robustness for dose awareness in contouring

This work was [published](https://www.mdpi.com/2072-6694/15/17/4226) in the journal [Cancers](https://www.mdpi.com/journal/cancers) (impact factor 4.5).

**Read the paper:** [Publisher (Cancers / MDPI)](https://doi.org/10.3390/cancers15174226) · [Google Scholar](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=clej42kAAAAJ&citation_for_view=clej42kAAAAJ:vV6vV6tmYwMC)

External beam radiation therapy requires a sophisticated and laborious planning procedure. To improve the efficiency and quality of this procedure, machine-learning models that predict these dose distributions were introduced. The most recent dose prediction models are based on deep-learning architectures called 3D U-Nets that give good approximations of the dose in 3D almost instantly. Our purpose was to train such a 3D dose prediction model for glioblastoma VMAT treatment and test its robustness and sensitivity for the purpose of quality assurance of automatic contouring.

From a cohort of 125 glioblastoma (GBM) patients, VMAT plans were created according to a clinical protocol. The initial model was trained on a cascaded 3D U-Net. A total of 60 cases were used for training, 15 for validation and 20 for testing. The prediction model was tested for sensitivity to dose changes when subject to realistic contour variations. Additionally, the model was tested for robustness by exposing it to a worst-case test set containing out-of-distribution cases.

The initially trained prediction model had a dose score of 0.94 Gy and a mean DVH (dose volume histogram) score for all structures of 1.95 Gy. In terms of sensitivity, the model was able to predict the dose changes that occurred due to the contour variations with a mean error of 1.38 Gy. We obtained a 3D VMAT dose prediction model for GBM with limited data, providing good sensitivity to realistic contour variations. We tested and improved the model's robustness by targeted updates to the training set, making it a useful technique for introducing dose awareness in the contouring evaluation and quality assurance process.

This journal work extends the conference study in [Chapter 7](chapter7.md); see [the project repository](https://github.com/amithjkamath/deepdosesens) for the supporting code.

## Citation

If you find this work useful, please cite it as:

    @article{poel2023deepdosepredictor,
    title={Deep-Learning-Based Dose Predictor for Glioblastoma--Assessing the Sensitivity and Robustness for Dose Awareness in Contouring},
    author={Poel, Robert and Kamath, Amith J. and Willmann, Jonas and Andratschke, Nicolaus and Ermis, Ekin and Aebersold, Daniel M. and Manser, Peter and Reyes, Mauricio},
    journal={Cancers},
    volume={15},
    number={17},
    pages={4226},
    publisher={MDPI},
    doi={10.3390/cancers15174226},
    year={2023}
    }
