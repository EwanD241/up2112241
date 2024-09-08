from django.urls import path
from .views import calendar, new_entry, update, remove, all_entries

#Forms urls for the views
urlpatterns = [
    path('', calendar, name='calendar'),
    path('all_entries/', all_entries, name='all_entries'),
    path('new_entry/', new_entry, name='new_entry'),
    path('update/', update, name='update'),
    path('remove/', remove, name='remove'),
]