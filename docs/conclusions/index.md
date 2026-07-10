# 12. Conclusions

*"I was born not knowing and have had only a little time to change that here and there."*

— Richard Feynman, in What Do You Care What Other People Think?, 1988.

The findings presented in this thesis span three main areas: clinical validation (Part One), technical investigations (Part Two), and proof-of-concept demonstrations (Part Three). Together, they address key challenges in radiation therapy planning and contribute to progress in the field.

This chapter revisits the hypothesis and research questions introduced in Chapter 1. It provides a critical summary of the main findings, discusses their limitations, and reflects on their impact on clinical practice and future research. The guiding themes of this work are summarized.

> *Artificial Intelligence (AI)-based systems can standardize and automate fast and reliable dosimetric contour Quality Assurance (QA) in Radiotherapy (RT) planning.* 

Chapters 3 to 5 provide strong support for the central hypothesis and advance the field by aiming to *improve the precision, efficiency, and reliability of RT using advanced AI tools*. Through the integration of **dose-aware QA, predictive dosimetry, and robust model design**, this work lays the foundation for more efficient RT workflows, with the potential to enhance patient outcomes.

The overarching impact of these results can be summarized into:

**1. Standardizing Dosimetric Contour QA: shifting from geometry-based to clinically relevant metrics.**
A central finding of this work is the need to reduce inter-evaluator variability in contour assessment, as highlighted in Chapters 3 and 4. Manual contour errors contribute to up to 25% of non-compliant treatment plans. Deep Learning (DL) models assessed in the subsequent research chapters show strong performance in estimating the dosimetric impact of realistic Target Volume (TV) contour variations—matching or exceeding expert accuracy.

By focusing on dosimetric outcomes rather than geometric similarity, these tools support more objective and clinically aligned QA. This is important given the weak correlation between geometric metrics and treatment quality. These results support the development of RT QA workflows that prioritize clinical relevance and consistency over subjective judgement.

**2. Automating Workflows for Faster Planning: enabling real-time, dosimetry-informed QA that can exceed expert performance in specific tasks.**
Chapter 3 highlights the need for standardized, automated contour QA. Chapters 7 and 6 demonstrate that DL models can support this by reducing the burden of manual checks. These models enable near-instant predictions of dose changes from contour edits, helping clinicians assess trade-offs between tumour coverage and OAR sparing more efficiently.

This capability shortens the planning and review cycle—an important factor in reducing delays between diagnosis and treatment. Chapter 8 introduces Atomic Surface Transformations for Radiotherapy quality Assurance (ASTRA), the first dose-aware sensitivity map that directs clinicians to high-impact areas needing correction. Chapter 5 presents AutoDoseRank, which prioritizes urgent interventions, particularly relevant for aggressive cancers like glioblastoma.

Combining dose prediction with auto-contouring enhances planning precision and speed, supporting more personalized and efficient care. This is especially valuable in busy clinical settings, where planning delays can compromise outcomes.

**3. Robustness Testing of Architectures: evaluating design choices for reliable performance under clinical variability.**
Chapters 9, 10, and 11 examine segmentation model design, focusing on robustness across varied clinical settings. A key finding is that skip connections, while improving accuracy in controlled conditions, reduce robustness in Out Of Distribution (OOD) scenarios. This trade-off is critical in tumour segmentation, where imaging varies across scanners and patient conditions.

While models like Attention Gated U-Net (AGU-Net) and U-Net with multiple skip-connections (UNet++) may perform well in ideal settings, NoSkip architectures or those with addition-based skip connections (e.g., V-Net) offer better reliability. The results also highlight the role of dataset diversity—specifically, texture variation and foreground-background balance—in improving generalizability, as shown in frameworks like nnU-Net.

Computational efficiency is another factor; for example, UNet++ can be up to 100× slower to train. These insights support the development of adaptive, efficient, and texture-aware models that maintain accuracy while ensuring robustness in real-world clinical use.

The following sections present the key conclusions from the three core parts of this thesis (Parts One, Two, and Three), and explain how they address the research questions outlined in Chapter 1.

## Clinical Understanding and Needs Validation

Findings from Part One highlight the urgent need for automated and standardized dosimetric contour quality assessment. Chapter 3 quantifies inter-observer variability in this task, while Chapters 7 and 4 show that DL-based dose prediction models can support automation and improve consistency in evaluation.

> *Is there a need to standardize and automate dosimetric contour QA?* 

**A1:** What is the variability among radiation oncology professionals in contour quality assessment?

