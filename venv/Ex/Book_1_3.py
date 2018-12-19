import random

article = ["the", "on", "are", "there", "a", "on"]
substantive = ["cat", "dog", "man", "women", "car", "work", "home"]
verb = ["sang", "ran", "jumped", "going", "frendly", "kill"]
adverb = ["loudly", "quietly", "well", "badly", "many"]

def random_string():
    for item in range(5):
        line_out = ""
        case = random.randint(0, 1)
        if case == 0:
            line_out += random.choice(article) + " " + random.choice(substantive) + " " + random.choice(
                verb) + " " + random.choice(adverb)
            print(line_out)
        elif case == 1:
            line_out += random.choice(article) + " " + random.choice(substantive) + " " + random.choice(verb)
            print(line_out)