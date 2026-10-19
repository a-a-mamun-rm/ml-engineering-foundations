# ML Engineering Foundations

A hands-on, structured path through the core knowledge an **ML / AI engineer** is expected to have:
classic machine learning, statistics and maths, deep learning, LLMs and retrieval-augmented generation (RAG),
model serving and MLOps, plus the Python and SQL used every day on the job.

Each topic has:
- a **module README** with a short summary and curated, free sources (docs, books, courses, papers), and
- one or more **Jupyter notebooks** that explain the concept, demonstrate it with runnable code, and end with
  exercises and interview-style questions.

Everything runs on a normal laptop CPU. No paid services or API keys are needed.

## Who this is for

- Software or data engineers moving into ML engineering
- LLM / GenAI engineers who want solid classic-ML and statistics foundations
- Anyone preparing for ML engineer interviews (theory, coding, SQL and system design)

Assumed background: comfortable with Python and basic NumPy/pandas.

## Repository structure

```
ml-engineering-foundations/
├── 00-setup/                                   environment + how to study with this repo
├── 01-ml-fundamentals/                         bias–variance, cross-validation, metrics, data leakage
├── 02-data-preprocessing-feature-engineering/  EDA, pipelines, encoding, imputation, feature recipes
├── 03-supervised-learning/                     linear/logistic regression from scratch, trees, ensembles, SVM, KNN
├── 04-unsupervised-learning/                   K-means, DBSCAN, hierarchical clustering, PCA, anomaly detection
├── 05-statistics-and-math/                     probability, hypothesis tests, A/B tests, optimisers, loss functions
├── 06-deep-learning/                           PyTorch training loop, regularisation, debugging
├── 07-llms-and-rag/                            chunking, BM25, embeddings, hybrid search, re-ranking, RAG evaluation
├── 08-serving-gpu-mlops/                       LLM memory/throughput maths, vLLM concepts, MLflow tracking
├── 09-python-sql-coding/                       SQL practice + a tested, production-style FastAPI ML service
├── 10-interview-practice/                      question bank, ML system design framework, STAR template
├── data/                                       optional public datasets (download instructions)
└── requirements.txt
```

## What's inside

### [00 · Setup](00-setup/)
Environment setup and a simple study loop: read → run → change → explain.

### [01 · ML fundamentals](01-ml-fundamentals/)
| Notebook | Covers |
|---|---|
| [01 · Bias, variance, overfitting & regularisation](01-ml-fundamentals/01_bias_variance_overfitting.ipynb) | Under/overfitting, validation and learning curves, Ridge/Lasso |
| [02 · Cross-validation & metrics](01-ml-fundamentals/02_cross_validation_and_metrics.ipynb) | KFold / Stratified / Group / TimeSeries splits, precision–recall, ROC-AUC vs PR-AUC, threshold choice, calibration, regression metrics |
| [03 · Data leakage](01-ml-fundamentals/03_data_leakage.ipynb) | 5 leakage types, each demonstrated with leaky vs honest scores, and the pipeline fix |

### [02 · Data preprocessing & feature engineering](02-data-preprocessing-feature-engineering/)
| Notebook | Covers |
|---|---|
| [01 · EDA → pipeline → saved model](02-data-preprocessing-feature-engineering/01_eda_preprocessing_pipeline.ipynb) | End-to-end tabular workflow on clinical-style data: EDA, feature engineering, `ColumnTransformer`, model comparison, tuning, odds ratios, saving a model for an API |
| [02 · Feature engineering cookbook](02-data-preprocessing-feature-engineering/02_feature_engineering_cookbook.ipynb) | Scalers, one-hot / ordinal / target encoding, cyclical dates, binning, interactions, KNN imputation, TF-IDF |

### [03 · Supervised learning](03-supervised-learning/)
| Notebook | Covers |
|---|---|
| [01 · Linear & logistic regression from scratch](03-supervised-learning/01_linear_logistic_from_scratch.ipynb) | Normal equation vs gradient descent, logistic regression in NumPy, cross-entropy, p-values and odds ratios with statsmodels |
| [02 · Trees, ensembles, SVM & KNN](03-supervised-learning/02_trees_ensembles_svm_knn.ipynb) | Tree depth, random forest (OOB), gradient boosting with early stopping, why scaling matters, permutation importance, decision boundaries |

### [04 · Unsupervised learning](04-unsupervised-learning/)
| Notebook | Covers |
|---|---|
| [01 · Clustering, PCA & anomaly detection](04-unsupervised-learning/01_clustering_pca_anomaly.ipynb) | Choosing k (elbow, silhouette), where K-means fails and DBSCAN works, dendrograms, PCA variance and reconstruction, Isolation Forest |

