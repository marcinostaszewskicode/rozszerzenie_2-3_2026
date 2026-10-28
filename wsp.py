import sys

if len(sys.argv) == 2:
    file = open(f"{sys.argv[1]}.in")
    line1 = file.readline().strip()
    line2 = file.readline().strip()
else:
    line1 = input()
    line2 = input()

def wsp(line1, line2):
    powers = list(map(int, line2.split()))
    ten_best = []

    for i in range(10):
        max_power = powers[0]
        for power in powers:
            if power > max_power:
                max_power = power
        ten_best.append(max_power)
        powers.remove(max_power)
    print(' '.join(str(x) for x in ten_best))

wsp(line1, line2)
