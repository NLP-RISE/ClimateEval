# 🌍 ClimateEval

> This code was originally forked from [eci-io/climategpt-evaluation](https://github.com/eci-io/climategpt-evaluation), with significant modifications and additions.

**ClimateEval** is a comprehensive benchmark designed to evaluate large language models (LLMs) across a wide range of climate change–related NLP tasks. It aggregates 13 datasets into 25 tasks covering classification, QA, information extraction, and misinformation detection — all integrated into the [`lm-eval-harness`](https://github.com/EleutherAI/lm-evaluation-harness) framework.

This benchmark enables standardized, reproducible assessment of LLMs for climate-focused applications.

## 🔧 Setup Instructions

### 1. Clone This Repo

```bash
git clone https://github.com/NLP-RISE/ClimateEval.git
cd ClimateEval
```

### 2. Install [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness)

```bash
git clone https://github.com/EleutherAI/lm-evaluation-harness.git
cd lm-evaluation-harness
pip install -e .
```

### 3. Run an Evaluation

Example command (5-shot evaluation on `claim_binary` task):

```bash
lm_eval \
  --model hf \
  --model_args pretrained=eci-io/climategpt-7b \
  --tasks claim_binary \
  --output_path /results/climategpt-7b.jsonl \
  --show_config --log_samples \
  --num_fewshot 5 \
  --include_path <path-to-ClimateEval>/
```

To evaluate the **full ClimateEval suite**, use the tag:

```bash
--task ClimateEval
```

Or run by subsets, e.g.,:

```bash
--task CheapTalk,climatebert,climabench
```

## 🏷 Task Tags

| Tag           | Description                                                                                                                   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| `ClimateEval` | Full ClimateEval benchmark suite                                                                                              |
| `CheapTalk`   | Corporate climate discourse tasks based on this [paper](https://www.sciencedirect.com/science/article/pii/S0378426624001080) |
| `climatebert` | Tasks used to evaluate [ClimateGPT](https://arxiv.org/pdf/2401.09646)                                               |
| `climabench`  | Tasks from the [ClimaBench benchmark](https://arxiv.org/pdf/2301.04253v2)                                             

## 📄 Citation

If you use ClimateEval in your work, please cite:

```bibtex
@inproceedings{ClimateEval2025,
  title={ClimateEval: A Comprehensive Benchmark for NLP Tasks Related to Climate Change},
  author={Murathan Kurfali and Shorouq Zahra and Joakim Nivre and Gabriele Messori},
  booktitle={Proceedings of the 2nd Workshop of Natural Language Processing meets Climate Change (ClimateNLP 2025) at ACL 2025},
  year={2025}
}
```
