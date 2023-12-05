from utils import cache_and_read_input
import re


input = cache_and_read_input(5)


seeds_and_maps = re.findall(r":\s+(\d+(?:\s+\d+)+)", input)

seeds = seeds_and_maps[0].split()

print(f"All given seeds: {seeds}")

for seed_mapped in seeds:

    for i, mappings in enumerate(seeds_and_maps[1:3]):
        print(f"Mapping {i+1}:")
        # print(mappings.split('\n'))
        for i2, mapping in enumerate(mappings.split('\n')):

            mapping_set = mapping.split(' ')

            destination_range_start = mapping_set[0]
            source_range_start = mapping_set[1]
            range_length = mapping_set[2]

            # print(F"range length for {i+1}.{i2+1} is {range_length}")

            # destination_range_end = destination_range_start + range_length
            source_range_end = source_range_start + range_length

            if seed_mapped >= source_range_start and seed_mapped <= source_range_end:
                diff_from_start = seed_mapped - source_range_start
                new_seed_value = destination_range_start + diff_from_start


            

            # thinking if the seed_mapped is in range the do the mapping and update the seed_no in seeds







