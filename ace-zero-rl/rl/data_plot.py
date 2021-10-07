import matplotlib.pyplot as plt
import numpy as np

num_lines = 5000
with open("../global-log.txt") as f:
    #data = f.read()
    data = [next(f) for x in range(num_lines)]

#data = data.split('\n')

delta = [row.split(',')[1] for row in data]
q46 = [row.split(',')[2] for row in data]

tick = list(range(len(delta)))

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Plot title2...")    
ax1.set_xlabel('your x label..')
ax1.set_ylabel('your y label...')



ax1.plot(tick, delta, 'r--', tick, q46, 'b--')


leg = ax1.legend()

plt.show()