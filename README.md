# ClimateGPT Evaluation

Prompt templates for climate-specific tasks can be found under `tasks`.  

#### To evaluate an LLM on climate-specific tasks, follow the steps below:  
1. Clone this repo 
2. Clone and install [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/)
Pass the paths to the tasks as command-line arguments using `--include_path`. An example command is shown below:  
       
        lm_eval \
        	--model hf \
        	--model_args pretrained=tiiuae/falcon-7b \
        	--tasks claim_binary \
        	--output_path /results/falcon-7b.jsonl \
        	--show_config --log_samples \
        	--num_fewshot 5 --include_path <path/to/this/repo/tasks/exeter>




   
      






