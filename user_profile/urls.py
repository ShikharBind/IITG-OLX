from django.urls import path
from user_profile import views

app_name = 'user_profile'

urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='user_login'),
    path('', views.user_getID, name='user'),
    path('<int:pk>', views.ProfileDetailView.as_view(), name='user_data'),
    path('new/', views.CreateProfileView.as_view(), name='create_data'),
    path('update/<int:pk>', views.UpdateProfileView.as_view(), name='update_data'),
    # path('delete/<int:pk>', views.ProfileDeleteView.as_view(), name='delete_data'),


    path('product/<int:pk>/wishlistadd', views.product_add_to_wishlist, name='wishlist_add'),
    path('product/<int:pk>/wishlistremove', views.product_remove_from_wishlist, name='wishlist_remove'),
]