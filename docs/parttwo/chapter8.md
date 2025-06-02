# ASTRA: Atomic Surface Transformations for Radiotherapy Quality Assurance

This is a WIP (Work-In-Progress): this message will be removed once sufficient progress has been made. 

[![2 minute video abstract](https://img.youtube.com/vi/vghlJh8ACOY/0.jpg)](https://www.youtube.com/watch?v=vghlJh8ACOY)

(click on the picture above to watch a 2 minute video describing this research)

Treatment for glioblastoma, an aggressive brain tumour usually relies on radiotherapy. This involves planning how to achieve the desired radiation dose distribution, which is known as treatment planning. Treatment planning is impacted by human errors, inter-expert variability in segmenting (or outlining) the tumor target and organs-at-risk, and differences in segmentation protocols. Erroneous segmentations translate to erroneous dose distributions, and hence sub-optimal clinical outcomes. Reviewing segmentations is time-intensive, significantly reduces the efficiency of radiation oncology teams, and hence restricts timely radiotherapy interventions to limit tumor growth. Moreover, to date, radiation oncologists review and correct segmentations without information on how potential corrections might affect radiation dose distributions, leading to an ineffective and suboptimal segmentation correction workflow. 

In this paper, we introduce an automated deep-learning based method: atomic surface transformations for radiotherapy quality assurance (ASTRA), that predicts the potential impact of local segmentation variations on radiotherapy dose predictions, thereby serving as an effective dose-aware sensitivity map of segmentation variations. On a dataset of 100 glioblastoma patients, we show how the proposed approach enables assessment and visualization of areas of organs-at-risk being most susceptible to dose changes, providing clinicians with a dose-informed mechanism to review and correct segmentations for radiation therapy planning. 

These initial results suggest strong potential for employing such methods within a broader automated quality assurance system in the radiotherapy planning workflow.

See [the project repository](https://github.com/amithjkamath/astra) to reproduce these results.

## Citation

If you find this work useful, please cite it as:

    @inproceedings{kamath2023astra,
    title={ASTRA: Atomic Surface Transformations for Radiotherapy quality Assurance},
    author={Kamath, Amith and Poel, Robert and Willmann, Jonas and Ermis, Ekin and Andratschke, Nicolaus and Reyes, Mauricio},
    booktitle={45th IEEE Engineering in Medicine and Biology Conference (EMBC)},
    year={2023}
    }