# CS521 - A2
# Deependrasingh Shekhawat
# Script for Feet to meter

def footToMeter(foot):
    return 0.305 * foot


def meterToFoot(meter):
    return meter / 0.305


print(f"{'Feet':<8s} {'Meters':^7s} | {'Meters':^9s} {'Feet':}")

m = 16
for i in range(1, 11):
    m = m + (4 if i % 2 else 6)
    print(f"{i:<8.1f}  {footToMeter(i):>5.3f}  |  {m:<7.1f}  {meterToFoot(m):>.3f}")