**Summary:** Chapter 3 explores this through a qualitative study involving four radiation oncologists and three medical physicists. They evaluated 54 glioblastoma target contour variations across 14 patients. The results showed **high variability** in assessments. Cohen’s Kappa values ranged from 0.33 to 0.74, indicating only fair to moderate agreement. Evaluators misclassified 46% of "no change" cases as "worse" and failed to identify any of the four "better" contours. Performance varied widely: the best evaluator achieved a precision of 0.63, recall of 0.65, and F1 score of 0.64, while the lowest scored 0.53, 0.43, and 0.35. These results confirm limited reliability in manual dosimetric contour assessment.

**Limitations:** The scoring system used in this study gave equal weight to all Organ at Risk (OAR)s, without considering their clinical importance. This may reduce the relevance of findings where high-priority structures are involved. The study focused only on glioblastoma, with data from 14 patients and seven evaluators from a single country, limiting generalizability to other tumour types or clinical settings. The small sample of evaluators may not reflect the full range of clinical practice. Finally, the study did not link contour assessments with clinical outcomes such as toxicity or Normalized Tissue Complication Probability (NTCP), which limits its ability to assess clinical impact.

**A2:** How can dosimetric criteria be systematically formulated to develop an automated systems to replicate their behaviour?

**Summary:** Chapter 4 explores this by using a DL-based dose prediction model, introduced in Chapter 7, to classify contour variations. The model was tested on 54 target volume variations from 14 brain tumour patients. **Dosimetric criteria were explicitly defined**: a variation was “Sub-optimal” if any OAR exceeded a 10% dose increase, “Improved” if the change was beneficial, and “No Impact” otherwise. These thresholds were tunable via parameters $\alpha$ (deviation threshold) and $n_{OAR}$ (number of affected organs), ensuring flexibility and clinical relevance.

The model outperformed three radiation oncologists, achieving a precision and recall of 0.57, slightly higher than the best expert. Confusion matrices showed better sensitivity in identifying “Sub-optimal” cases. These results demonstrate that automated, dosimetry-based evaluation is not only feasible but can also enhance human performance. The approach provides a replicable and efficient framework for contour QA, aligned with clinical priorities.

**Limitations:** The use of a fixed 10% dose threshold simplifies classification but may miss subtler or context-specific dose effects. Experts were not given formal definitions or dose distributions, which may have limited their performance and affected comparisons. The test set was small (54 variations from 14 Glioblastoma Multiforme (GBM) cases), limiting generalizability. The sensitivity study in Chapter 7 was also limited to simulated variations of a single OAR and did not include real inter-observer segmentations. Broader validation across tumour types, anatomical sites, and clinical scenarios is needed to confirm robustness and clinical utility.

## Technical Investigations and Analysis

Findings from Part Two demonstrate the potential of DL-based dose prediction models to improve treatment planning for glioblastoma using Volumetric Modulated Arc Therapy (VMAT). Chapters 6, 4, 8, and 5 show that these models enable real-time dosimetric contour evaluation due to their fast inference times. Chapters 9 and 11 further investigate the reliability of DL architectures, particularly for auto-contouring tasks.

> *How reliable and fast are AI-based systems for dosimetric contour QA?* 

**B1:** Do the predicted doses correlate better with the true dose differences compared to geometric metrics?

**Summary:** Chapters 7 and 6 provide strong quantitative evidence that DL-based dose predictors can accurately estimate dose changes from clinically relevant contour variations. Chapter 6 evaluated a cascaded 3D U-Net trained on 60 cases, and tested on 10 OOD scenarios. It achieved a dose error of 0.98 Gy and a mean Dose-Volume Histogram (DVH) error of 1.89 Gy. After fine-tuning on OOD data, dose error slightly improved to 0.97 Gy, with a small rise in DVH error to 2.03 Gy.

In Chapter 7, the same model was tested for sensitivity to expert variation in left optic nerve contours. It achieved a dose Mean Absolute Error (MAE) of 2.039 Gy, closely matching the ground truth MAE of 2.115 Gy. **A high correlation coefficient of 0.926 confirmed the model's accuracy in capturing dose changes**. These results suggest such models could reduce RT planning times, which currently average 9.63 days.

**Limitations:** Both studies are limited to glioblastoma cases using a single VMAT protocol and data from one institution, restricting generalizability. Model performance in other tumour types, modalities, or multi-centre settings remains untested. As a result, re-training may be necessary for each new clinical context, and the potential for a universal "foundation model" remains unproven.

No correlation was made between predicted dose changes and clinical outcomes such as toxicity or treatment efficacy. This limits the clinical relevance of the findings and reflects the lack of standardized, publicly available datasets and benchmarks. Additionally, only a cascaded 3D U-Net was evaluated. Alternative architectures were not compared, limiting insight into possible improvements in accuracy, interpretability, or efficiency, which is especially important for real-time clinical deployment.

