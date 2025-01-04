def mode(numbers):
    if not numbers:
        return 0
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    if len(modes) == len(numbers):  # No mode if all numbers are equally frequent
        return 0
    return modes[0] 
