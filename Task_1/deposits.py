#!/usr/bin/env python3

USAGE = """USAGE: {script} percent fixed_period set_period
\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)
    return initial_sum * growth


def main(args):
    """Gets called when run as a script."""
    if 4 + 1 != len(args):
        exit(USAGE.format(script=args[0]))

    args = args[1:]
    initial_sum, percent, fixed_period, set_period = map(float, args)
    res = deposit(initial_sum, percent, fixed_period, set_period)
    mes = f'Якщо Ви покладете до нашого банку сумму {initial_sum}' \
          f' умовних одиниць під {percent} % на {fixed_period} ' \
          f'місяців, то через {set_period} місяців Ви отримаєте' \
          f' {round(res, 2)} умовних одиниць.'

    with open('proposition.txt') as inf:
        s1 = inf.read()
    print(s1)

    with open('result.txt', 'w') as ouf:
        ouf.write(mes)


if __name__ == '__main__':
    import sys

    main(sys.argv)