### [05 · Statistics & maths](05-statistics-and-math/)
| Notebook | Covers |
|---|---|
| [01 · Probability & hypothesis testing](05-statistics-and-math/01_probability_and_hypothesis_testing.ipynb) | Bayes and base rates, CLT, confidence intervals, t-test / chi-square, A/B tests and power, multiple testing, bootstrap CI for AUC |
| [02 · Gradient descent, losses & vectors](05-statistics-and-math/02_gradient_descent_losses_linear_algebra.ipynb) | Learning rates, batch vs mini-batch, SGD vs momentum vs Adam, regression and classification losses, stable softmax, cosine similarity |

### [06 · Deep learning](06-deep-learning/)
| Notebook | Covers |
|---|---|
| [01 · PyTorch training loop & regularisation](06-deep-learning/01_pytorch_training_loop_regularisation.ipynb) | Autograd, a clean train/eval loop, dropout vs weight decay vs early stopping, a debugging checklist |

### [07 · LLMs & RAG](07-llms-and-rag/)
| Notebook | Covers |
|---|---|
| [01 · Retrieval for RAG: build and measure it](07-llms-and-rag/01_embeddings_hybrid_search_rrf_eval.ipynb) | Chunking, BM25, sentence-transformer embeddings, hybrid search with Reciprocal Rank Fusion, cross-encoder re-ranking, Recall@k / MRR / nDCG, error analysis, grounded prompts with citations |

### [08 · Serving, GPU & MLOps](08-serving-gpu-mlops/)
| Notebook | Covers |
|---|---|
| [01 · GPU memory & throughput calculator](08-serving-gpu-mlops/01_gpu_memory_and_throughput_calculator.ipynb) | Weights and KV-cache memory, concurrency vs context length, decode-speed ceilings, MoE, GQA/MLA, tensor vs pipeline parallelism, key vLLM ideas |
| [02 · Experiment tracking with MLflow](08-serving-gpu-mlops/02_experiment_tracking_mlflow.ipynb) | Logging params, metrics, data hash, git commit and models; comparing runs; reloading the best model; MLOps tool map |

### [09 · Python, SQL & coding](09-python-sql-coding/)
| Item | Covers |
|---|---|
| [01 · SQL practice (SQLite)](09-python-sql-coding/01_sql_practice_sqlite.ipynb) | 10 interview-style questions (JOINs, HAVING, CTEs, window functions) with solutions and pandas equivalents |
| [production_python/](09-python-sql-coding/production_python/) | A small ML service: typed feature code, Pydantic validation, FastAPI `/predict`, pytest tests |

### [10 · Interview practice](10-interview-practice/)
A question bank mapped to the notebooks, an ML system-design framework with practice prompts, and a STAR
template for behavioural answers.

## Suggested learning paths

| Goal | Path |
|---|---|
| **Classic ML foundations** | 01 → 02 → 03 → 04 → 05 |
| **LLM / GenAI engineer** | 01 → 05·02 → 06 → 07 → 08 |
| **Interview crash course (~1 week)** | 01 → 02·01 → 03 → 04 → 05·01 → 07 → 08·01 → 09 → 10 |

## Getting started

```bash
git clone https://github.com/a-a-mamun-rm/ml-engineering-foundations.git
cd ml-engineering-foundations
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
jupyter lab
```

- Notebooks use scikit-learn's built-in datasets or generate synthetic data, so nothing needs downloading.
  [`data/`](data/) explains the optional real datasets.
- Module 07 downloads two small Hugging Face models (~90 MB each) on first run and falls back to TF-IDF offline.
- Every notebook is saved with its outputs, so you can read the results on GitHub before running anything.

## How each notebook is organised

1. **Concept**: a short explanation, usually with a comparison table
2. **Demo**: runnable code with plots and printed results
3. **✍️ Your turn**: exercises to complete in the empty cells
4. **🎯 Interview check**: questions to answer aloud in under a minute

Each module also has a `notes.md` for writing your own summary.

## Core references

| Resource | Why |
|---|---|
| [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) | The best free reference for classic ML in practice |
| [An Introduction to Statistical Learning (ISLP), free PDF](https://www.statlearning.com/) | Theory with intuition; Python edition |
| [Hands-On Machine Learning (Géron), notebooks](https://github.com/ageron/handson-ml3) | End-to-end projects |
| [StatQuest (YouTube)](https://www.youtube.com/@statquest) | Clear short explanations of most algorithms |
| [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) | Fast, practical fundamentals |
| [Mathematics for Machine Learning, free book](https://mml-book.github.io/) | Linear algebra, calculus, probability |
| [Dive into Deep Learning](https://d2l.ai/) | Deep learning with runnable code |
| [Chip Huyen, ML interviews book (free)](https://huyenchip.com/ml-interviews-book/) | What interviewers ask and why |

Module-specific sources are listed in each module's README.

## Contributing

Issues and pull requests are welcome: corrections, clearer explanations, new exercises, or new topics
(e.g. time series, recommender systems, fine-tuning). Please make sure notebooks run top to bottom before
opening a PR.

## Acknowledgements & license

Content was drafted with AI assistance (Claude), then reviewed, run and checked by the author.
Code is released under the [MIT License](LICENSE). External resources belong to their authors; this repository
only links to them.
