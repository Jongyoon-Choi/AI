POPULATION_SIZE=(50)
MUTATION_RATE=(0.005 0.01) 
SIZE=998
MAX_VAL=420
iteration=2000
# crossover_name: order, position_based, uniform_order_based, pmx, cycle
crossover_name=(uniform_order_based)

for crossover in "${crossover_name[@]}"; do
  output_dir="GA_result/${crossover}"
  mkdir -p "$output_dir"
  for pop_size in "${POPULATION_SIZE[@]}"; do
    for mutation_rate in "${MUTATION_RATE[@]}"; do
            output_path="$output_dir/${pop_size}pop_${mutation_rate}mut_${iteration}iter"
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