from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexCLassView.as_view(), name='index'),
    path("food/", include([
        path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
        path('item/', views.item, name='item'),
        path('add/', views.CreateItem.as_view(), name='create_item'),
        path('edit/<int:id>/', views.edit_item, name='edit_item'),
        path('delete/<int:id>/', views.delete_item, name='delete_item'),
    ])),
]
