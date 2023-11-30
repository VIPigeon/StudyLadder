
from collections import defaultdict, Counter


d = {}

tuple0 = (1, 2, 3)  # tuple, он же кортеж

d['12'] = 14
d.items()
d.keys()
d.values()
# print(d['12'])s
# print(d.get(1))
# print(d.get('12'))

text = "askf;adsv;asdkflsadv asdf"
counter = {}
for c in text:
    if counter.get(c):
        counter[c] += 1
    else:
        counter[c] = 1
print(counter)

for key, value in counter.items():
    print(key, value)


print("\nА теперь defaultdict:")

text = "askf;adsv;asdkflsadv asdf"
counter = defaultdict(int)
for c in text:
    counter[c] += 1
print(dict(counter))

for key, value in counter.items():
    print(key, value)

print("\nА теперь Counter:")
text = "askf;adsv;asdkflsadv asdf"
counter = Counter(text)
for key, value in counter.items():
    print(key, value)
