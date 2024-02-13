import requests


def get_review(book_title, api_key):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    book_title = book_title.replace(" ", "+")
    print(book_title)
    params = {"q": f"intitle:{book_title}"}
    # params = {"q": f"isbn:{book_title}, key:{api_key}"}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
        if "items" in data and data["items"]:
            book_info = data["items"][0]["volumeInfo"]
            if "averageRating" in book_info and "ratingsCount" in book_info:
                average_rating = book_info["averageRating"]
                ratings_count = book_info["ratingsCount"]
                return average_rating, ratings_count

    print(response.status_code)
    return None, None
