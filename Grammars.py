import random as rd

# Our Grammar rules
rules = {
    "S":[ 
        ["The", "N", "V"] 
    ], 
    "N":[ 
        ["cat"],
        ["dog"],
        ["tiger"]
    ],
    "V":[ 
        ["Adj", "meow", "cat"],
        ["Adj","barks", "A"],
        ["Adj","moo", "A"]
    ],
    "Adj": [
        ["Stinky"]
    ],
    "A": [
        ["and", "the", "black", "N", "sings"]
    ]
}

# Contributed by Tigermoo
def generate_items(items):
    for item in items:
        if isinstance(item, list):
            for subitem in generate_items(item):
                yield subitem
        else:
            yield item       

# Our expansion algo
def expansion(start):
    for element in start:
        if element in rules:
            loc = start.index(element)
            start[loc] = rd.choice(rules[element])
        result = [item for item in generate_items(start)]

    for item in result:
        if not isinstance(item, list):
            if item in rules:
                result = expansion(result)
    
    return result



raw = ["S"]
result = [item for item in generate_items(raw)]
print(result)
result = expansion(result)
print(result)

    