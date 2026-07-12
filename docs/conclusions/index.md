# 12. Conclusions

*"I was born not knowing and have had only a little time to change that here and there."*

— Richard Feynman, in What Do You Care What Other People Think?, 1988.

This work set out to test a single central hypothesis:

> *Fast, dose-aware AI systems can make contour quality assurance (QA) in radiotherapy planning more consistent and clinically meaningful, provided that their dose-prediction and segmentation components are sensitive to consequential contour variations and robust to distribution shifts.*

The chapters that precede this one build the case for that hypothesis in three parts, organized by theme rather than by technology-readiness level. [Part One](../partone/index.md) asks whether there is a real clinical need for dose-aware contour QA and shows how far automated dose prediction can already go towards meeting it. [Part Two](../parttwo/index.md) examines whether the dose-prediction models at the heart of this idea are fast, sensitive, and robust enough to be trusted, and turns that insight into a concrete review tool. [Part Three](../partthree/index.md) looks underneath these models at the segmentation architectures they depend on, and asks how robust those architectures really are.

A recurring motivation runs through all three parts: geometric agreement metrics such as the Dice Similarity Coefficient correlate weakly with the clinical, dosimetric consequences of a contour {cite}`Poel_2021_predictive`, yet contour errors drive a large share of non-compliant treatment plans {cite}`Peters_2010_Critical`. Shifting QA from geometry to dose is therefore not a cosmetic change but a clinically meaningful one.

Unlike the original thesis — which grouped ASTRA and AutoDoseRank separately as proof-of-concept applications — this site folds each of those tools into the theme it grows out of: AutoDoseRank alongside the dosimetric-awareness work in Part One, and ASTRA alongside the dose-sensitivity work in Part Two.

## Part One: Dosimetric Awareness of Radiation Oncology Professionals

Part One establishes the clinical need and shows that automation can meet it.

