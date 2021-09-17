from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views


urlpatterns = [

    re_path(r'^users/$', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    re_path(r'^get-token/$', views.get_csrf_token),

    re_path(r'^posts/$', views.PostList.as_view()),
    re_path(r'^posts/<int:pk>/$', views.PostDetail.as_view()),
    path('posts/<str:term>/', views.SearchWord.as_view()),
    path('posts/<str:word>/<int:count>/',views.SearchWordByCount.as_view())
    

]

urlpatterns = format_suffix_patterns(urlpatterns)