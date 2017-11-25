"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """

    # create a list of zeros, the same length
    # as line
    result = [0] * len(line)

    # iterate through the nums in line, adding
    # any non-zeros to result and allowing each
    # num to be merged once with a previous num
    # if they are identical
    result_pos = 0
    prev_merged = False

    for num in line:
        # skip zeros in line because result already
        # contains zeros
        if num != 0:

            # if we're at the 2nd num or later, and
            # didn't do a merge on the last num, then
            # attempt a merge of this num
            if result_pos > 0 and not prev_merged:
                prev_num = result[result_pos-1]

                # can only merge identical nums...
                if num == prev_num:
                    result[result_pos-1] = num + prev_num

                    # set prev_merged flag to ensure
                    # a merge is never attempted more
                    # than once on each num
                    prev_merged = True

                else:
                    result[result_pos] = num
                    result_pos += 1

                    prev_merged = False

            else:
                result[result_pos] = num
                result_pos += 1

                prev_merged = False

    return result

# Tests

def test(test_num, line, result):
    if merge(line) == result:
        print "test " + str(test_num) + ": pass"
    else:
        print "test " + str(test_num) + ": fail"
        print "- expected: " + str(result)
        print "-   result: " + str(merge(line))

test(1, [2, 0, 2, 4], [4, 4, 0, 0])
test(2, [0, 0, 2, 2], [4, 0, 0, 0])
test(3, [2, 2, 0, 0], [4, 0, 0, 0])
test(4, [2, 2, 2, 2, 2], [4, 4, 2, 0, 0])
test(5, [8, 16, 16, 8], [8, 32, 8, 0])
