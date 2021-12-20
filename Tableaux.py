import array
import time

start = time.time() * 1000

print(start)
tab_voyelles = array.array('u')
voyelles = ["a", "e", "i", "o", "u"]
i = y = 0

while i < len(voyelles):
    if y < 1000000:
        y += 1
        continue

    tab_voyelles.append(voyelles[i])
    i += 1


print(tab_voyelles)
stop = time.time() * 1000
print(stop)

print(stop - start)

