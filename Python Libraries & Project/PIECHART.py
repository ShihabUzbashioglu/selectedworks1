import matplotlib.pyplot as plt

labels = ("python","java","scala","c#","c++","erlang")

sizes = [45,20,15,20]

pyplot.pie(sizes,
           labels=labels.autopct='%1.f%%',
           counterClock=False,startangle=105)

pyplot.show()