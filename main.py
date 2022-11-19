homerseklet = [0, 12, 13, 9, 2, 7]
day = ["október 1", "október 2", "október 3", "október 4", "október 5", "október 6"]
i = 0
"""while i < len(homerseklet)-1:
    if (homerseklet[i] - homerseklet[i + 1] > 3):
        print(day[i])
    i += 1"""

while (i < len(homerseklet)-1) and (homerseklet[i] - homerseklet[i + 1] <= 3):
    i += 1
if (i < len(homerseklet)-1):
    print(day[i])
else:
    print("nincs ilyen nap")

