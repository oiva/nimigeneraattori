# Nimigeneraattori

A Python script for generating Finnish (sounding) names. Collisions with real people are possible but rare.

## Command line usage

```
$ python generator.py

Make Mastodontti
```

Specify number of names to generate:
```
$ python generator.py -n 5

Pertti Peistamo
Kataja Kennel
Ben Boston
Roine Rymy-Eetu
Hyvä Utö
```

Specify sex (female, male, unisex)
```
$ python generator.py --sex female

Martina Mastodontti
```

Specify a seed: this is useful if you need to get the same output on a given input (for example SSN). Seed is cast into an integer.
```
$ python generator.py --seed 15

Jacce Janakkala
```
