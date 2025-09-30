# Evaluating the Effectiveness of Fine-Tuning in Financial NLP: The Case of Social Trading Action Detection

## 🧾 Abstract

Financial Natural Language Processing has become increasingly important for understanding and predicting market behavior. One of the most intriguing approaches focuses on detecting user intentions in social media, which have been increasingly linked to market movements. However, most existing methods for this purpose rely on simple sentiment analysis models, which fail to capture the concrete trading intentions expressed in these discussions. 
Large Language Models (LLMs) represent a promising alternative, and fine-tuning is widely assumed to further enhance their effectiveness. Nevertheless, it remains uncertain to what extent fine-tuning enhances performance across different model families, particularly in noisy and domain-specific contexts such as online posts. 
In this paper, we address these challenges by introducing Social Trading Action Detection (STAD), a new task that classifies online posts into actionable categories (buy, sell, or other). We also present FinReddit-2K, a dataset of 2,123 manually annotated Reddit posts, designed to serve as a benchmark for this task. Using FinReddit-2K, we perform a systematic evaluation of 57 models, covering traditional neural networks, zero-shot sequence classifiers, and a diverse range of LLMs.
In order to investigate the behaviour of fine-tuning in this domain, we compare 12 classic models, 23 LLMs in zero-shot settings with 22 fine-tuned counterparts. This comprehensive experiment provides an in-depth evaluation of the benefits and limitations of fine-tuning, highlighting not only the types of errors it can mitigate but also those it may introduce. \color{black}
Results show that fine-tuning yields, on average, a +15.1\% increase in F1 score, with Mistral-7B achieving the best performance (F1 = 86.0\%), but also reveal several cases where fine-tuning fails to deliver improvements.
---

## 📘 Introduction
This project introduces the novel task of **Social Trading Action Detection (STAD)**, which goes beyond sentiment classification to directly infer trading actions from financial discussions. To support this task, we present **FinReddit-2K**, a new manually annotated dataset of Reddit posts, and benchmark a variety of machine learning and large language models to assess their effectiveness in identifying these actions: *buy*, *sell*, or *other*.

This repository provides:

- 📝 A manually annotated dataset of Reddit posts labeled as `buy`, `sell`, or `other`
- 🐍  A Python module for text preprocessing, used to clean and prepare posts before modeling

All experiments were conducted using the FinReddit-2K dataset on a machine equipped with an NVIDIA A100-SXM4 GPU (80GB memory). We evaluated four families of models through a **5-fold stratified cross-validation**, ensuring class balance across folds.

---

## 📂 Repository Structure

```bash
📦 FINREDDIT-2K/
├── FinReddit-2K.csv       # Sample dataset with annotated trading actions
├── README.md              # Project overview and documentation
└── text_cleaning.py       # Preprocessing function for cleaning Reddit text
```

### 🗂️ FinReddit-2K dataset

The dataset consists of 2,123 manually annotated Reddit posts. It has the following structure:

| Column      | Description                                              |
|-------------|----------------------------------------------------------|
| `subreddit` | The subreddit in which the Reddit post was published     |
| `stock`     | The stock mentioned in the Reddit post                   |
| `text`      | The raw content of the Reddit post                       |
| `label`     | The associated trading action: `buy`, `sell`, or `other` |

---

## 👥 Authors

[**Simone D'Amico**](https://orcid.org/0009-0002-2820-0277), Department of Electrical Engineering and Information Technology, University of Naples Federico II, Naples, Italy

[**Andrea Maurino**](https://orcid.org/0000-0001-9803-3668), Department of Informatics, Systems and Communication, University of Milano-Bicocca, Milan, Italy

[**Francesco Osborne**](https://orcid.org/0000-0001-6557-3131), Knowledge Media Institute, The Open University, Milton Keynes, UK

[**Giancarlo Sperlì**](https://orcid.org/0000-0003-4033-3777), Department of Electrical Engineering and Information Technology, University of Naples Federico II, Naples, Italy

---
