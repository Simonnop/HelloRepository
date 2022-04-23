"""
This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import random
import tqdm

def has_duplicates(t):
    """Returns True if any element appears more than once in (t),
    False otherwise."""
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length (n)."""
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(students, samples):
    """Generates (samples) samples of (students) students, and counts
    how many of them have at least one pair of students with the same bday."""
    count = 0
    for i in tqdm.trange(samples):
        t = random_bdays(students)
        if has_duplicates(t):
            count += 1
    return count

"""run the birthday simulation 1000 times and print the number of matches"""
num_students = 23
num_simulations = 1000000
count = count_matches(num_students, num_simulations)

print('After {} simulations'.format(num_simulations))
print('with {} students'.format(num_students))
print('there were {} simulations with at least one match'.format(count))
