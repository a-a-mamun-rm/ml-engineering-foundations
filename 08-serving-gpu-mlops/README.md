# 08 · Serving, GPU & MLOps

| Notebook | You will be able to |
|---|---|
| [01_gpu_memory_and_throughput_calculator](01_gpu_memory_and_throughput_calculator.ipynb) | Estimate weights + KV-cache memory, concurrency and decode speed; explain TP vs PP, PagedAttention, continuous batching, MoE, GQA/MLA |
| [02_experiment_tracking_mlflow](02_experiment_tracking_mlflow.ipynb) | Log runs (params, metrics, data hash, git commit, model) to MLflow; compare runs; reload the best model |

## Start here
- EleutherAI, [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) (memory and compute formulas)
- [vLLM documentation](https://docs.vllm.ai/) (engine arguments, parallelism, quantisation)
- Kwon et al., [PagedAttention / vLLM paper](https://arxiv.org/abs/2309.06180)
- Hugging Face, [Optimizing LLMs for speed and memory](https://huggingface.co/docs/transformers/llm_tutorial_optimization)
- [MLflow documentation](https://mlflow.org/docs/latest/index.html) (tracking quickstart)

## Go deeper
- Shoeybi et al., [Megatron-LM (tensor parallelism)](https://arxiv.org/abs/1909.08053)
- [Made With ML](https://madewithml.com/) (end-to-end MLOps course)
- Google, [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml)
- [Docker: Get started](https://docs.docker.com/get-started/) · [AWS Skill Builder](https://skillbuilder.aws/) (free cloud basics) · [Evidently (drift monitoring)](https://docs.evidentlyai.com/)
- Chip Huyen, *Designing Machine Learning Systems* (O'Reilly, 2022)

## Done when
- [ ] I can do the memory maths for a 27B model in BF16 and FP8 out loud
- [ ] I can explain when to use tensor vs pipeline parallelism
- [ ] I can describe how I'd make an experiment reproducible and a deployment rollback-safe
