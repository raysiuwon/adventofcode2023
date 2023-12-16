from collections import Counter

path = '../advent of code/day4_input.txt'
cards = open(path).read().splitlines()

points = 0

from collections import Counter
for card in cards:
    c = card.split(':')[1:]
    count_cards = c[0].replace('|','')
    cc = count_cards.split()
    cc_points = Counter(cc)
    total = [cc_points[k] for k in cc_points]
    if total.count(2) >= 1:
        points += (1*2**(total.count(2)-1))

print(points)
