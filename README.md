# Evaluating the Effectiveness of Fine-Tuning in Financial NLP: The Case of Social Trading Action Detection

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
