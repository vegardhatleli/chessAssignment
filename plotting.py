import random
import matplotlib.pyplot as plt
from more_itertools import sample


def DrawSimple(minValue, maxValue, mode, size):
    sample = []
    for _ in range(0, size):
        x = random.triangular(minValue, maxValue, mode)
        sample.append(x)
    return sample


def ProcessSample(sample):
    sample.sort()
    times = []
    counts = []
    count = len(sample)
    times.append(minValue)
    counts.append(count)
    for x in sample:
        times.append(x)
        count -= 1
        counts.append(count)
    return (times, counts)


minValue = 100
maxValue = 200
mode = 140
size = 100

sample1 = DrawSimple(minValue, maxValue, mode, size)
sample2 = DrawSimple(minValue, maxValue, mode, size)


times1, counts1 = ProcessSample(sample1)
times2, counts2 = ProcessSample(sample2)


plt.plot(times1, counts1, 'g')
plt.plot(times2, counts2, 'b')

plt.savefig("KaplanMeier.png")
plt.show()
