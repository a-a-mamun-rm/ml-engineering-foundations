# 00 · Setup and how to study

## Environment
```bash
python -m venv .venv
.venv\Scripts\activate            # Windows
pip install -r requirements.txt
jupyter lab
```
Everything runs on CPU. Module 07 downloads two small models (~90 MB each) from Hugging Face on first run.
Free GPUs if you want them: [Kaggle notebooks](https://www.kaggle.com/code) or [Google Colab](https://colab.research.google.com/).

## Study loop (per notebook)
1. **Read** the module README's "Start here" sources (≈1–2 h).
2. **Run** the notebook top to bottom. Change one number per section and predict the result *before* re-running.
3. **Do** the ✍️ exercises in the empty cells, without looking at solutions.
4. **Say** the 🎯 interview answers out loud in under 1 minute each. Record yourself once a day.
5. **Write** 5–10 lines in the module's `notes.md`, in your own words. If you can't explain it simply, go back to step 1.

## Rules
- Prefer understanding over coverage: one topic you can explain beats three you've skimmed.
- Every claim you make in an interview should be backed by something you ran yourself.
