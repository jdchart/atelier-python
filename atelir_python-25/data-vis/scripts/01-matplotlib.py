"""
01 Matplotlib

Basic visualisation.

plt.savefig("output/image.png") to save to image.
"""

import matplotlib.pyplot as plt
import utils

src = "data-vis/data/basic-data.csv"

def process(data_source):
    data = utils.read_csv(data_source)
    data = utils.convert_to_int(data)

    line_plot_simple(data)
    line_plot_subplot(data)

    scatter_plot(data)
    bar_plot(data)
    pie_plot(data)

    plot_3d(data)

def line_plot_simple(data):
    
    plt.plot(data[0], data[1])
    
    plt.xlabel("Hello")
    plt.ylabel("World")
    plt.title("My amazing plot")
    plt.ylim([0, 100])

    plt.show()

def line_plot_subplot(data):
    graph, subplot = plt.subplots(1, 1)
    
    subplot.plot(data[0], data[1])
    
    subplot.set_xlabel("Hello")
    subplot.set_ylabel("World")
    subplot.set_title("My amazing plot")
    subplot.invert_yaxis()

    graph.tight_layout()
    plt.show()

def scatter_plot(data):
    plt.scatter(data[0], data[1])
    plt.show()

def bar_plot(data):
    graph, subplot = plt.subplots(1, 1)
    
    subplot.bar(data[0], data[1])
    #subplot.invert_yaxis()

    graph.tight_layout()
    plt.show()

def pie_plot(data):
    plt.pie(data[1], labels=data[0])
    plt.show()

def plot_3d(data):
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(data[0], data[1], data[2])

    ax.view_init(elev=20., azim=-35, roll=0)

    plt.show()

process(src)