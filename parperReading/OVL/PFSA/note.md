# 论文阅读 
## Plug-in Feedback Self-adaptive Attention in CLIP for Training-free Open-Vocabulary Segmentation

Open-Vocabulary Segmentation（OVSS）：开放词汇分割

Training-free：无训练

[Contrastive Language-Image Pre-training（CLIP）：对比语言-图像预训练](https://blog.csdn.net/likuoelie/article/details/152820331)

### 一些概念

1. 自蒸馏（Self-distillation）：自蒸馏是知识蒸馏（Knowledge Distillation）的一个重要分支，核心是让模型自身（而非独立的 “教师模型”）生成的知识指导自身学习，通过挖掘模型内部的隐含信息（如输出分布、中间特征），在不引入额外数据或复杂教师模型的情况下，提升模型的泛化能力、紧凑性或任务适配性。

2. CLS token：在 Transformer（尤其是 Vision Transformer，ViT）模型中，CLS token（Classification token，分类标记） 是一个特殊的输入向量，专门用于承载全局语义信息，辅助模型完成分类等任务。

3. 最后一层注意力调制（Last-layer Attention Modulation）：是现有方法（如 SCLIP、ProxyCLIP 等）为提升分割性能而采用的核心技术，其本质是通过修改 ViT 最后一层的注意力图，增强图像 patch 间的空间关联性，进而优化分割结果的连贯性。

### 本文创新点




#### 模型结构

