# 07 · LLMs & RAG

| Notebook | You will be able to |
|---|---|
| [01_embeddings_hybrid_search_rrf_eval](01_embeddings_hybrid_search_rrf_eval.ipynb) | Chunk text; retrieve with BM25 and embeddings; fuse with RRF; re-rank with a cross-encoder; measure Recall@k, MRR and nDCG; build a grounded, cited prompt |

## Start here
- Jay Alammar, [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- Hugging Face [LLM Course](https://huggingface.co/learn/llm-course) (transformers, tokenizers, fine-tuning basics)
- [Sentence-Transformers documentation](https://www.sbert.net/) (bi-encoders, cross-encoders, retrieve & re-rank)
- Anthropic, [Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) (hybrid BM25 + embeddings + re-ranking, with measured gains)
- Eugene Yan, [Patterns for building LLM-based systems & products](https://eugeneyan.com/writing/llm-patterns/)

## Papers worth knowing by name
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (2017)
- Lewis et al., [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) (2020)
- Cormack et al., [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) (2009)

## Frameworks (know at least two)
- [LlamaIndex docs](https://docs.llamaindex.ai/) · [LangChain docs](https://python.langchain.com/) · [RAGAS (RAG evaluation)](https://docs.ragas.io/)

## Reliability & safety
- Lilian Weng, [Extrinsic hallucinations in LLMs](https://lilianweng.github.io/posts/2024-07-07-hallucination/)
- [OWASP Top 10 for LLM applications](https://genai.owasp.org/llm-top-10/) (prompt injection and more)

## Done when
- [ ] I can draw a RAG pipeline and say where each failure mode happens
- [ ] I can give one query where BM25 beats dense retrieval, and one where it loses
- [ ] I have rebuilt the notebook's retriever in LlamaIndex and compared the numbers
