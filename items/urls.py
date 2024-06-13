from django.urls import path
from .views import *

app_name = 'items'

urlpatterns = [
    path('', ItemsListView.as_view(), name='items'),
    path('category/<int:pk>/<name>/', ItemsByCategoryListView.as_view(), name='category'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    path('search/', SearchItemView.as_view(), name='search'),
    path('search/<state>/', SearchItemByStateView.as_view(), name='state'),
    path('wishlist/add/<int:id>/', add_to_wishlist, name='wishlist_add'),
    path('wishlist/delete/<int:id>/', remove_from_wishlist, name='wishlist_remove'),
    path('wishlist/', WishlistView.as_view(), name='wishlist')
]