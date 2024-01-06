from django.urls import path, re_path
from lists import views


urlpatterns = [
    re_path(r'(\d+)/$', views.view_list, name='view-list'),
    re_path(r'(\d+)/add_item$', views.add_item, name='add-item'),
    path('new', views.new_list, name='new-list'),
]