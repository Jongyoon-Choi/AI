POPULATION_SIZE=(40 50)
MUTATION_RATE=(0.05)
SIZE=998
TARGET_VAL=100
MAX_VAL=400
max_iter=1000
crossover_name=(order positon_based uniform_order_based pmx cycle edge_recom)

output_dir="GA_result"
mkdir -p "$output_dir"

for crossover in "${crossover_name[@]}"; do
  for POPULATION_SIZE in "${POPULATION_SIZE[@]}"; do
    for MUTATION_RATE in "${MUTATION_RATE[@]}"; do
            output_path="$output_dir/${crossover}_${POPULATION_SIZE}pop_${MUTATION_RATE}mut"
            python3 GA.py \
                --POPULATION_SIZE $POPULATION_SIZE \
                --MUTATION_RATE $MUTATION_RATE \
                --SIZE $SIZE \
                --TARGET_VAL $TARGET_VAL \
                --MAX_VAL $MAX_VAL \
                --max_iter $max_iter \
                --crossover_name "$crossover" \
                --output_path "$output_path" &
    done
  done
done

wait  # 모든 백그라운드 작업이 완료될 때까지 대기