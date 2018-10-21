import random as rd

# Example Grammar rules
rules = {
    "S":[ 
        ["The", "N", "V"] 
    ], 
    "N":[ 
        ["Adj","cat"],
        ["Adj","dog"],
        ["Adj","tiger"]
    ],
    "V":[ 
        ["meows", "A"],
        ["barks", "A"],
        ["moos", "A"]
    ],
    "Adj": [
        ["Stinky"],
        ["Giant"],
        ["Blue"]
    ],
    "A": [
        ["and", "the", "N", "Va"]
    ],
    "Va": [
        ["sings"],
        ["yawns"],
        ["eats grass"]
    ]
}

# Contributed by Tiger Sachase
# Used to parse any list of strings and insert them in place in a list 
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


# An example test you can run to see it at work
result = ["S"]
print(result) # Print our starting result
result = expansion(result) # Expand our starting list 
print(result) # Print the final result

    