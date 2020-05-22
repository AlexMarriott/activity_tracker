import json
import matplotlib.pyplot as plt

from datetime import date
plt.style.use('ggplot')
today = str(date.today())

with open("{0}.json".format(today), "r") as file:
    data = json.load(file)
    x = []
    y = []
    for key, value in data[today].items():
        x.append(key)
        y.append(round(value%3600/60))
    print(x)
    print(y)

    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, y, color='green')
    plt.xlabel("Applications")
    plt.ylabel("Minutes")
    plt.title("Time spent on each application")

    plt.xticks(x_pos, x)

    plt.show()