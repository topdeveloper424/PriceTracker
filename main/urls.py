from django.urls import path,include
from . import views
    
app_name = 'main'

urlpatterns = [
    path('', views.home,name='home'),
    path('detail/<int:id>/', views.detail,name='detail'),
    path('get-prices', views.get_prices,name='get_prices'),
    path('update-db', views.update_db,name='update_db'),
]