**The need is real.** [Chapter 3](../partone/chapter3.md), a qualitative survey published in *Radiotherapy and Oncology*, asked four radiation oncologists and three medical physicists to judge 54 glioblastoma target-volume contour variations across 14 patients. Agreement was only fair to moderate (Cohen's Kappa 0.33–0.74), evaluators misclassified 46% of "no change" cases as "worse", and none of the four genuinely improved contours were recognized as such. The best evaluator reached an F1 score of 0.64 and the worst 0.35. Human reviewers, in other words, are unreliable at estimating the dosimetric impact of contour changes from geometry alone — precisely the gap an automated system could close.

**Automation can exceed expert performance.** [Chapter 4](../partone/chapter4.md), presented at MIDL 2024, put a deep-learning dose predictor head-to-head with three radiation oncologists on the same task. With dosimetric criteria defined explicitly (a variation counts as "sub-optimal" when any organ-at-risk sees more than a 10% dose increase), the model reached a precision and recall of 0.57 and outperformed all three experts at flagging dosimetrically sub-optimal contours. This is the first evidence that a dose-aware model can not only replicate but surpass human dosimetric triage.

**From judgement to ranking.** [Chapter 5](../partone/chapter5.md) turns this capability into a usable tool. AutoDoseRank, presented at the CaPTion workshop at MICCAI 2024, ranks a set of candidate segmentations by their dosimetric quality, combining organ-at-risk-specific dose constraints with clinical priority weights. On 65 segmentations from 13 patients it outperformed three of four radiation oncologists (mean Kendall's Tau 0.129, against a best expert of 0.148 and a worst of 0.014), demonstrating a practical, dosimetry-driven way to triage auto-contour proposals.

**Limitations.** All three studies are confined to glioblastoma, a single institution, and small evaluator and patient cohorts, and they weight all organs-at-risk equally without linking assessments to downstream toxicity or clinical outcomes. Broader validation across tumour sites and centres is needed before these tools change practice.

## Part Two: Sensitivity of Dose Prediction Models

Part Two asks whether the dose predictor underpinning Part One is trustworthy — fast, sensitive to real contour changes, and robust to unusual cases — and then builds a review tool on top of it.

**Accurate and sensitive dose prediction.** [Chapter 6](../parttwo/chapter6.md), published in *Cancers*, trained a cascaded 3D U-Net {cite}`Liu_2021_Technical` to predict glioblastoma VMAT dose distributions from 60 training cases. It achieved a dose score of 0.94 Gy and a mean dose-volume-histogram error of 1.95 Gy, and — most importantly for QA — predicted the dose changes caused by realistic contour variations with a mean error of 1.38 Gy. [Chapter 7](../parttwo/chapter7.md), presented at ISBI 2023, quantified this sensitivity directly: for variations of the left optic nerve contour, the model's predicted dose error (mean absolute error 2.039 Gy) closely tracked the ground-truth inter-expert variation (2.115 Gy), with a correlation of 0.926 between predicted and true dose differences. Because inference is near-instant, such a model could compress planning-and-review cycles that today average more than a week {cite}`Guo_2020_Accurate`.

**Robustness needs deliberate attention.** The *Cancers* study also stress-tested the model against a worst-case, out-of-distribution set and showed that its robustness could be recovered by augmenting the training data with synthetic cases mirroring the observed failure modes — a reminder that sensitivity and robustness must be validated, not assumed.

**From sensitivity to a review tool.** [Chapter 8](../parttwo/chapter8.md) builds ASTRA (Atomic Surface Transformations for Radiotherapy quality Assurance) on this sensitivity. By simulating roughly 2,000 local surface perturbations per patient across 100 glioblastoma cases, ASTRA produces a dose-aware sensitivity map that highlights exactly where a contour edit would most change the delivered dose (for example, a correlation of −0.76 for the left eye). It is the first method to give clinicians local, dosimetry-informed heat maps to focus their review — the applied counterpart of the sensitivity analysis that precedes it. This work won the 2nd best student paper award at EMBC 2023.

**Limitations.** These models are trained on a single glioblastoma VMAT protocol from one institution, so re-training is likely needed for other sites, modalities, or planning systems, and their predictions have not yet been linked to clinical endpoints such as toxicity.

## Part Three: Robustness of Segmentation Models

Part Three looks beneath dose prediction at the U-Net-based segmentation architectures on which both auto-contouring and dose prediction depend, and asks how their design choices affect robustness.

**Skip connections are not free.** [Chapter 9](../partthree/chapter9.md), published in *Computers in Biology and Medicine*, shows that the benefit of skip connections is small for low-to-medium complexity tasks and grows only as complexity increases — and that advanced variants such as the Attention-Gated U-Net and UNETR are not consistently more robust than a plain U-Net under distribution shift. Attention-Gated U-Net scored 0.795 on clean Breast ultrasound but fell to 0.645 under perturbation, below a NoSkip U-Net's 0.735; a NoSkip V-Net won 78.3% of the hardest Heart MRI cases, with a much lower coefficient of variation (0.20 versus 0.35). [Chapter 10](../partthree/chapter10.md), the earlier MICCAI 2023 study this journal paper extends, first established that the value of skip connections is non-linear and appears mainly at high task complexity, and that it comes at a robustness cost on out-of-domain clinical data.

**Context versus foreground.** [Chapter 11](../partthree/chapter11.md), presented at Medical Imaging meets NeurIPS 2022, examined the trade-off between global context and foreground-to-background ratio in 3D segmentation. All architectures prefer more global context, but Transformer-based (UNETR) and attention-gated models are markedly more sensitive to shifts in foreground ratio than a vanilla U-Net, with Dice drops of up to 0.369 compared with just 0.0139 for the U-Net.

**Implication.** Reliable dose-aware QA depends on segmentation models that behave predictably across scanners, protocols, and anatomy. These chapters argue for choosing architectures — and curating training data for texture and foreground-background diversity — with robustness in mind, rather than adopting the most elaborate variant by default.

**Limitations.** The robustness studies rely on synthetic and curated datasets with controlled perturbations, focus on U-Net variants, and measure segmentation quality with standard geometric metrics rather than clinical outcomes.

## Synthesis

Taken together, the three parts support the central hypothesis. Part One shows that dose-aware QA is clinically needed and that models can already match or beat expert dosimetric judgement, with AutoDoseRank turning that capability into a ranking tool. Part Two shows that the underlying dose predictors are accurate, sensitive to realistic contour variation, and fast enough for real-time review, with ASTRA translating their sensitivity into an actionable, localized map. Part Three shows that the segmentation architectures beneath these models must be chosen and trained for robustness if the whole pipeline is to be trusted in the clinic.

The through-line is a shift from geometry to dose: evaluating contours by their clinical, dosimetric consequences rather than their pixel-wise overlap. Realizing this shift in routine practice will require external validation across tumour sites, institutions, and imaging protocols, and — ultimately — evidence that dose-aware QA improves patient outcomes, not just agreement with experts.
