from unicodedata import name
from django.urls import path     
from . import views
urlpatterns = [
    path('admin/admin-page/add-item/', views.add_item),
    path('admin/admin-page/edit-item/<int:item_id>/', views.edit_item, name="edit_item"),
    path('admin/admin-page/edit-item/<int:item_id>/update-item/<int:same_item_id>/', views.update_item),
    path('admin/admin-page/delete-item/<int:id>/', views.delete_item),
    path('marketplace/add-to-cart/<int:item_id>/<int:user_id>/', views.add_to_cart),
    path('marketplace/view-cart/<int:user_id>/', views.view_cart, name="cart"),
    path('marketplace/view-cart/<int:user_id>/buy-items/', views.buy_items, name="buy"),
    path('marketplace/view-cart/<int:user_id>/remove/<int:item_id>/', views.remove_from_cart, name="remove"),
    # path('marketplace/view-cart/<int:user-id>/update/<int:item_id>/', views.update_cart, name="update")
    # path('admin/admin-page/add-category/', views.add_category)
]
