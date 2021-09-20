from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views


urlpatterns = [

    re_path(r'users/$', views.UserIdAPIView.as_view()),
    re_path(r'register/$', views.UserCreateAPIView.as_view()),

    re_path(r'get-token/$', views.get_csrf_token),
    path('posts/<int:owner>/', views.PostDetail.as_view()),
    re_path(r'posts/$', views.PostList.as_view()),
    
    path('search/<str:term>/', views.SearchWord.as_view()),
    path('search/<str:word>/<int:count>/',views.SearchWordByCount.as_view())
    

]

urlpatterns = format_suffix_patterns(urlpatterns)