import matplotlib.pyplot as plt


def bar_chart(categories, values, title="Bar Chart"):
    plt.bar(categories, values)
    plt.title(title)
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.show()


def line_chart(x, y, title="Line Chart"):
    plt.plot(x, y, marker="o")
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def pie_chart(labels, values, title="Pie Chart"):
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title(title)
    plt.show()