from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home_page' ),
    path('houses_per_city/<int:id>/<str:availability>', views.houses_per_city, name='houses_per_city'),
    path('houses_detail/<int:id>', views.house_detail, name='house_detail'),
    path('like_page/<int:id>', views.like_page, name='like_page'),
    path('dislike_page/<int:id>', views.dislike_page, name='dislike_page'),
    path('favourites', views.favourites, name='favourites_page'),
    path('contact_form/<int:id>', views.contact_owner_form, name='contact_form'),

]

