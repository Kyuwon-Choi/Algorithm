import sys
from collections import deque

input = sys.stdin.readline

rome1 = input().strip()
rome2 = input().strip()

convert_table = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}


def convert_rome_to_arabia(rome):
    arabia = 0
    i = 0
    while i < len(rome):
        if i < len(rome) - 1 and rome[i] + rome[i + 1] in convert_table.keys():
            arabia += convert_table[rome[i] + rome[i + 1]]
            i += 2
        else:
            arabia += convert_table[rome[i]]
            i += 1

    return arabia


def convert_arabia_to_rome(arabia):
    rome = ""
    for key, value in convert_table.items():
        if arabia // value >= 1:
            rome += key * (arabia // value)
            arabia %= value
        if arabia == 0:
            break
    return rome


arabia1=convert_rome_to_arabia(rome1)
arabia2=convert_rome_to_arabia(rome2)
sum_arabia=arabia1+arabia2
sum_rome=convert_arabia_to_rome(sum_arabia)
print(sum_arabia)
print(sum_rome)