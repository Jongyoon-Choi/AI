POPULATION_SIZE=(50 60)
MUTATION_RATE=(0.05)
SIZE=998
MAX_VAL=420
iteration=500
crossover_name=(order)

output_dir="GA_result"
mkdir -p "$output_dir"

for crossover in "${crossover_name[@]}"; do
  for pop_size in "${POPULATION_SIZE[@]}"; do
    for mutation_rate in "${MUTATION_RATE[@]}"; do
            output_path="$output_dir/${crossover}_${pop_size}pop_${mutation_rate}mut"
            python3 -u GA.py \
                --POPULATION_SIZE $pop_size \
                --MUTATION_RATE $mutation_rate \
                --SIZE $SIZE \
                --MAX_VAL $MAX_VAL \
                --iteration $iteration \
                --crossover_name "$crossover" \
                --output_path "$output_path" > "$output_path.log" 2>&1 &
    done
  done
done

wait  # 모든 백그라운드 작업이 완료될 때까지 대기