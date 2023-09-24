from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:item_id>/', views.FoodDetail.as_view(), name='detail'),
    path('item/', views.item, name='item'),
    path('add/', views.CreateItem.as_view(), name='create_item'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
