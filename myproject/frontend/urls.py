from django.urls import path, include
from .views import call_external_api, call_all_items

urlpatterns = [
    path('items/<int:item_id>', call_external_api, name='items'),
    path('items/', call_all_items, name='items')
]