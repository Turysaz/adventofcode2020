
import re

with open("../inputs/day04.txt") as file:
    text = file.read()

def split_data(text: str) -> list:
    latest = ""
    for line in text.splitlines(keepends=False):
        latest += line + " "
        if(line == ""):
            yield latest
            latest = "" # reset
    yield latest # last line

def int_in_range(x: str, min: int, max: int, l: int) -> bool:
    return (min <= int(x) <= max) if x.isdigit() and len(x) == l else False

def hgt_is_valid(x: str) -> bool:
    if x[-2:] == "cm":
        return int_in_range(x[:-2], 150, 193, 3)
    elif x[-2:] == "in":
        return int_in_range(x[:-2], 59, 76, 2)
    else:
        return False

checkhandler_part1 = {
    "byr" : lambda x : 0x01,
    "iyr" : lambda x : 0x02,
    "eyr" : lambda x : 0x04,
    "hgt" : lambda x : 0x08,
    "hcl" : lambda x : 0x10,
    "ecl" : lambda x : 0x20,
    "pid" : lambda x : 0x40,
    "cid" : lambda x : 0x80
}

checkhandler_part2 = {
    "byr" : lambda x : 0x01 if int_in_range(x, 1920, 2002, 4) else 0,
    "iyr" : lambda x : 0x02 if int_in_range(x, 2010, 2020, 4) else 0,
    "eyr" : lambda x : 0x04 if int_in_range(x, 2020, 2030, 4) else 0,
    "hgt" : lambda x : 0x08 if hgt_is_valid(x) else 0,
    "hcl" : lambda x : 0x10 if re.match(r"\#[0-9a-f]{6}", x) != None else 0,
    "ecl" : lambda x : 0x20 if x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] else 0,
    "pid" : lambda x : 0x40 if len(x) == 9 and x.isdigit() else 0,
    "cid" : lambda x : 0x80
}

def count_valid(checkhandler: dict):
    req_mask = 0x7f
    valid = 0
    for data in split_data(text):
        checksum = sum(
            set(checkhandler[match.group("key")](match.group("val"))
                for match
                in re.finditer(r"(?P<key>\w{3}):(?P<val>[^\s]*)", data)))
        if (checksum & req_mask) == req_mask:
            valid += 1
    print ("Valid: {}".format(valid))

print("Part 1")
count_valid(checkhandler_part1)

print("Part 2")
count_valid(checkhandler_part2)
