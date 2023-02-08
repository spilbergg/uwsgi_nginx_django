from django.urls import path

from json_file_parser.views import get_data, get_form, post_form

urlpatterns = [
    path('', get_form, name='get_form'),
    path('get_data/', get_data, name='get_data'),
    path('post_form/', post_form, name='post_form'),

]
