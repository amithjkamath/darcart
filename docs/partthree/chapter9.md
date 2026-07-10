# The impact of U-Net architecture choices and skip connections on the robustness of segmentation across texture variations

This work was [published](https://doi.org/10.1016/j.compbiomed.2025.111056) in [Computers in Biology and Medicine](https://www.sciencedirect.com/journal/computers-in-biology-and-medicine) (CiBM), volume 197, article 111056, 2025.

**Read the paper:** [Publisher (Computers in Biology and Medicine)](https://doi.org/10.1016/j.compbiomed.2025.111056) · [Google Scholar](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=clej42kAAAAJ&citation_for_view=clej42kAAAAJ:u_35RYKgDlwC)

The U-Net has become the default architecture for medical image segmentation, and more than a hundred variants have been proposed — mostly modifying its skip connections, backbones, and bottlenecks. Skip connections are widely believed to carry fine spatial detail across the encoder-decoder gap, but how much they help, and how they interact with robustness under real-world variability, is not well understood.

This journal paper extends the MICCAI 2023 conference study (see [Chapter 10](chapter10.md)) with a broader analysis across task complexities and texture variations. We find that the benefit of skip connections is small for low-to-medium complexity tasks and grows only as task complexity becomes large, and — critically — that advanced variants such as the Attention-Gated U-Net and UNETR are **not consistently more robust** than a standard U-Net under distribution shifts. NoSkip architectures, or those using addition-based skip connections (e.g., V-Net), offer better stability on out-of-domain data, while dataset diversity (texture variation and foreground-background balance) further improves generalizability. These results argue for careful, robustness-aware design of skip connections rather than adopting more complex architectures by default.

## Citation

If you find this work useful, please cite it as:

    @article{kamath2025impact,
    title={The impact of U-Net architecture choices and skip connections on the robustness of segmentation across texture variations},
    author={Kamath, Amith and Willmann, Jonas and Andratschke, Nicolaus and Reyes, Mauricio},
    journal={Computers in Biology and Medicine},
    volume={197},
    pages={111056},
    publisher={Elsevier},
    doi={10.1016/j.compbiomed.2025.111056},
    year={2025}
    }
