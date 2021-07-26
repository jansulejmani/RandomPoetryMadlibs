import random

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
noun = input("Noun: ")

madlib1 = f"The sky is falling upon a {adj} ground, \
with a dazzling beauty and startled cloud.\
 Love to {verb1}, stay to {verb2}.\
 Shining over the inevitable {noun}!"

madlib2 = f"Beauty is the {adj} way, \
let it be a certainty.\
 Ode to {verb1} the way, none gone to {verb2} the pavement.\
 Willful to be drawn about the {noun}."

madlib3 = f"Never between that {adj} passage, \
it's to be the very spirit.\
 Sober is to {verb1} through it all, has it not been given to {verb2} the revolution.\
 More the better as it used the {noun}."

switcher = {
1: madlib1,
2: madlib2,
3: madlib3
}

print(switcher.get(random.randint(1,3)))

