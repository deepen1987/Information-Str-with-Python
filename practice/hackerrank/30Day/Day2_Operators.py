
import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(meal, tip, tax):
    tip = meal * (tip/100)
    tax = meal * (tax/100)
    return meal+tip+tax


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(round(solve(meal_cost, tip_percent, tax_percent)))