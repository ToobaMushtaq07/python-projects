import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 140, 200, 230]

# Bar Chart
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Line Chart
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Pie Chart
products = ["Laptop", "Phone", "Tablet", "Headphones"]
product_sales = [40, 30, 20, 10]

plt.pie(product_sales, labels=products, autopct="%1.1f%%")
plt.title("Product Sales - Pie Chart")
plt.show()