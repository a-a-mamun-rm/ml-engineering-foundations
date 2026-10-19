# ML Engineering Foundations

A structured, hands-on path through the machine-learning knowledge an **ML/AI engineer** is expected to have:
classic ML, statistics and maths, deep learning, LLMs and RAG, serving and MLOps, plus Python and SQL.
Every topic has a short README with curated sources and a notebook that runs on a laptop CPU.

I come from LLM systems work (RAG, agents, vLLM serving), so this repository is where I rebuild and show the
classic-ML foundations underneath. It started as a 7-day intensive and keeps growing.

> Built with AI assistance (Claude) for structure and first drafts; I work through every notebook and
> exercise myself, and my own notes and solutions live in each module's `notes.md`.

## How to use

```bash
git clone https://github.com/a-a-mamun-rm/ml-engineering-foundations.git
cd ml-engineering-foundations
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
jupyter lab
```

Each notebook follows the same shape: **concept → runnable demo → ✍️ Your turn (exercises) → 🎯 Interview check
(questions to answer aloud)**. Read the module README's sources first, then run the notebook top to bottom,
then do the exercises without looking at the solution cells.

## Modules

| # | Module | Notebooks | Key questions it answers |
|---|---|---|---|
| 00 | [Setup](00-setup/) | — | Environment, how to study |
| 01 | [ML fundamentals](01-ml-fundamentals/) | bias–variance & regularisation · cross-validation & metrics · data leakage | Over/underfitting? Which metric? Is my score honest? |
| 02 | [Preprocessing & feature engineering](02-data-preprocessing-feature-engineering/) | EDA → leak-free pipeline → saved model · feature-engineering cookbook | How do I go from a raw CSV to a model behind an API? |
| 03 | [Supervised learning](03-supervised-learning/) | linear/logistic regression from scratch · trees, ensembles, SVM, KNN | What does `.fit()` do? Bagging vs boosting? |
| 04 | [Unsupervised learning](04-unsupervised-learning/) | K-means, DBSCAN, hierarchical, PCA, Isolation Forest | How do I choose k? When does K-means fail? |
| 05 | [Statistics & maths](05-statistics-and-math/) | probability & hypothesis testing · gradient descent, losses, vectors | p-values, A/B tests, bootstrap CIs, optimisers |
| 06 | [Deep learning](06-deep-learning/) | PyTorch training loop with dropout, weight decay, early stopping | Write a training loop from memory |
| 07 | [LLMs & RAG](07-llms-and-rag/) | chunking, BM25, embeddings, hybrid RRF, re-ranking, retrieval metrics | How do I build *and measure* retrieval? |
| 08 | [Serving, GPU & MLOps](08-serving-gpu-mlops/) | GPU memory & throughput calculator · MLflow experiment tracking | Will this LLM fit? How many users? Reproducibility? |
| 09 | [Python, SQL & coding](09-python-sql-coding/) | SQL practice on SQLite · production-style Python package with tests and an API | Production-quality code, SQL windows, live coding |
| 10 | [Interview practice](10-interview-practice/) | — | Question bank, ML system design, STAR stories |

## 7-day intensive (20–26 Oct 2026)

About 7 focused hours a day: **morning** sources (~2 h), **midday** notebooks (~3–4 h), **evening** interview
drill (~1 h: 3 coding problems + 1 STAR story + one section of the question bank, answered aloud).

| Day | Date | Focus | Notebooks | Evening drill |
|---|---|---|---|---|
| 1 | Tue 20 Oct | Bias–variance, CV, metrics, leakage | 01 · 01–03 | Story: RAG platform |
| 2 | Wed 21 Oct | EDA, preprocessing pipelines, feature engineering | 02 · 01–02 (+ rebuild an old project with a proper README) | Story: LLM serving |
| 3 | Thu 22 Oct | Linear/logistic from scratch, trees, boosting, SVM, KNN | 03 · 01–02 | Story: coding agent |
| 4 | Fri 23 Oct | Unsupervised learning + statistics | 04 · 01, 05 · 01 | Story: research paper |
| 5 | Sat 24 Oct | Maths for ML + deep learning | 05 · 02, 06 · 01 | Story: a failure and what I learned |
| 6 | Sun 25 Oct | LLMs/RAG + serving/MLOps | 07 · 01, 08 · 01–02 | ML system design drill |
| 7 | Mon 26 Oct | SQL, production Python, full mock interview | 09 · all, 10 | Full mock (45 min technical + 15 behavioural) |

## Progress

- [ ] 01 ML fundamentals
- [ ] 02 Preprocessing & feature engineering
- [ ] 03 Supervised learning
- [ ] 04 Unsupervised learning
- [ ] 05 Statistics & maths
- [ ] 06 Deep learning
- [ ] 07 LLMs & RAG
- [ ] 08 Serving, GPU & MLOps
- [ ] 09 Python, SQL & coding
- [ ] 10 Interview practice

## Core references (used across modules)

| Resource | Why |
|---|---|
| [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) | The best free reference for classic ML in practice |
| [An Introduction to Statistical Learning (ISLP), free PDF](https://www.statlearning.com/) | Theory with intuition; Python edition |
| [Hands-On Machine Learning (Géron), notebooks](https://github.com/ageron/handson-ml3) | End-to-end projects |
| [StatQuest (YouTube)](https://www.youtube.com/@statquest) | Clear 10–20 minute explanations of every algorithm |
| [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) | Fast, practical fundamentals |
| [Mathematics for Machine Learning, free book](https://mml-book.github.io/) | Linear algebra, calculus, probability |
| [Dive into Deep Learning](https://d2l.ai/) | Deep learning with runnable code |
| [Chip Huyen, ML interviews book (free)](https://huyenchip.com/ml-interviews-book/) | What interviewers ask and why |

Datasets: scikit-learn's built-in datasets (no download needed), plus optional public Kaggle files noted in each notebook.

## License

Code: MIT. External resources belong to their authors; this repo only links to them.
