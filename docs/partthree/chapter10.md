# Do We Really Need that Skip-Connection? Understanding Its Interplay with Task Complexity

This is a WIP (Work-In-Progress): this message will be removed once sufficient progress has been made. 

#[![2 minute video abstract](https://img.youtube.com/vi/YreG6vC64aw/0.jpg)](https://www.youtube.com/watch?v=YreG6vC64aw)

(click on the picture above to watch a 2 minute video abstract describing this research)

The UNet architecture has become the preferred model used for medical image segmentation tasks. Since its inception, several variants have been proposed. An important component of the UNet architecture is the use of skip-connections, said to carry over image details on its decoder branch at different scales. However, beyond this intuition, not much is known as to what extent skip-connections of the UNet are necessary, nor what their interplay is in terms of model robustness when they are subjected to different levels of task complexity. 

In this study we analyzed these questions using three variants of the UNet architecture (the standard UNet, a ``No-Skip'' UNet, and an Attention-Gated UNet) using controlled experiments on varying synthetic texture images, and evaluated these findings on three medical image data sets. We measured task complexity as a function of texture-based similarities between foreground and background distributions. 

Using this scheme, our findings suggest that the benefit of employing skip-connections is small for low-to-medium complexity tasks, and its benefit appear only when the task complexity becomes large. We report that such incremental benefit is non-linear, with the Attention-Gated UNet yielding larger improvements. Furthermore, we find that these benefits also bring along robustness degradations on clinical data sets, particularly in out-of-domain scenarios. These results suggest a dependency between task complexity and the choice/design of noise-resilient skip-connections, indicating the need for careful consideration while using these skip-connections.

#See [the project repository](https://github.com/amithjkamath/to_skip_or_not) to reproduce these results.

## Citation

If you find this work useful, please cite it as:

    @inproceedings{kamath2023skipconnections,
    title={Do we really need that skip connection? Understanding its' interplay with task complexity},
    author={Kamath, Amith and Willmann, Jonas and Andratschke, Nicolaus and Reyes, Mauricio},
    booktitle={International Conference on Medical Image Computing and Computer-Assisted Intervention},
    year={2023}
    }