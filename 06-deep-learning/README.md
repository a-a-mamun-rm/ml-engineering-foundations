# 06 · Deep learning (PyTorch)

| Notebook | You will be able to |
|---|---|
| [01_pytorch_training_loop_regularisation](01_pytorch_training_loop_regularisation.ipynb) | Write a training/evaluation loop from memory; cause overfitting and fix it with dropout, weight decay and early stopping |

## Start here
- PyTorch: [Learn the basics](https://pytorch.org/tutorials/beginner/basics/intro.html) (tensors → datasets → models → autograd → optimisation → save/load)
- 3Blue1Brown: [Neural networks](https://www.3blue1brown.com/topics/neural-networks) (chapters 1–4, including backpropagation)
- Andrej Karpathy, [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/)

## Go deeper
- Karpathy, [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) (micrograd → GPT)
- [Dive into Deep Learning](https://d2l.ai/) (MLP chapter: dropout, weight decay; CNN chapters)
- [fast.ai Practical Deep Learning](https://course.fast.ai/)

## Done when
- [ ] I can write the 4-line training step without notes
- [ ] I can explain `model.train()` vs `model.eval()` and `torch.no_grad()`
- [ ] I can debug "loss is NaN" and "loss does not go down"
