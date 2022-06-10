from django.urls import path
from posts_app import views

app_name = 'posts_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('drafts/', views.DraftsListView.as_view(), name='drafts'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/new', views.ProductCreateView.as_view(), name='product_new'),
    path('product/update/<int:pk>', views.ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/newrequest', views.BuyRequestCreateView.as_view(), name='request_add'),
    path('product/buyrequest/<int:pk>/edit', views.BuyRequestUpdateView.as_view(), name='request_edit'),
    path('product/buyrequest/<int:pk>/delete', views.BuyRequestDeleteView.as_view(), name='request_delete'),

    
    path('product/<int:pk>/publish', views.product_publish, name='product_publish'),
    path('productrequest/<int:pk>/sell', views.product_sell, name='product_sell'),
]