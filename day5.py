from utils import cache_and_read_input
import re


input = cache_and_read_input(5)


seeds_and_maps = re.findall(r":\s+(\d+(?:\s+\d+)+)", input)

seeds = [int(x) for x in seeds_and_maps[0].split()]

print(f"All given seeds: {seeds}")

for seed_index, seed_mapped in enumerate(seeds):
    next_mapping_found = False
    print(f"checking for seed no: {seed_mapped}")
    for mappings_index, mappings in enumerate(seeds_and_maps):
        print(f"Mapping set {mappings_index+1}:")
        # print(mappings.split('\n'))
        for mapping_index, mapping in enumerate(mappings.split('\n')):

            mapping_set = mapping.split(' ')
            print(f"Mapping {mapping_index}: {mapping_set}")
            destination_range_start = int(mapping_set[0])
            source_range_start = int(mapping_set[1])
            range_length = int(mapping_set[2])


            # destination_range_end = destination_range_start + range_length
            source_range_end = source_range_start + range_length - 1
            print(f"source start:{source_range_start}")
            print(f"source end: {source_range_end}")
            print(f"range length {range_length}")
            print(f"destination start{destination_range_start}")

            if seed_mapped >= source_range_start and seed_mapped <= source_range_end:
                print(f"New mapping found for seed {seed_mapped}")
                diff_from_start = seed_mapped - source_range_start
                print(f"Difference from source start: {diff_from_start} ")
                new_seed_value = destination_range_start + diff_from_start
                print(f"Therefore new value is {new_seed_value}")
                next_mapping_found = True
                seeds[seed_index] = new_seed_value
                print(f"New seed ")
                break

        if next_mapping_found:
            break

print(seeds)
