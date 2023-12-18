from django.urls import path
from .views import home, quistion, qiuz, result_list, themes_detail, theme_list, statistika
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('quiz/<int:pk>/', quistion, name='quistion'),
    path('results/<int:pk>/', result_list, name='result_detail'),
    path('test/mavzuli/', qiuz, name='thematic'),
    path('mavzu/<slug:slug>/', themes_detail, name='theme'), 
    path('mavzular/', theme_list, name='themes'),
    path('statistika/', statistika, name='statistika')
]