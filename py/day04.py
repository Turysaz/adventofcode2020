
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

def part1():
    print("Part 1")
    fieldbits = {
        "byr" : 0x01,
        "iyr" : 0x02,
        "eyr" : 0x04,
        "hgt" : 0x08,
        "hcl" : 0x10,
        "ecl" : 0x20,
        "pid" : 0x40,
        "cid" : 0x80
    }
    req_mask = 0x7f
    c_valid = 0
    for data in split_data(text):
        checksum = 0
        for pair in re.finditer(r"(?P<key>\w{3}):(?P<val>\w*)", data):
            checksum += fieldbits[pair.group("key")]
        if (checksum & req_mask) == req_mask:
             c_valid += 1

    print ("Valid: {}".format(c_valid))

def part2():
    print("Part 2")

    def intbetween(x: str, min: int, max: int, length: int) -> bool:
        if not x.isdigit() or len(x) != length:
            return False
        
        return int(x) >= min and int(x) <= max

    def hgtvalid(x: str) -> bool:
        if x[-2:] == "cm":
            return intbetween(x[:-2], 150, 193, 3)
        elif x[-2:] == "in":
            return intbetween(x[:-2], 59, 76, 2)
        else:
            return False

    checkhandler = {
        "byr" : lambda x : 0x01 if intbetween(x, 1920, 2002, 4) else 0,
        "iyr" : lambda x : 0x02 if intbetween(x, 2010, 2020, 4) else 0,
        "eyr" : lambda x : 0x04 if intbetween(x, 2020, 2030, 4) else 0,
        "hgt" : lambda x : 0x08 if hgtvalid(x) else 0,
        "hcl" : lambda x : 0x10 if re.match(r"\#[0-9a-f]{6}", x) != None else 0,
        "ecl" : lambda x : 0x20 if x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] else 0,
        "pid" : lambda x : 0x40 if len(x) == 9 and x.isdigit() else 0,
        "cid" : lambda x : 0x80
    }

    req_mask = 0x7f
    valid = 0
    for data in split_data(text):
        checksum = 0
        for pair in re.finditer(r"(?P<key>\w{3}):(?P<val>[^\s]*)", data):
            k = pair.group("key")
            v = pair.group("val")
            checksum += checkhandler[k](v)
        if (checksum & req_mask) == req_mask:
            valid += 1
    print ("Valid: {}".format(valid))

part1()
part2()
