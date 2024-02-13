import requests
from send_email import send_email

# https://newsapi.org
api_key = "4fb701b80b1f418c92235d6c028bb1eb"

topic = "bitcoin"
url = f"https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      f"sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      f"language=en"

requests = requests.get(url)
content = requests.json()

print(content)

body = "Subject: Today's news of Python App" + "\n"
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
