# 10 · Interview practice

Answer every question **out loud**, under 2 minutes, then check yourself against the linked notebook.

## 1. Question bank

### Classic ML (modules 01–04)
1. Overfitting vs underfitting: how do you detect each, and what do you try first? → 01·01
2. What is data leakage? Give a real example and how you'd prevent it. → 01·03
3. Precision vs recall: which matters more for disease screening? For spam? → 01·02
4. When is accuracy misleading? What do you use instead? → 01·02
5. How do you handle class imbalance? → 01·02
6. Walk me through building a model for a new tabular dataset, from raw file to API. → 02·01
7. One-hot vs target encoding for a column with 10,000 categories? → 02·02
8. Derive (in words) the gradient of logistic regression. What does a coefficient mean? → 03·01
9. Bagging vs boosting. Random forest vs XGBoost. → 03·02
10. L1 vs L2 regularisation. → 01·01
11. How do you choose k in K-means? When does K-means fail? → 04·01
12. Explain PCA to a non-technical manager. → 04·01
13. Your model is 95% accurate offline but fails in production. What do you check? → 01·03

### Statistics & maths (module 05)
14. Explain a p-value and a 95% confidence interval correctly.
15. Disease prevalence 1%, test sensitivity 95%, specificity 90%: P(disease | positive)?
16. How do you design an A/B test? What is statistical power?
17. Why does Adam usually train faster than SGD?
18. Cosine similarity vs Euclidean distance for embeddings?

### Deep learning (module 06)
19. Write the PyTorch training step from memory.
20. Dropout vs weight decay vs early stopping.
21. Loss is NaN. Loss doesn't go down. Debug each.

### LLMs & RAG (module 07)
22. Walk through a RAG system end to end. Where does it fail?
23. Bi-encoder vs cross-encoder; why use both?
24. How do you evaluate retrieval and generation? With no labels?
25. How do you reduce hallucinations, and how do you prove it worked?
26. RAG vs fine-tuning: when would you fine-tune?
27. What is prompt injection? One defence.

### Serving & MLOps (module 08)
28. Memory maths for a 27B model in BF16 and FP8.
29. Tensor vs pipeline parallelism: when each?
30. What do PagedAttention, continuous batching and prefix caching do?
31. Which metrics do you monitor on an LLM server? On a classic ML model?
32. How do you make an experiment reproducible? How do you roll back a bad model?

### Behavioural
33. Tell me about yourself (60–90 seconds).
34. A time a model or system you built failed. What did you change?
35. A disagreement with a teammate and how you resolved it.
36. How do you keep up with AI? (Name real sources you use.)

## 2. ML system design: answer framework (~35 minutes)

1. **Clarify** (5 min): users, scale, latency budget, what "good" means for the business.
2. **Metrics**: offline (AUC, recall@k, faithfulness) and online (conversion, tickets resolved, cost per request).
3. **Data**: sources, labels, volume, freshness, privacy; leakage risks.
4. **Baseline first**: rules or a simple model; then the ML/LLM approach and why.
5. **Architecture**: draw the boxes: ingestion → features/index → model → serving → feedback.
6. **Evaluation**: offline test set, then shadow traffic or an A/B test.
7. **Serving**: latency, throughput, cost, hardware, batching, caching, fallbacks.
8. **Monitoring & iteration**: drift, quality sampling, alerts, retraining or re-indexing.
9. **Trade-offs & risks**: say what you would *not* build in v1.

### Drills
- **A.** A RAG assistant over 50,000 internal documents for 500 staff, answers must cite sources.
- **B.** Self-host an open-weight LLM for ~200 developers on a fixed GPU budget (coding assistant).
- **C.** Predict customer churn for a fintech app; the business wants weekly risk scores.
- **D.** Detect fraudulent transactions in real time (< 50 ms) with 0.1% positives.

## 3. STAR story template

Write 6 stories (each with **one number** and **one trade-off you chose**):

| | |
|---|---|
| **Situation** | 1–2 sentences of context |
| **Task** | what *you* owned |
| **Action** | 3–4 concrete steps, tools and decisions, why you chose them |
| **Result** | a number, what changed, what you learned / would do differently |

## 4. Sources
- Chip Huyen, [Introduction to Machine Learning Interviews (free book)](https://huyenchip.com/ml-interviews-book/)
- Chip Huyen, *Designing Machine Learning Systems* (O'Reilly, 2022)
- Ali Aminian & Alex Xu, *Machine Learning System Design Interview* (ByteByteGo, 2023)
- Google, [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml)
