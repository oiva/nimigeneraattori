# Nimigeneraattori

A Python script for generating Finnish (sounding) names. Collisions with real people are possible but rare.

## Command line usage

```
$ python generator.py

Ritwa Riistakäristys
```

Specify number of names to generate:
```
$ python generator.py -n 10

Lasse Lapio
Martina Mähönen
Lupu Tapaturma
Armo Astinlauta
Rantanen Rosmariini
Torvi Tyyrpuuri
Heimo Kypros
Hupu Hutilyönti
Anttooni Armenialainen
Orpana Orlando
```

Specify gender of name (female, male, unisex)
```
$ python generator.py -n 5 --gender female

Gertrud Graavilohi
Astrid Astuma
Tiiti Teboil
Kikke Kelomaa
Tove Tesla
```

Specify a seed: this is useful if you need to get the same output on a given input (for example SSN). Seed is cast into an integer.
```
$ python generator.py --seed 15

Jacce Janakkala

$ python generator.py --seed 15

Jacce Janakkala
```
