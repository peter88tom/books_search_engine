from django.test import TestCase
from google_book.views import search_books
from admin.settings import API_KEY
import requests

# Create your tests here.
def test_search_books():

  # require parameters
  end_point = "https://www.googleapis.com/books/v1/volumes?"
  key_word = "Python"

  response = requests.get(f"{end_point}q={key_word}&key={API_KEY}")
  assert response.status_code == 200


