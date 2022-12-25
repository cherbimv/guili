python interactive_conditional_samples.py --device 0 \
--topk 3 \
--topp 0.95 \
--dirty_path data/dirty_words.txt \
--model_name_or_path kuakua_robot_model \
--repetition_penalty 1.2 \
--max_len 33 \
--no_cuda True