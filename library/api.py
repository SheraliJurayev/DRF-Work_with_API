from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"books" , views.BookViewSet , basename= 'books')
router.register(r"lib-users" , views.LibUserViewSet)
router.register(r"rented-books" , views.RentBookViewSet)


for url in router.urls :
    print(url , '/n')