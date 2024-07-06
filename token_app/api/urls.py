from django.urls import path
from .views import get_balance_view, get_balance_batch_view, get_token_info_view, top_token_holders_view, top_token_holders_info

urlpatterns = [
    path('', get_balance_view, name='get_balance'),
    path('get_balance_batch/', get_balance_batch_view, name='get_balance_batch'),
    path('get_token_info/', get_token_info_view, name='get_token_info'),
    path('top_token_holders/', top_token_holders_view, name='top_token_holders'),
    path('top_token_holders_info/', top_token_holders_info, name='top_token_holders_info'),
]

