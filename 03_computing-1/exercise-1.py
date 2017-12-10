"""
Analyzing a simple dice game
"""

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """

    ans = set([()])

    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp

    return ans

def max_repeats(seq):
    """
    Compute the maxium number of times that an outcome is repeated
    in a sequence
    """
    item_count = [seq.count(item) for item in seq]
    return max(item_count)


def compute_expected_value(all_possible_permutations):
    """
    Function to compute expected value of simple dice game
    """
    num_permutations = float(len(all_possible_permutations))

    results = [max_repeats(permutation) for permutation in all_possible_permutations]

    sum_of_scores = 0

    for result in results:
        if result == 2:
            sum_of_scores += 10
        elif result == 3:
            sum_of_scores += 200

    return sum_of_scores / num_permutations


def run_test():
    """
    Testing code, note that the initial cost of playing the game ($10)
    has been ignored
    """
    outcomes = set([1, 2, 3, 4, 5, 6])
    all_possible_permutations = gen_all_sequences(outcomes, 3)
    print "All possible sequences of three dice are:"
    print all_possible_permutations
    print "(%s possible permutations in total)" % len(all_possible_permutations)
    print
    print "Test for max repeats"
    print "Max repeat for (3, 1, 2) is", max_repeats((3, 1, 2))
    print "Max repeat for (3, 3, 2) is", max_repeats((3, 3, 2))
    print "Max repeat for (3, 3, 3) is", max_repeats((3, 3, 3))
    print
    print "Ignoring the initial $10, the expected value was $", compute_expected_value(all_possible_permutations)

run_test()
