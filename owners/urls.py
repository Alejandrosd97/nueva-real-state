from django.urls import path
from . import views
from django.contrib.auth import views as dj_views


urlpatterns = [
    path('register/', views.register, name='register_page'),
    path('selling/', views.selling_page, name='selling_page'),
    path('login/', views.login, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('my_properties/', views.my_properties, name='my_properties'),
    path('edit_add/<int:id>', views.edit_add, name='edit_add'),
    path('remove_picture/<int:id>', views.remove_picture, name='remove_picture'),
    path('add_picture/<int:id>', views.add_picture, name='add_picture'),
    path('remove_add/<int:id>', views.remove_add, name='remove_add'),
   
    path('lower_price/<int:id>', views.lower_price, name='lower_price'),
]

# path('send_email/', views.send_email, name='send_email'),
 #   path('send_email2/', views.send_email2, name='send_email2'),