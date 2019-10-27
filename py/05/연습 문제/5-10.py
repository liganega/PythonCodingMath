event1 = 0
event2 = 0
event3 = 0
for x in range(1,7):
    for y in range(1,7):
        if x+y <= 6:
            event1 += 1
        if x-y == 3:
            event2 += 1
        if (y == x-2) and (y > -x + 7):
            event3 += 1
print (event1, event2, event3)