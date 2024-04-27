#!/bin/bash

POPULATION_SIZE=(30 40 50)
MUTATION_RATE=(0.1 0.05 0.01)
SIZE=20
TARGET_VAL=4
max_iter=5000

output_dir="GA_result"
mkdir -p "$output_dir"

for POPULATION_SIZE in "${POPULATION_SIZE[@]}"; do
  for MUTATION_RATE in "${MUTATION_RATE[@]}"; do
            output_file="$output_dir/${POPULATION_SIZE}_pop${MUTATION_RATE}_mut${k}.log"
            python3 GA copy.py \
                --POPULATION_SIZE "$POPULATION_SIZE" \
                --MUTATION_RATE "$MUTATION_RATE" \
                --SIZE "$SIZE" \
                --TARGET_VAL "$TARGET_VAL" \
                --max_iter "$max_iter" 2>&1 & 
  done
done

wait  # 모든 백그라운드 작업이 완료될 때까지 대기