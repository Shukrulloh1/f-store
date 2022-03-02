from django.urls import path
from .views import ShopView

app_name = 'shops'

urlpatterns = [
    path('', ShopView.as_view(), name='shop')
]