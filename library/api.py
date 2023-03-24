from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"books" , views.BookViewSet)
router.register(r"lib-users" , views.LibUserViewSet)
router.register(r"rented-books" , views.RentBookViewSet)