# 02 · Data preprocessing & feature engineering

| Notebook | You will be able to |
|---|---|
| [01_eda_preprocessing_pipeline](01_eda_preprocessing_pipeline.ipynb) | Run EDA, engineer features, build a leak-free `Pipeline` + `ColumnTransformer`, tune, interpret odds ratios, save the model for an API |
| [02_feature_engineering_cookbook](02_feature_engineering_cookbook.ipynb) | Scale, encode (one-hot, ordinal, target), handle dates, bins, interactions, missing values, text |

## Start here
- Kaggle Learn: [Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) (missing values, categorical variables, pipelines, leakage) and [Feature Engineering](https://www.kaggle.com/learn/feature-engineering)
- scikit-learn: [Pipelines and composite estimators](https://scikit-learn.org/stable/modules/compose.html) · [Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html) · [Imputation](https://scikit-learn.org/stable/modules/impute.html)
- Géron, *Hands-On Machine Learning*, ch. 2 "End-to-end project" ([notebooks](https://github.com/ageron/handson-ml3))

## Go deeper
- Kuhn & Johnson, [Feature Engineering and Selection (free online)](https://feat.engineering/)

## Done when
- [ ] I can write a `ColumnTransformer` pipeline from a blank file in 20 minutes
- [ ] I can explain why every fitted step must live inside the pipeline
- [ ] I can choose an encoding for a 10,000-category column and justify it
