"""Generate Finnish names."""
from random import random, randrange, sample
from re import compile


with open('data/firstnames.txt', 'r') as f:
    firstNames = f.read()
    firstNames = firstNames.split('\n')
    firstNames = list(filter(None, firstNames))

with open('data/lastnames.txt', 'r') as f:
    lastNames = f.read()
    lastNames = lastNames.split('\n')
    lastNames = list(filter(None, lastNames))


def generate(amount):
    """Generate a number <amount> of names."""
    names = []
    for i in range(0, amount):
        first_name = get_first_name()
        last_name = get_last_name(first_name)

        names.append(first_name + ' ' + last_name)

    return names


def get_first_name():
    """Return a random name from list of first names."""
    return firstNames[randrange(0, len(firstNames))]


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

    last_names_random = sample(lastNames, len(lastNames))
    last_names_sorted = sorted(last_names_random, key=name_comparator)

    """Walk through names and check on each name if you should stop. Since
       the matching names are first they are more likely to be selected."""
    for i in range(0, 10):
        if random() >= 0.5:
            return last_names_sorted[i]

    return last_names_sorted[0]


names = generate(3)
print(names)
