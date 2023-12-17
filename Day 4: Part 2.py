from collections import Counter

path = '/home/ray/Documents/programming/python/coding problems/advent of code/day4_input.txt'
cards = open(path).read().splitlines()

points = 0
card_points = {}

for c,card in enumerate(cards,start=1):
    card_points[c] = 1

for i,card in enumerate(cards,start=1):
    c = card.split(':')[1:]
    count_cards = c[0].replace('|','')
    cc = count_cards.split()
    cc_match = len(cc) - len(set(cc))
    for point in range(1,cc_match+1):
        card_points[i+point] += card_points[i]

total = 0
for t in card_points:
    total += card_points[t]

print(total)
