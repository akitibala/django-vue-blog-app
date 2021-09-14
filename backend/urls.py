from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts', views.SearchList.as_view()),
    # path('posts?word=<str>&word-count=<int>',views.SearchByCountList.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)