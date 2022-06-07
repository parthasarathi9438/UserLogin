from loginpage import views
from django.urls import path, include
from knox import views as knox_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('tweet', views.TweetViewSet)
router.register('follower', views.FollowerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    #path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]

