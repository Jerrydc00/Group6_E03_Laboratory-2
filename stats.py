def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    if not numbers:
        return 0
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    if len(modes) == len(numbers):  
        return 0
    return modes[0]  

def main():
    test_numbers = [1, 2, 2, 3, 4]
    print("Numbers:", test_numbers)
    print("Mean:", mean(test_numbers))
    print("Median:", median(test_numbers))
    print("Mode:", mode(test_numbers))

if __name__ == "__main__":
    main()
