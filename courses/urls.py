from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("categories", views.CategoryViewSet, 'category')
router.register("courses", views.CourseViewSet, 'courses')
router.register("lessons", views.LessonViewSet, 'lessons')
router.register("users", views.UserViewSet, 'users')
router.register("comments", views.CommentViewSet, 'comment')



urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view())
]
