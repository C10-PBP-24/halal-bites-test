from django.urls import path
from resto.views import get_resto, show_resto, filter_resto, add_resto
from resto.views import delete_resto

app_name = "resto"

urlpatterns = [
    path('', show_resto, name="show_resto"),
    path('filter-resto/', filter_resto, name='filter_resto'),
    path('add-resto/', add_resto, name='add_resto'),
    path('delete-resto/<int:id>/', delete_resto, name="delete_resto")
]