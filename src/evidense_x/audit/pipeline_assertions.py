from typing import Set

def assert_zero_partition_leakage(overlap_set: Set):
    if len(overlap_set) > 0:
        raise AssertionError(f"Leakage detected! Found {len(overlap_set)} cross-partition observations.")
