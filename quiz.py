# function imports
import random
import os
import sys
import time


# set the right clear command for the platform
if sys.platform in ("linux", "darwin"):
    CLEAR = "clear"
elif sys.platform == "win32":
    CLEAR = 'cls'
else:
    exit(1)

# clear the terminal
def clear_terminal() -> None:
    os.system(CLEAR)

clear_terminal()

# DICTIONARY IMPORTANT:::
# identify what language feature is being shown!!!!!
# e.g:
# What language feature is this:
# “The car’s tires screeched as she slammed on the brakes.”
# (answer = onomatapoea)
# correct!!!!

questions = [
    "The car's tires screeched as she slammed on the brakes.",
    "This is a pivotal time to produce policy to protect our planet.",
    "What is the most important thing in the world? It is people, it is people, it is people.",
    "He took my pride and my dignity and my hope and my money. He needed to be punished.",
    "The wind whispered through the lonely house.",
    "He was her lighthouse in the storm.",
    "Her hair was like silk.",
    "The shirt was handed down \nTo me by my brother",
    "The scent of pine was carried on the wind; the trees moved from side to side beneath the warm sun.",
    "He felt so guilty; he took a shower hot enough to burn his skin off.",
    "Before you judge me, think — what would you have done in that situation?"
]

answers = [
    "onomatopoeia",
    "alliteration",
    "repetition",
    "listing",
    "personification",
    "metaphor",
    "simile",
    "enjambment",
    "sensorylanguage",
    "hyperbole",
    "rhetoricalquestion"
]

