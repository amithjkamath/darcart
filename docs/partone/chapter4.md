# Comparing the Performance of Radiation Oncologists versus a Deep Learning Dose Predictor to Estimate Dosimetric Impact of Segmentation Variations for Radiotherapy

This is a WIP (Work-In-Progress): this message will be removed once sufficient progress has been made.

[![Oral talk at MIDL 2024:](https://img.youtube.com/vi/Co9yUIAw6H0/0.jpg)](https://youtu.be/Co9yUIAw6H0?t=3587)

Current evaluation methods for quality control of manual/automated tumor and organs-at- risk segmentation for radiotherapy are driven mostly by geometric correctness. It is however known that geometry-driven segmentation quality metrics cannot characterize potentially detrimental dosimetric effects of sub-optimal tumor segmentation. 

In this work, we build on prior studies proposing deep learning-based dose prediction models to extend its use for the task of contour quality evaluation of brain tumor treatment planning. Using a test set of 54 contour variants and their corresponding dose plans, we show that our model can be used to dosimetrically assess the quality of contours and can outperform clinical expert radiation oncologists while estimating sub-optimal situations. 

We compare results against three such experts and demonstrate improved accuracy in addition to time savings.

See [the project repository](https://github.com/ubern-mia/radonc-vs-dldp) to reproduce these results.

## Citation

If you find this work useful, please cite it as:

    @inproceedings{kamath2024radoncvsdldp,
    title={Comparing the Performance of Radiation Oncologists versus a Deep Learning Dose Predictor to Estimate Dosimetric Impact of Segmentation Variations for Radiotherapy},
    author={Kamath, Amith and Mercado, Zahira and Poel, Robert and Willmann, Jonas and Ermis, Ekin and Riggenbach, Elena and Andratschke, Nicolaus and Reyes, Mauricio},
    booktitle={Medical Imaging with Deep Learning},
    year={2024}
    }