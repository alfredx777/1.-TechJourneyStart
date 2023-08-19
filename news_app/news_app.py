import requests

API_KEY = "ENTER API_KEY"

def get_news_headlines(category):
    """Gets the top news headlines from the News API for a given category."""
    url = "https://newsapi.org/v2/top-headlines?country=us&category={}".format(category)
    headers = {
        "Authorization": "Bearer {}".format(API_KEY)
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    articles = data["articles"]
    return articles[:2]

def print_news_headlines(articles):
    """Prints the top news headlines."""
    for article in articles:
        print(f"Headline: {article['title']}\nDescription: {article['description']}\n\n")

def main():
    category = input("Enter category: ")
    articles = get_news_headlines(category)
    print_news_headlines(articles)

if __name__ == "__main__":
    main()
