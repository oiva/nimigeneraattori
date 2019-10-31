"""Generate Finnish names."""

import argparse
from random import choice, random, randrange, sample, seed
from re import compile


def read_name_file(filename):
    """Read names from a file containing one name per line."""
    with open(filename, 'r') as f:
        names = f.read()
        names = names.split('\n')
        names = list(filter(None, names))
        return names


def generate(amount, gender=None, force_seed=None):
    """Generate a number <amount> of names."""
    names = []
    for i in range(0, amount):
        seed(force_seed)
        first_name = get_first_name(gender)
        last_name = get_last_name(first_name)

        names.append(first_name + ' ' + last_name)

    return names


def get_first_name(gender=None):
    """Return a random name from list of first names."""
    if gender is None:
        gender = choice(['male', 'female', 'unisex'])
    if gender == 'male':
        return male_first_names[randrange(0, len(male_first_names))]
    elif gender == 'female':
        return female_first_names[randrange(0, len(female_first_names))]
    else:
        return unisex_first_names[randrange(0, len(unisex_first_names))]


def get_last_name(first_name):
    """Pick a random last name that probably fits the first name."""
    """Order last names so that names closest to first name are first.
       For example first name "Kikke" -> last names should be "Kilari",
       "Kolari", [all other names by random]"""
    def name_comparator(last_name):
        """Return a number describing how close the two names are."""
        score = 0

        # check if first n letters of first and last name matches
        for i in range(1, 4):
            if len(first_name) >= i and len(last_name) >= 2:
                # if previous letter does not match, don't continue
                if i > 1 and score > (i - 1) * -1:
                    break

                # lower score by one per each matching letter
                if first_name[i - 1: i] == last_name[i - 1: i]:
                    score -= 1

        """detect names with umlauts and give them higher score if both have
           them, lower score if only one has them."""
        regex = compile(r'[äöå]')
        if score == 0:
            if regex.search(first_name) and regex.search(last_name):
                score -= 1
        else:
            if bool(regex.search(last_name)) != bool(regex.search(last_name)):
                score += 1

        return score

    last_names_random = sample(last_names, len(last_names))
    last_names_sorted = sorted(last_names_random, key=name_comparator)

    """Walk through names and check on each name if you should stop. Since
       the matching names are first they are more likely to be selected."""
    for i in range(0, 10):
        if random() >= 0.7:
            return last_names_sorted[i]

    return last_names_sorted[0]


parser = argparse.ArgumentParser(description='Generate names')
parser.add_argument("-n", default=1, help="Number of names to generate")
parser.add_argument("--gender", default=None,
                    help="Gender of name (male, female, unisex)"
                    )
parser.add_argument("--seed", default=None, help="Custom seed for random")

args = parser.parse_args()
n = int(args.n)
gender = args.gender
custom_seed = args.seed

male_first_names = read_name_file('data/firstnames-men.txt')
female_first_names = read_name_file('data/firstnames-women.txt')
unisex_first_names = read_name_file('data/firstnames-unisex.txt')
last_names = read_name_file('data/lastnames.txt')

# test how unique the names are
names = []
for i in range(0, n):
    name = generate(1, gender, custom_seed)
    name = name[0]
    if name not in names:
        names.append(name)


print("\n".join(names))
