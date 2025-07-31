# xInjectAgent

`xInjectAgent` is a customized version of [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) for generating attack prompts. 
It provides an extensible framework to evaluate LLM agent robustness against tool-based indirect prompt injections, logic overrides, and complex chained attack scenarios.

## 🔐 Set Up OpenAI API Key

Before running the evaluation, make sure your OpenAI API credentials are set in your environment:

```bash
export OPENAI_API_KEY=your-api-key-here
```

## 🧪 How to Use

### Step 1: Generate Attack Test Cases

Edit `test.py` to ensure it uses the **test** setting and outputs test case files to:

* `data/test_cases_dh_test.json` for Direct Harm
* `data/test_cases_ds_test.json` for Data Stealing

Then run:

```bash
python3 test.py
```

---

---

### Step 2: Run Evaluation

Now evaluate your model against the test cases:

```bash
python -m src.evaluate_prompted_agent \
  --model_type GPT \
  --model_name gpt-3.5-turbo \
  --setting test \
  --prompt_type InjecAgent \
```

---

All options are (change model name changing MODEL_NAME)
```bash
usage: evaluate_prompted_agent.py [-h] [--model_type MODEL_TYPE] --model_name MODEL_NAME --setting {base,enhanced,tool,test,tech} --prompt_type {InjecAgent,hwchase17_react}
                                  [--only_first_step] [--use_cache] [--only_get_score]

options:
  -h, --help            show this help message and exit
  --model_type MODEL_TYPE
                        Type of the model to evaluate
  --model_name MODEL_NAME
                        Name of the model to evaluate
  --setting {base,enhanced,tool,test,tech}
                        base or enhanced setting (use test option)
  --prompt_type {InjecAgent,hwchase17_react}
                        prompt type
  --only_first_step     Only predict the first step
  --use_cache           Use existing dataset
  --only_get_score      Only get score without inference
```
