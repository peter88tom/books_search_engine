from django.shortcuts import render
import requests
from admin.settings import API_KEY

# Create your views here.
def index(request):
  return render(request, 'google_book/index.html')



def search_books(request):
  end_point = "https://www.googleapis.com/books/v1/volumes?"
  key_word=request.GET["search"]

  res = requests.get(f"{end_point}q={key_word}&key={API_KEY}")
  books = res.json()

  queried_book = []

  for book in books['items']:
    k = {
      "book_title":book['volumeInfo']['title'],
      "authors":(book['volumeInfo']['authors'])[0],
      'cover':book['volumeInfo']['imageLinks']['smallThumbnail'],
      'link': book['volumeInfo']['previewLink'],
    }
    queried_book.append(k)

  #print(queried_book)

  return render(request, 'google_book/index.html',{"books":queried_book})

