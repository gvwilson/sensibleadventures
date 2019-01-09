#!/usr/bin/env python

ways = {}
rolls = range(1, 7)
for i in rolls:
    for j in rolls:
        for k in rolls:
            score = i + j + k
            ways[score] = ways.get(score, 0) + 1

base = 6 ** 3
values = sorted(ways.keys())
accum = {}
total = 0
print('| Number | # Ways to Roll | %age Roll | # Get or Less | %age Get or Less |')
print('| ------ | -------------- | --------- | ------------- | ---------------- |')
for v in values:
    total += ways[v]
    accum[v] = total
    ways_p = 100 * ways[v] / base
    accum_p = 100 * accum[v] / base
    miss = base - total
    print(f'| {v : 6} | {ways[v] : 14} | {ways_p : 8.1f}% | {accum[v] : 13} | {accum_p : 15.1f}% |')

print()

bonuses = range(-7, 9)
upper = 3 * 6 + 3
print('| Bonus | Roll Needed | # Ways to Win |  % Win  |')
print('| ----- | ----------- | ------------- | ------- |')
for bonus in bonuses:
    needed = 11 - bonus
    get = accum[upper - needed]
    win = 100 * get / base
    print(f'| {bonus : >+5} | {needed : 11} | {get : 13} | {win : 6.1f}% |')

