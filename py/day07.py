import re

with open("../inputs/day07.txt") as file:
    lines = file.readlines()

rules = {}
for l in lines:
    rules[re.match(r"(?P<name>\w+ \w+) bags contain", l).group("name")] = [
            (match.group("name"), int(match.group("count")))
            for match in re.finditer(r"(?P<count>\d+) (?P<name>\w+ \w+) bag", l)
        ] if "contain no other bags" not in l else []

def hold_gold(color: str) -> bool:
    inner = [name for (name, _) in rules[color]]
    if inner == []:
        return False
    return True if "shiny gold" in inner else any(hold_gold(x) for x in inner)

def weight(color: str) -> int:
    return sum([count * weight(name) + count for (name, count) in rules[color]])

print("Part 1: %i" % sum(int(hold_gold(x)) for x in rules))
print("Part 2: %i" % weight("shiny gold"))
