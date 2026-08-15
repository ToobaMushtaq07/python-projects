import requests
import matplotlib.pyplot as plt

# Fetch JSON data from API
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Take the first 10 posts
    posts = data[:10]

    # Get post IDs and titles
    post_ids = [post["id"] for post in posts]
    title_lengths = [len(post["title"]) for post in posts]

    # Create a bar chart
    plt.bar(post_ids, title_lengths)

    plt.title("Title Length of First 10 Posts")
    plt.xlabel("Post ID")
    plt.ylabel("Title Length")
    plt.show()

else:
    print("Failed to fetch data")
    print("Status code:", response.status_code)