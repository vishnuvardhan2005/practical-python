# bounce.py
#
# Exercise 1.5

def bounce(h):
    for i in range(0,10):
        h = h *3/5
        print(round(h, 4))

bounce(100)