from .views import yangiliklar_batafsil_view, news_list_view, contact_view
from django.urls import path, include

urlpatterns = [
    path('', news_list_view, name = 'all_news'),
    path('news/<int:id>/', yangiliklar_batafsil_view, name = 'news_detail'),
    path('contact-us/', contact_view, name= 'contact_page')
]