**B2:** How reliable are the core DL architectures under difficult conditions?

**Summary:** Chapters 9, 10, and 11 examine the role of skip connections in U-Net-based architectures. While skip connections help preserve spatial detail for complex segmentation tasks, the findings show that advanced variants like AGU-Net and U-Net + Transformer Hybrid (UNETR) are **not consistently more robust** than standard U-Net models, particularly under distribution shifts.

Enhanced models perform well in clean conditions (e.g., AGU-Net: 0.795 on Breast US) but degrade more under perturbations (e.g., AGU-Net drops to 0.645 vs. NoSkipU-Net at 0.735). No-Skip models like NoSkipV-Net show better stability in harder settings, winning 78.3% of the most difficult Heart Magnetic Resonance Imaging (MRI) cases. Lower coefficient of variation scores (e.g., 0.20 for NoSkipV-Net vs. 0.35 for AGU-Net) further support this. Chapter 11 shows that UNETR and AGU-Net are highly sensitive to foreground-background ratio changes, with Dice Similarity Coefficient (DSC) drops of up to 0.369, compared to just 0.0139 for U-Net.

These results suggest that skip connections can amplify noise under domain shifts. However, larger patch sizes improve performance across architectures, indicating that global context remains valuable for complex segmentation tasks.

**Limitations:** The studies rely on synthetic or curated datasets with controlled perturbations, which do not fully reflect real-world clinical variability such as scanner differences, anatomical diversity, or multi-modal noise. The analysis is limited to U-Net variants, without testing broader architectures like transformer hybrids or alternative attention mechanisms. In addition, segmentation quality is measured using standard metrics (e.g., DSC, Hausdorff Distance (HD)), without linking performance to clinical outcomes or decision-making. This limits understanding of how robustness improvements impact actual clinical utility.

## Proofs of Concept Experiments

Part Three, through Chapters 8 and 5, presents initial proof-of-concept demonstrations showing how the advances from earlier chapters could be integrated into clinical applications.

> *What clinical systems can such dosimetric contour QA be integrated into?* 

**C1:** Can such models assist in focusing contour review efforts on locations where segmentation variations are dosimetrically most critical?

**Summary:** Chapter 8 introduces the novel ASTRA method, which enhances QA by generating sensitivity maps that highlight contour regions with the greatest dosimetric impact. By simulating over 2,000 local surface perturbations per subject, ASTRA quantifies the relationship between contour errors and dose differences (e.g., correlation of –0.76 for the left eye). Although based on synthetic perturbations rather than inter-expert variability, it represents the **first approach to produce local, dosimetry-informed heat maps** for guiding expert review.

**Limitations:** The study is limited to glioblastoma cases treated with VMAT using a single planning system, which restricts generalizability. Separate training is needed for different clinical setups, posing scalability challenges. The method does not assess whether sensitivity maps influence treatment decisions or clinical outcomes, such as toxicity or efficacy. ASTRA uses simplified, uniform perturbations that may not reflect real-world, anatomically constrained errors. Further validation is needed to compare estimated and true dose differences and to justify its clinical reliability.

**C2:** Can such models assist in dosimetrically ranking various auto-contour proposals?

**Summary:** Chapter 5 introduces AutoDoseRank, a method for ranking segmentations by dosimetric quality using a DL-based dose predictor and a novel dose impact metric. This metric incorporates OAR-specific constraints and priority weights (e.g., p("optic nerve") = 1, p("eye") = 8), and aggregates per-OAR scores into a patient-level ranking. Tested on 65 segmentations from 13 patients, AutoDoseRank outperformed three of four radiation oncologists, achieving a mean Kendall’s Tau of 0.129, close to the best expert (0.148) and well above the worst (0.014). This approach provides **a practical, dosimetry-driven method for ranking contours**.

**Limitations:** The study is limited to a small dataset of 13 GBM patients, which affects the statistical strength of the results. The method depends on a DL-based dose predictor, and any errors in dose estimation could bias the rankings. The impact of prediction uncertainty on ranking reliability is not quantified. Additionally, the clinical utility of AutoDoseRank remains untested. Its effects on decision-making, correction time, or treatment quality are not evaluated, leaving its real-world benefits uncertain.

$ {\ast}\,{\ast}\,{\ast} $

The research presented across Parts One, Two, and Three provides strong evidence supporting the hypothesis that AI-based systems can reliably and efficiently standardize and automate dosimetric contour QA in RT planning. Building on these findings, Chapter 13 outlines future directions to advance this field further.
