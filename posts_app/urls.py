from django.urls import path
from posts_app import views

app_name = 'posts_app'

urlpatterns = [
    # path(r'^$',)
    path('', views.IndexView.as_view(), name='index'),
]