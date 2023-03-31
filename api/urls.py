from django.urls import path
from views import BookCategoryListView


urlpatterns = [
    path('category-list/', BookCategoryListView.as_view() )
]