from requests import get

Websites = (
    "googel.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tictoc.com"
)

for website in Websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    print(response)
numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8,
           "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]
