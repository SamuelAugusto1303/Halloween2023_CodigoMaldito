toys = ["Sapo", "Aranha", "Fantasma", "Bruxinha", "Dentadura"]
children = ["Samuel", "Franklin", "Hellen", "JC", "Daniel"]

child_toy = {"Samuel": "Sapo"}

child_toy["Hellen"] = "Fantasma"

child_toy["Daniel"] = "Dentadura"

for child in children:
    if child != "Franklin" and child != "Samuel" and child != "Hellen" and child != "Daniel":
        child_toy[child] = "Bruxinha"

remaining_toys = [toy for toy in toys if toy not in child_toy.values()]
remaining_children = [child for child in children if child not in child_toy.keys()]

for i, child in enumerate(remaining_children):
    child_toy[child] = remaining_toys[i]

for child, toy in child_toy.items():
    print(f"{child}: {toy}")