
from django.urls import path
from pages import views as page_views


urlpatterns = [

    path('', page_views.homepage, name='home'),
    path('contact/', page_views.contact, name='contact'),
    path('affiliate/', page_views.affiliate, name='affiliate'),
    path('demo/', page_views.demo, name='demo'),
    # path('pages/', include('pages.urls')),
    
]
